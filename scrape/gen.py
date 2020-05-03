import sys, json

sys.path.append('/Users/charles/codes/olipy/olipy')
from queneau import DialogueAssembler

"""
To use olipy:

Step 1:
    git clone http://github.com/leonardr/olipy /path/to/olipy

Step 2:
    add /path/to/olipy to $PYTHONPATH
    add to your .profile:
    export PYTHONPATH="/path/to/olipy:$PYTHONPATH"

Step 3:
    good to go!
"""

def make_fj(which):
    f = "apollo%s/data/apollo_%s_min.txt"%(which,which)
    make(f)

def make_sj(which):
    f = "apollo%s/data/apollo_%s_sj_min.txt"%(which,which)
    make(f)

def make(f):
    d = DialogueAssembler.loadlines(open(f))
    last_speaker = None
    for i in range(1, 100):
        speaker = ''
        while (speaker=='' or speaker=='ANNOTATION'):
            speaker, tokens = d.assemble(last_speaker)
        last_speaker = speaker
        print("%s: %s\n" % (speaker, " ".join(x for x, y in tokens)))

if __name__=="__main__":
    print("="*40)
    make_fj('14')
    print("="*40)
    make_sj('14')
