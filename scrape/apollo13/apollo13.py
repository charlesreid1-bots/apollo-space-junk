#!/usr/bin/env python3
import os, glob, re
import requests
from bs4 import BeautifulSoup
import json

"""
Apollo 13 Lunar Flight Journals:

https://www.hq.nasa.gov/alsj/main.html

Apollo 13 Lunar Surface Journals:

https://www.hq.nasa.gov/alsj/a13/a13.html
"""


SCRAPE_DIR = 'scrape'
DATA_DIR = 'data'


SPEAKERS = [
    'Public Affairs Office',
    'SC',
    'MS',
    'Fullerton',
    'Lovell',
    'Lovell (onboard)',
    'Lovell (on board)',
    'Haise',
    'Haise (onboard)',
    'Haise (on board)',
    'Swigert',
    'Swigert (onboard)',
    'Swigert (on board)',
    'NETWORK',
    'MILA',
    'Bermuda',
    'Canary',
    'Kerwin',
    'Brand',
    'Mattingly',
    'Lousma',
    'Lousma',
    'Unrecognized crewman',
    'Duke',
]


def apollo13_lfj_scrape_index():
    """
    Scrape the index of the Apollo 13 Lunar Flight Journal.
    Get each link to a "Day X" page.
    Request the contents of each "Day X" page.
    Save it to a file for later processing.
    """
    lfj_base_link = 'https://web.archive.org/web/20171225232131/https://history.nasa.gov/afj/ap13fj/'

    headers = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    # Make a soup from the page HTML
    r = requests.get(lfj_base_link, headers = headers)
    html_doc = r.text
    soup = BeautifulSoup(html_doc,"lxml")

    # Extract each link to a "Day X" page
    log_links = []
    
    a_s = soup.find_all('a')

    for a_ in a_s:
        link_text = a_.get_text()
        if 'Day ' in link_text \
        or 'Launch and Reaching' in link_text \
        or 'Earth Orbit' in link_text \
        or 'Transposition' in link_text \
        or 'SPS Troubleshooting' in link_text:
            page_name = a_.attrs['href']
            link_name = lfj_base_link + page_name
            log_links.append(link_name)

    if not os.path.exists(SCRAPE_DIR):
        os.mkdir(SCRAPE_DIR)

    # Follow those links!!!
    # Save each page to disk
    for i,link in enumerate(log_links):

        dest = os.path.join(SCRAPE_DIR, os.path.basename(link))

        if not os.path.exists(dest):

            print("Scraping...")
            print("    Link: %s"%(link))
            print("    Target file: %s"%(dest))

            r = requests.get(link, headers=headers)
            html_doc = r.content.decode('utf-8')
            soup = BeautifulSoup(html_doc, "lxml")

            with open(dest,'w') as f:
                f.write(soup.text)

            print("Done.\n")

        else:

            print("Skipping %s, file already exists..."%(dest))

    print("Done scraping Apollo 13 Lunar Flight Journals.")



def apollo13_lfj_extract_dialogue():
    """
    Use the saved "Day X" pages saved to disk to exract dialogue.
    """
    import nltk

    # a list of dictionaries with "speaker" and "token" keys
    all_the_dialogue = []

    hh = 0
    mm = 0

    lfj_files = glob.glob(os.path.join(SCRAPE_DIR,"0*.html"))

    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)

    # For each LFJ transcript, we have plain text,
    # so go through each line and look for speaker: dialogue tokens.
    for lfj_file in lfj_files:

        print("Tokenizing...")
        print("    Target file: %s"%(lfj_file))

        with open(lfj_file,'r') as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, "lxml")

        ## --------------------
        ## tokenize by word:
        #tokens = nltk.wordpunct_tokenize(booty)

        # tokenize by sentence:
        tokens = nltk.tokenize.sent_tokenize(html_doc)

        # split, then flatten list
        tokens = [j.split(": ") for j in tokens]
        tokens = [item for sublist in tokens for item in sublist]

        # split, then flatten list
        tokens = [j.split(" - ") for j in tokens]
        tokens = [item for sublist in tokens for item in sublist]

        # split, then flatten list
        tokens = [j.split("\n") for j in tokens]
        tokens = [item for sublist in tokens for item in sublist]

        # replace double quotes
        tokens = [j.replace('"','') for j in tokens]

        # no mp3 audio clips
        tokens = [j for j in tokens if 'mp3 audio' not in j.lower()]
        tokens = [j for j in tokens if ' kb.' not in j.lower()]

        comm_break = 'comm break'

        tokens = [j for j in tokens if tokens!='']

        # replace timestamps 000:00:00
        # look for "last updated" location
        #
        last_updated_index = 0
        for jj,tok in enumerate(tokens):

            if any([speaker in tok for speaker in SPEAKERS]):

                stripped_tok = re.sub('[0-9]{3}:[0-9]{2}:[0-9]{2} ','',tok)
                stripped_tok2 = re.sub('at [0-9]{3}:[0-9]{2}:[0-9x]{2}','',stripped_tok)
                stripped_tok3 = re.sub(' \(onboard\)','',stripped_tok2)
                tokens[jj] = stripped_tok3
            
            if 'last updated' in tok.lower():
                last_updated_index = jj
        
        if last_updated_index != 0:
            tokens[0:last_updated_index+1] = []

        ii = 0
        while ii < len(tokens):
            if tokens[ii] in SPEAKERS:
                d = {}
                d['speaker'] = tokens[ii]
                ii += 1
                z = []
                while (ii<len(tokens)) and (comm_break not in tokens[ii].lower()) and (tokens[ii] not in SPEAKERS):
                    z.append(tokens[ii])
                    ii += 1
                d['tokens'] = z

                cc = len(all_the_dialogue)
                if ((mm+1)%60)==0:
                    mm=0
                if ((cc+1)%60)==0:
                    hh += 1
                
                d['time'] = '%03d:%02d:00'%(hh,mm)
                all_the_dialogue.append(d)
                mm += 1

            ii += 1
        
        print("Done.")


    out_min = os.path.join(DATA_DIR,'apollo_13_min.txt')
    out_nice = os.path.join(DATA_DIR,'apollo_13.json')

    print("Saving tokens to file:")
    print("    Text: %s"%(out_min))
    print("    Json: %s"%(out_nice))

    with open(out_min,'w') as f:
        for d in all_the_dialogue:
            f.write(json.dumps(d))
            f.write("\n")
    
    with open(out_nice,'w') as f:
        json.dump(all_the_dialogue,f,indent=4)

    print("Done.\n")

    print("Done tokenizing Apollo 13 Lunar Flight Journals.")




def check_for_funky_unicode(txt):
    """
    Given some text, check if there are any funky unicode symbols
    that need to be removed. Print out their names. Add them to
    the strip_funky_unicode() method below.
    """
    import unicodedata
    for c in txt:
        if ord(c) >= 127:
            print('{} U+{:04x} {}'.format(c.encode('utf8'), ord(c), unicodedata.name(c)))

def strip_funky_unicode(txt):
    """
    Scrub out any funk unicode.
    """
    # scrub these unicode symbols from the scraped text
    unicode_key = [
        (u"\u2019",'RIGHT SINGLE QUOTATION MARK','\''),
        (u"\u2013",'EN DASH','-'),
        (u"\u00bd",'VULGAR FRACTION ONE HALF',' 1/2 '),
        (u"\u00be",'VULGAR FRACTION THREE QUARTERS',' 3/4 '),
        (u"\u201d",'RIGHT DOUBLE QUOTATION MARK','"'),
        (u"\u201c",'LEFT DOUBLE QUOTATION MARK','"'),
        (u"\u00b7",'MIDDLE DOT','.'),
        (u"\u00b7",'MIDDLE DOT','.'),
        (u"\u00a9",'COPYRIGHT SIGN',' '),
        (u"\u00e9",'LATIN SMALL LETTER E WITH ACUTE','e'),
        (u"\u00b0",'DEGREE SIGN','o'),
        ]

    for code, name, symbol in unicode_key:
        txt_decode = txt.decode("utf-8")
        txt_replace = txt_decode.replace(code,symbol)
        txt_encode = txt_replace.encode("utf-8")
        txt = txt_encode

    return txt




if __name__=="__main__":

    apollo13_lfj_scrape_index()
    apollo13_lfj_extract_dialogue()


