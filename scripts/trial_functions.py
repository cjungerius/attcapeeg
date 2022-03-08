import random, copy
from display_functions import *
from util_functions import *
from psychopy import core, event



def search_trial(trial, info):
        targetloc = trial['targetloc']
        distractor = trial['distractor']
        lineDir = trial['lineDir']

        contexts = info['contexts']
        target_shape = info['target_shape']
        target_color = info['target_color']
        
        contextnumber = random.choice([0,1,2])
        distractorlocs = list(filter(lambda x: x!= targetloc, [0, 2, 4, 6]))
        distractorloc = distractorlocs[contextnumber]

        shape_arr = copy.deepcopy(contexts[targetloc//2][contextnumber])
        shape_arr.insert(targetloc,target_shape)

        color_arr = [target_color] * 8
        if distractor:
                color_arr[distractorloc] = next(filter(lambda c: c!=target_color,['r','g']))

        drawFixationDisplay(mywin)

        core.wait(.500)

        print(len(shape_arr), len(color_arr))
        drawSearchDisplay(mywin, shape_arr, color_arr)

        event.waitKeys(maxWait = 2.0, keyList=['left','right'])
        
        return


if __name__ == '__main__':
        
        info = get_subject_info(1234)

        trial = {
                'targetloc': 4,
                'distractor': True,
                'lineDir': 'l'
        }

        search_trial(trial, info)