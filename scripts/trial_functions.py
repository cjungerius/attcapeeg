import random, copy
from display_functions import *
from util_functions import *
from probe_letter_recall import *
from psychopy import core, event
import itertools



def general_trial(trial, info):
        targetloc = trial['targetloc']
        distractor = trial['distractor']
        lineDir = trial['lineDir']
        
        trialType = trial['trialType']
        novel = trial['novel']

        target_shape = info['target_shape']
        target_color = info['target_color']

        learned_contexts = info['contexts']
        print(learned_contexts)
        # this should still work I think for the distractor to be random 
        contextnumber = random.choice([0,1,2])
        distractorlocs = list(filter(lambda x: x!= targetloc, [0, 2, 4, 6]))
        distractorloc = distractorlocs[contextnumber]

        if novel == False: # means that contexts are learned 
            shape_arr = copy.deepcopy(learned_contexts[targetloc//2][contextnumber])
            shape_arr.insert(targetloc,target_shape)
            #print(shape_arr)

        elif novel == True: 
            
            learned_contexts_f = list(itertools.chain(*learned_contexts))
            
            while True: 
                shape_arr = ['', '', '', '', '', '', '', '']
                shape_arr[targetloc] = target_shape
            
                if target_shape == 'c': 
                    other_shapes = ['s', 's', 's', 'h', 'h', 'h', 'd']
                else: 
                    other_shapes = ['s', 's', 's', 'h', 'h', 'h', 'c']
                random.shuffle(other_shapes) 
                
                if other_shapes not in learned_contexts_f: 
                    print(other_shapes)
                    other_shapes.reverse() # need to so that later pop in same 
                    # order 
                    for i in range(8):
                        if i != targetloc:
                            shape_arr[i] = other_shapes.pop()
                    
                    print(shape_arr)
                    break


        color_arr = [target_color] * 8
        if distractor:
                color_arr[distractorloc] = next(filter(lambda c: c!=target_color,['r','g']))

        drawFixationDisplay(mywin)

        core.wait(.500)

        #print(len(shape_arr), len(color_arr))
        #drawSearchDisplay(mywin, shape_arr, color_arr)
        #event.waitKeys(maxWait = 2.0, keyList=['left','right'])
        
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
            # maybe we need to report them back as well
            
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
            # do we want a ratio here? 

        return response, used_letters 


if __name__ == '__main__':
        
        info = get_subject_info(1234)

        trial = {
                'targetloc': 4,
                'distractor': True,
                'trialType': 'search',
                'lineDir': 'l',
                'novel': True 
        }

        r = general_trial(trial, info)
        # to see if returned response value workes correctly 
        print(r)
