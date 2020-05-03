import rainbowmindmachine as rmm
import os, glob
import logging

ch = logging.StreamHandler()
logger = logging.getLogger('')
logger.setLevel(logging.INFO)
logger.addHandler(ch)

fh = logging.FileHandler(filename='rmm_apollo.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)

DATADIR = os.path.join(os.getcwd(), 'data')
KEYSDIR = os.path.join(os.getcwd(), 'keys')

def setup():
    k = rmm.TxtKeymaker()
    k.set_apikeys_file('apikeys.json')
    k.make_keys(DATADIR, KEYSDIR)
    
def run():
    sh = rmm.TwitterShepherd(
            KEYSDIR, 
            flock_name = 'apollo',
            sheep_class=rmm.QueneauSheep
    )


    LIVE = True


    if not LIVE:
        sh.perform_parallel_action(
                'tweet',
                **{
                    'publish' : False,
                    'inner_sleep' : 1,#3*60,
                    'outer_sleep' : 1,#2*3600,
                    'lines_length' : 4
                }
        )
    else:
        sh.perform_parallel_action(
                'tweet',
                **{
                    'publish' : True,
                    'inner_sleep' : 3*60,
                    'outer_sleep' : 2*3600,
                    'lines_length' : 4
                }
        )


if __name__=="__main__":

    keys_exists = os.path.isdir(KEYSDIR)
    keys_has_keys = len(glob.glob(os.path.join(KEYSDIR,"*.json"))) > 0
    if( keys_exists and keys_has_keys ):
        print("running bot")
        run()
    else:
        print("setting up bot")
        setup()

