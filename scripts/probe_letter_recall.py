# -------------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------------
from psychopy import visual, event
import numpy as np
from string import ascii_uppercase

# -------------------------------------------------------------------------
# making probe recall keybored
# -------------------------------------------------------------------------


def drawLetters(mywin, reported_letters=set()):

    r_locs = []

    # this can later be chnaged to be according to the visual angle as well
    # so far made sure that the exact amount of letters are in each row
    for y in [0.1, 0, -0.1]:
        for x in np.arange(-0.24, 0.25, 0.06):
            r_locs.append((x, y))  # later can be changed to visual degree

    for i, letter in enumerate(ascii_uppercase):
        stim = visual.TextStim(mywin, letter, pos=r_locs[i])
        if letter in reported_letters:
            stim.color = 'red'
        stim.draw()
    mywin.flip()


def letterListener(mywin):
    waiting = True
    reported_letters = set()

    while waiting:

        keypress = event.getKeys()

        for key in keypress:
            print(key)  # to be sure which keys where pressed
            # break/exit if space is pressed
            if key == 'space':
                waiting = False
                break
            # check that only changes if key pressed that are in the ENG alphabet
            elif key.upper() in ascii_uppercase:
                reported_letters.add(key.upper())
                drawLetters(mywin, reported_letters)  # draw the letters
                # to be sure that the list is appened correctly
                print(reported_letters)

    return reported_letters


if __name__ == "__main__":
    # -------------------------------------------------------------------------
    # defining (stimulus) properties
    # -------------------------------------------------------------------------
    # create a samller window for visualisation and tests
    win_width = 1250
    win_height = 700
    win_size = [win_width, win_height]
    height = 28
    distance = 60
    vertResolution = 1250

    # this later is replaced by the canvas of participants screens

    mywin = visual.Window(win_size, monitor="testMonitor")
    # first draw the window
    drawLetters(mywin)
    letterListener(mywin)
