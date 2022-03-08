from display_functions import *
from psychopy import core, event

def search_trial(trial):
        targetloc = trial['targetloc'],
        distractor = trial['distractor']
        lineDir = trial['lineDir']

        drawFixationDisplay(mywin)

        core.wait(.500)

        drawSearchDisplay(mywin)

        event.waitKeys(maxWait = 10.0, keyList=['left','right'])
        
        return


if __name__ == '__main__':
        target_shape = 'c'
        target_color = 'g'

        trial = {
                'targetloc': 4,
                'distractor': True,
                'lineDir': 'l'
        }

        search_trial(trial)