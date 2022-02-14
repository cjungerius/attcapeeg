#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, os
from psychopy import core, data, visual
from math import atan2, degrees
import display_functions

def run():

	# Create a window

	win = visual.Window([400,300], monitor="testMonitor")




	# Create factorial design
	factors = {
		'targets': [0, 2, 4, 6],
		'distractor': [True, False],
		'trialType': ['search', 'search', 'probe'],
		'lineDir': ['l','r']
	}

	trialList = data.createFactorialTrialList(factors)
	
	trials = data.TrialHandler(trialList,2, method='random')

	# Run the experiment
	for trial in trials:
		print(trial)

	# Close the window
	win.close()
	
	# Close PsychoPy
	core.quit()

if __name__ == '__main__':
	run()