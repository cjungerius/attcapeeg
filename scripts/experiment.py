from psychopy import core, data
from trial_functions import *
from util_functions import *


def run():

	info = get_subject_info(1234)

# Create factorial design
	factors = {
		'targetloc': [0, 2, 4, 6],
		'distractor': [True, False],
		'trialType': ['search', 'search', 'probe'],
		'lineDir': ['l','r'], 
		'novel': [True, False]
	}

	trialList = data.createFactorialTrialList(factors)

	trials = data.TrialHandler(trialList,2, method='random')

	# Run the experiment
	for trial in trials:
		print(trial)
		g = general_trial(trial, info)
		print(g)
	# Close the window
	mywin.close()

	# Close PsychoPy
	core.quit()

if __name__ == '__main__':
	run()

