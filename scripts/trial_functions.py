import random, copy
from display_functions import *
from util_functions import *
from probe_letter_recall import *
from psychopy import core, event
import itertools



def general_trial(trial, info, blockType):
        targetloc = trial['targetloc']
        distractor = trial['distractor']
        lineDir = trial['lineDir']
        
        trialType = trial['trialType']

        target_shape = info['target_shape']
        target_color = info['target_color']

        if blockType == 'search 8':
            targetLocs = [0,1,2,3,4,5,6,7]
            number = random.choice([0,1,2,3,4,5,6])
            distractorlocs = list(filter(lambda x: x!= targetloc, targetLocs))
            distractorloc = distractorlocs[number]
        elif blockType == 'search 8/4': 
            targetLocs = [0,2,4,6]
            number = random.choice([0,1,2])
            distractorlocs = list(filter(lambda x: x!= targetloc, targetLocs))
            distractorloc = distractorlocs[number]

        if target_shape == 'c': 
            shape_arr = ['s', 's', 's', 'h', 'h', 'h', 'd']
        else: 
            shape_arr = ['s', 's', 's', 'h', 'h', 'h', 'c']
        random.shuffle(shape_arr) 


        shape_arr.insert(targetloc,target_shape)
        
        color_arr = [target_color] * 8
        if distractor:
                color_arr[distractorloc] = next(filter(lambda c: c!=target_color,['r','g']))

        drawFixationDisplay(mywin)

        core.wait(.500)

        if trialType == 'search': 
            line_arr = ['', '', '', '', '', '', '', '']
            line_arr[targetloc] = lineDir
            
            if lineDir == 'r': 
                lines = [lineDir] * 3 + ['l']*4
            else: 
                lines = [lineDir] * 3 + ['r']*4
                    
            random.shuffle(lines)
            
            # to create line_arr
            for i in range(8):
                if i != targetloc:
                    line_arr[i] = lines.pop()
            

            # draw the search display
            drawDisplay(mywin, shape_arr, color_arr, 'search', line_arr)


            # wait for answer 
            button_pressed = event.waitKeys(maxWait = 2.0, keyList=['left','right'])
            response = None 
            
            if button_pressed != None: 
                button_pressed = button_pressed.pop()
                if lineDir in button_pressed:
                    response = True 
                elif lineDir not in button_pressed:
                    response = False # clicked wrong or too slow 
            
            used_letters = [] # so that later for the letter probe it can be returned

        else: 
            letter_arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            random.shuffle(letter_arr) # shuffle them 
            
            used_letters = letter_arr[0:8] # only first 8 letters used
            
            # draw the letters for 100msec
            drawDisplay(mywin, shape_arr, color_arr, 'probe letter', used_letters)
            core.wait(.100) # wait for 100msec 
            
            # draw the mask for 500msec
            drawDisplay(mywin, shape_arr, color_arr, 'probe mask', [])
            core.wait(.500) # wait for 500msec 
            
            
            # then draw answer display
            drawLetters(mywin)
            
            
            # wait for answer
            response = letterListener(mywin)

        return response, used_letters 


if __name__ == '__main__':
        
        info = get_subject_info(1234)

        trial = {
                'targetloc': 4,
                'distractor': True,
                'trialType': 'search',
                'lineDir': 'l',
        }

        r = general_trial(trial, info)
        # to see if returned response value workes correctly 
        print(r)
