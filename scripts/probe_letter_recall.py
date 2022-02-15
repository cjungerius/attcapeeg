# -------------------------------------------------------------------------
# Import libraries 
# -------------------------------------------------------------------------
from psychopy import core, visual, event
import random, os # to later use randomizations
from math import pi, atan, atan2, degrees, cos, sin, pi, radians
import numpy as np

# -------------------------------------------------------------------------
# defining (stimulus) properties 
# -------------------------------------------------------------------------
# create a samller window for visualisation and tests 
win_width = 1250
win_height = 700
win_size = [win_width, win_height] 
height = 28; distance = 60; vertResolution = 1250 

# this later is replaced by the canvas of participants screens
mywin = visual.Window(win_size, monitor="testMonitor")


# -------------------------------------------------------------------------
# making probe recall keybored
# -------------------------------------------------------------------------

All_l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
r_locs = []

# this can later be chnaged to be according to the visual angle as well
# so far made sure that the exact amount of letters are in each row
for y in [0.1, 0, -0.1]:
    for x in np.arange(-0.24,0.25,0.06):
        r_locs.append((x,y)) # later can be changed to visual degree 


def drawLetters(): 
    for i in range(26):
        stim = visual.TextStim(mywin, All_l[i], pos = r_locs[i])
        stim.draw()

def keyboardLettersChange(mywin): 
    correct = True
    lst_pressed_keys = []

    while correct: 
    
        keypress = event.getKeys()
        
        for key in keypress: 
            print(key) # to be sure which keys where pressed 
            # break/exit if space is pressed 
            if key == 'space': 
                    correct = False 
                    break
            # check that only changes if key pressed that are in the ENG alphabet
            elif key.upper() in All_l: 
                drawLetters() # draw the letters
                if key.upper() not in lst_pressed_keys:
                    lst_pressed_keys.append(key.upper())
                print(lst_pressed_keys) # to be sure that the list is appened correctly 
                for i in lst_pressed_keys: # change the letters color to red if pressed
                    stim = visual.TextStim(mywin, i, pos = r_locs[All_l.index(i)])
                    stim.color = 'red'
                    stim.draw()
                mywin.flip()


if __name__ == "__main__": 
    # first draw the window
    drawLetters()
    mywin.update()
    # then wait for which letters are pressed and change their color to red 
    keyboardLettersChange(mywin)
