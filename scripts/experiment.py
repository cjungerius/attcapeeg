#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The first line is called the hash bang. It helps operating systems 
# understand what to do with this script. The second line describes 
# the encoding of this file. UTF-8 is the only one used nowadays.
# It supports all alphabeths, even runes and linear B.
 
# Import the PsychoPy libraries that you want to use
from psychopy import core, visual
 
# Create a window
win = visual.Window([400,300], monitor="testMonitor")
 
# Create a stimulus for a certain window
message = visual.TextStim(win, text="Hello World!")
 
# Draw the stimulus to the window. We always draw at the back buffer of the window.
message.draw()
 
# Flip back buffer and front  buffer of the window.
win.flip()
 
#a Pause 5 s, so you get a chance to see it!
core.wait(5.0)
 
# Close the window
win.close()
 
# Close PsychoPy
core.quit()