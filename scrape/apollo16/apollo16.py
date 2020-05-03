#!/usr/bin/env python3
import os, glob, re
import requests
from bs4 import BeautifulSoup
import json

"""
Apollo 16 Lunar Flight Journals:

https://www.hq.nasa.gov/alsj/main.html

Apollo 16 Lunar Surface Journals:

https://www.hq.nasa.gov/alsj/a16/a16.html
"""


SCRAPE_DIR = 'scrape'
DATA_DIR = 'data'

SPEAKERS = [
    'Public Affairs Office',
    'SC',
    'MS',
    'Fullerton',
    'Duke',
    'Duke (onboard)',
    'Duke (on board)',
    'Duke (LM onboard)',
    'Duke (LM)',
    'Young',
    'Young (onboard)',
    'Young (on board)',
    'Young (LM onboard)',
    'Young (LM)',
    'Mattingly',
    'Mattingly (onboard)',
    'Mattingly (on board)',
    'McCandless',
    'Peterson',
    'England',
    'Hartsfield',
    'Haise',
    'Roosa',
    'Roosa(?)',
    'Shaffer',
    'USS Ticonderoga',
    'ELS',
    'Boyd',
    'Morgan',
    'Unidentified',
    'Recovery',
    'Airboss',
    'Chaplain',
    'ANNOTATION',
]


def apollo16_lsj_scrape_index():
    """
    Scrape the index of the Apollo 16 Lunar Surface Journal.
    """
    lsj_base_link = 'https://www.hq.nasa.gov/alsj/a16/'
    lsj_base_page = lsj_base_link+'a16.html'

    headers = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    # Make a soup from the page HTML
    r = requests.get(lsj_base_page, headers = headers)
    html_doc = r.text
    soup = BeautifulSoup(html_doc,"lxml")

    # Extract everything under "<h2>The Journal</h2>"
    log_links = []

    stuff = soup.find_all(['h2','a'])
    
    switch = False
    for s in stuff:
        if s.name=='h2':
            if s.text=='The Journal':
                switch=True
            else:
                switch=False
        if s.name=='a' and switch:
            if 'Flight Journal' not in s.text:
                link_loc = lsj_base_link+"/"+s.attrs['href'] 
                print(link_loc)
                print("Found link:")
                print("    Target: %s"%(link_loc))
                log_links.append(link_loc)

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
            html_doc = r.content.decode('ISO-8859-1')
            soup = BeautifulSoup(html_doc, "lxml")

            with open(dest,'w') as f:
                f.write(soup.text)

            print("Done.\n")

        else:

            print("Skipping %s, file already exists..."%(dest))

    print("Done scraping Apollo 16 Lunar Surface Journals.")


def apollo16_lfj_scrape_index():
    """
    Scrape the index of the Apollo 16 Lunar Flight Journal.
    Get each link to a "Day X" page.
    Request the contents of each "Day X" page.
    Also. "Launch", "Earth", "Transposition", and "SPS".
    Save it to a file for later processing.
    """
    lfj_base_link = 'https://web.archive.org/web/20171225232126/https://history.nasa.gov/afj/ap16fj/'

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
            html_doc = r.content.decode('ISO-8859-1')
            soup = BeautifulSoup(html_doc, "lxml")

            with open(dest,'w') as f:
                f.write(soup.text)

            print("Done.\n")

        else:

            print("Skipping %s, file already exists..."%(dest))

    print("Done scraping Apollo 16 Lunar Flight Journals.")




def apollo16_lsj_extract_dialogue():
    """
    Use the Lunar Surface Journal pages saved to disk to extract dialogue.
    """
    import nltk

    # list of dictionaries with "speaker" and "token" keys
    all_the_dialogue = []

    hh = 0
    mm = 0

    lsj_files = glob.glob(os.path.join(SCRAPE_DIR,"a16*.html"))

    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)

    # For each LFJ transcript, we have plain text,
    # so go through each line and look for speaker: dialogue tokens.
    for lsj_file in lsj_files:

        print("Tokenizing...")
        print("    Target file: %s"%(lsj_file))

        with open(lsj_file,'r') as f:
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

        # ignore these tokens
        tokens = [j for j in tokens if j!='']
        tokens = [j for j in tokens if 'RealAudio' not in j]

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

                #####################
                # after inspecting the output, 
                # we found some problems with 
                # non-dialogue annotations 
                # in brackets showing up as
                # speaker dialogue...
                # this should belong to speaker
                # "ANNOTATION"
                # keep this dictionary ready
                # to add annotations if they
                # do appear.
                #####################
                annotation = {}
                annotation['speaker'] = 'ANNOTATION'
                annotation_tokens = []
                annotation_running = False

                d = {}
                d['speaker'] = tokens[ii]
                ii += 1
                speaker_tokens = []

                while (ii<len(tokens)) and (comm_break not in tokens[ii].lower()) and (tokens[ii] not in SPEAKERS):

                    if tokens[ii][0]=='[':
                        # this is the start of a sequence
                        # of annotation tokens
                        annotation_running = True
                        annotation_tokens.append(tokens[ii])
                        ii += 1

                    elif tokens[ii][-1]==']':
                        # this is the end of a sequence
                        # of annotation tokens
                        annotation_running = False
                        annotation_tokens.append(tokens[ii])
                        ii += 1

                    elif annotation_running:
                        # more annotation tokens
                        annotation_tokens.append(tokens[ii])
                        ii += 1

                    else:
                        # back to speaker tokens
                        speaker_tokens.append(tokens[ii])
                        ii += 1


                # load results into the master dialogue list

                # first the speaker tokens

                d['tokens'] = speaker_tokens

                cc = len(all_the_dialogue)
                if ((mm+1)%60)==0:
                    mm=0
                if ((cc+1)%60)==0:
                    hh += 1
                
                d['time'] = '%03d:%02d:00'%(hh,mm)
                all_the_dialogue.append(d)
                mm += 1


                # now the annotation tokens

                if len(annotation_tokens)>0:

                    annotation['tokens'] = annotation_tokens

                    cc = len(all_the_dialogue)
                    if ((mm+1)%60)==0:
                        mm=0
                    if ((cc+1)%60)==0:
                        hh += 1

                    annotation['time'] = '%03d:%02d:00'%(hh,mm)
                    all_the_dialogue.append(annotation)
                    mm += 1

            ii += 1
        
        print("Done.")


    out_min = os.path.join(DATA_DIR,'apollo_16_sj_min.txt')
    out_nice = os.path.join(DATA_DIR,'apollo_16_sj.json')

    print("Saving tokens to file:")
    print("    Text: %s"%(out_min))
    print("    Json: %s"%(out_nice))

    with open(out_min,'w') as f:
        for d in all_the_dialogue:
            f.write(json.dumps(d))
            f.write("\n")
    
    with open(out_nice,'w') as f:
        json.dump(all_the_dialogue,f)

    print("Done.\n")

    print("Done tokenizing Apollo 16 Lunar Surface Journals.")



def apollo16_lfj_extract_dialogue():
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


    out_min = os.path.join(DATA_DIR,'apollo_16_min.txt')
    out_nice = os.path.join(DATA_DIR,'apollo_16.json')

    print("Saving tokens to file:")
    print("    Text: %s"%(out_min))
    print("    Json: %s"%(out_nice))

    with open(out_min,'w') as f:
        for d in all_the_dialogue:
            f.write(json.dumps(d))
            f.write("\n")
    
    with open(out_nice,'w') as f:
        json.dump(all_the_dialogue,f)

    print("Done.\n")

    print("Done tokenizing Apollo 16 Lunar Flight Journals.")



if __name__=="__main__":

    #apollo16_lfj_scrape_index()
    apollo16_lfj_extract_dialogue()

    #apollo16_lsj_scrape_index()
    apollo16_lsj_extract_dialogue()


