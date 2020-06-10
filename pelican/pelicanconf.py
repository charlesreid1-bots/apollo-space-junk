import markdown

AUTHOR = 'charlesreid1'
SITENAME = 'apollo space junk bot flock'
SITEURL = ''#'b-apollo'
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# --------------8<---------------------

THEME = 'scurvy-knave-theme'

LICENSE_URL = "https://opensource.org/licenses/MIT"
LICENSE_NAME = "MIT License"

# Pelican is designed for files => pages.
# Use variables (below) to set pieces of pages.

# twitter blue
INTROCOLOR  = "#fff"
ACOLOR      = "#00aced"
AHOVERCOLOR = "#0084b4"
BRIGHTCOLOR = "#1dcaff"
TEMPLATE_PAGES = {
    'custom.css' : 'custom.css'
}

INTROBKG='img/flare.jpg'
LINKSBKG='img/buttons.jpg'

# img/ should be in content/
# available at <url>/img
STATIC_PATHS = ['img']

# ---

# description appears between <p> tags, so don't include them

SITE_TITLE = "apollo space junk bot flock"
SITE_DESCRIPTION = "On an imaginary circumlunar trajectory, forever."
GITEA_URL = "https://github.com/charlesreid1-bots/apollo-space-junk"

# ---

about_md = markdown.Markdown(extensions=['extra','codehilite'],
                             output_format='html4')

ABOUT_SHORT = "About"

ABOUT_TITLE = "about apollo space junk bot flock"

ABOUT_TEXT = """

<br />

**What is the apollo space junk bot flock?**

The apollo space junk bot flock is a flock of twitter bots that tweet random Apollo radio dialogue.

The flock is implemented in Python and uses the 
[rainbow mind machine](https://pages.charlesreid1.com/rainbow-mind-machine)
library.

Each bot is given the entire contents of the transcripts of the corresponding 
Apollo mission, and the bot chops up the corpus and uses it to generate 
dialogue in the same style. 

The text processing portion was implemented using [leonardr/olipy](https://github.com/leonardr/olipy)
on Github, which implements the Queneau assembly algorithm that is used 
by the bot flock to generate dialogue.

For more information about bots and bot flocks, see [bots.charlesreid1.com](https://bots.charlesreid1.com).

Find the bots on twitter at the [apollo space junk bot flock twitter list](https://twitter.com/i/lists/1267145550496858113)

[@apollo11junk](https://twitter.com/apollo11junk) &bull; 
[@apollo12junk](https://twitter.com/apollo12junk) &bull; 
[@apollo13junk](https://twitter.com/apollo13junk) &bull;
[@apollo14junk](https://twitter.com/apollo14junk) &bull;
[@apollo14junk](https://twitter.com/apollo15junk) &bull;
[@apollo14junk](https://twitter.com/apollo16junk) &bull;
[@apollo15junk](https://twitter.com/apollo17junk)

<br />

**Why build the apollo space junk bot flock?**

The Apollo Space Junk bots are robots that create and publish tweets. 
But the tweets they create are randomly generated. The bots learn how 
to speak by being given a large corpus of dialogue, and they construct
new dialogue by repeating and re-using language at the phrase level, 
instead of the letter- or word-level often used in random text generation algorithms.

The tweets have the same authentic sound as the original dialogue: 
dense and thickly technical exchanges, interspersed with moments where
the humanity of the astronauts shines through. 

The space junk bots take on a personality all their own.

<br />

<blockquote class="twitter-tweet ubuntu" data-lang="en"><p lang="en" dir="ltr">Armstrong: Coming into the terminator.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/988590995485814784?ref_src=twsrc%5Etfw">April 24, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<br />

<div>
<blockquote class="twitter-tweet ubuntu" data-lang="en"><p lang="en" dir="ltr">Swigert: Yes. I think we ought to be having AOS, gang; we&#39;ve got... Lovell Give me a call when you&#39;re ready for E-memory dump. Okay.</p>&mdash; Apollo 13 Space Junk (@apollo13junk) <a href="https://twitter.com/apollo13junk/status/746895028153245696">June 26, 2016</a></blockquote>
</script>
</div>

<br />

<div style="align:right;">
<blockquote class="twitter-tweet ubuntu" lang="en"><p>Bean: Try to get it out of the center hatch window now, Houston. It really is beautiful. That mark looks just like a nose; about the same</p>&mdash; Apollo 12 Space Junk (@apollo12junk) <a href="https://twitter.com/apollo12junk/status/552697699582357504">January 7, 2015</a></blockquote>
</script>
</div>

<br />

<blockquote class="twitter-tweet ubuntu" data-lang="en"><p lang="en" dir="ltr">Armstrong: Boy, this water separator sure isn&#39;t working worth a durn. Yes.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/989567018226495488?ref_src=twsrc%5Etfw">April 26, 2018</a></blockquote>
</script>

<br />

<blockquote class="twitter-tweet ubuntu" data-lang="en"><p lang="en" dir="ltr">Duke: Roger, Buzz. Over. You are stay for a T3. Could you describe, from your view, the polar cloud cap? We got the network all configured for the TV. [Pause.]</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/989534549116837888?ref_src=twsrc%5Etfw">April 26, 2018</a></blockquote>
</script>

<br />

<blockquote class="twitter-tweet ubuntu" data-lang="en"><p lang="en" dir="ltr">Duke: 11, your friendly geologist says it&#39;s the camera cank - crank, excuse me, for the 16-sequence camera if it jams. Your angles are 270 in yaw, pitch minus 50. To us you are just bringing it down by the optics now. Thanks again for a great show, you guys.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/988592508006383616?ref_src=twsrc%5Etfw">April 24, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<br />

<blockquote class="twitter-tweet ubuntu" lang="en"><p>McCandless: Go ahead, 11. And I&#39;d like to pass up your Delta azimuth correction at this time if you&#39;re ready to copy.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/551686395681452032">January 4, 2015</a></blockquote>
</script>

<br />

<blockquote class="twitter-tweet ubuntu" lang="en"><p>Evans: Apollo 11, Houston. Just about, though. We got about 2 minutes to LOS here, Mike. Over.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/551443999626915841">January 3, 2015</a></blockquote>
</script>

<br />

<blockquote class="twitter-tweet ubuntu" lang="en"><p>Boston out hit Baltimore to score 6 runs to the Orioles&#39; 2; and Chicago beat Kansas City 6 to 1. Loud and clear. It looks okay to us.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/550302963311181825">December 31, 2014</a></blockquote>
</script>

<br />

<blockquote class="twitter-tweet ubuntu" lang="en"><p>Collins: I said the Czar is brushing his teeth, so I&#39;m filling in for him. Good.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/552305959511789569">January 6, 2015</a></blockquote>
</script>

<br />

<blockquote class="twitter-tweet ubuntu" lang="en"><p>Collins: Let me know when it&#39;s lunch time, will you?</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/550850060582281217">January 2, 2015</a></blockquote>
</script>

<br />

<blockquote class="twitter-tweet ubuntu" lang="en"><p>Over.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/548438294191554560">December 26, 2014</a></blockquote>
</script>

<br />

<blockquote class="twitter-tweet ubuntu" lang="en"><p>Armstrong: (Joking) You can&#39;t get away with anything anymore, can you? Yes, it&#39;s about a second off.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/548438652507152384">December 26, 2014</a></blockquote>
</script>

<br />

<blockquote class="twitter-tweet ubuntu" lang="en"><p>McCandless: There we go, the salmon salad, very good. Reading you loud and clear. One thing that we did miss in the drop-out in the noise</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/552305204193161216">January 6, 2015</a></blockquote>
</script>

<br />

<blockquote class="twitter-tweet ubuntu" lang="en"><p>on panel 251 also. Roll for Sep 357, 107, 041; 301, 287, 319. [No answer.] The feature that I was describing to you - the small bright</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/552305205946368001">January 6, 2015</a></blockquote>
</script>

<br />

<blockquote class="twitter-tweet ubuntu" lang="en"><p>Duke: Houston. About 50 percent of the time, we&#39;re getting high bit rate off the omnis when you&#39;re in PTC. Copy, 11. [Long pause.] Copy.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/548621624699011073">December 26, 2014</a></blockquote>
</script>

<br />

<blockquote class="twitter-tweet ubuntu" lang="en"><p>Collins: That&#39;s affirmative.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/548621859910975488">December 26, 2014</a></blockquote>
</script>

<br />

<blockquote class="twitter-tweet ubuntu" lang="en"><p>Collins: See that, Buzz?</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/552163884207861761">January 5, 2015</a></blockquote>
</script>

<br />

<blockquote class="twitter-tweet ubuntu" lang="en"><p>Aldrin: Roger.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/552163999903514626">January 5, 2015</a></blockquote>
</script>

<br />

<blockquote class="twitter-tweet ubuntu" lang="en"><p>Armstrong: Yes.</p>&mdash; Apollo 11 Space Junk (@apollo11junk) <a href="https://twitter.com/apollo11junk/status/552164326107148288">January 5, 2015</a></blockquote>
</script>

"""

ABOUT_DESCRIPTION = about_md.convert(ABOUT_TEXT)



# -----------


# This is where we document various webhook endpoints.

LINKS_TITLE = "On The Web"

LINKS_DESCRIPTION = """
<p><a class="btn btn-default btn-lg" href="https://github.com/charlesreid1-bots/apollo-space-junk">
<i class="fa fa-fw fa-2x fa-github"></i> github.com/charlesreid1-bots/apollo-space-junk
</a></p>

<p><a class="btn btn-default btn-lg" href="https://pages.charlesreid1.com/b-apollo">
<i class="fa fa-fw fa-2x fa-globe"></i> pages.charlesreid1.com/b-apollo
</a></p>
"""


# ---


CONTACT_TITLE = "Contact charlesreid1"

CONTACT_DESCRIPTION = """<p>@charlesreid1 is a full-time data engineer and part-time bot-wrangler working on
the intersection of cloud computing and genomics at UC Santa Cruz.</p>
<p>Get in touch:</p>
<p><a href="mailto:twitter@charlesreid1.com">twitter (at) charlesreid1.com</a></p>
"""

ATTRIBUTION = """
<p style="font-size: 12px;">Image credit: <a href="https://nasa.gov">NASA</a> and 1960s U.S. taxpayers
"""


# --------------8<---------------------

DISPLAY_PAGES_ON_MENU = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False
