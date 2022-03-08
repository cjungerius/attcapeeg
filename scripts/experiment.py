from psychopy import core, data
from trial_functions import *



def run():

	# Create factorial design
	factors = {
		'targetloc': [0, 2, 4, 6],
		'distractorloc': [0, 2, 4, 6],
		'distractor': [True, False],
		'trialType': ['search', 'search', 'probe'],
		'lineDir': ['l','r']
	}

	trialList = data.createFactorialTrialList(factors)
	
	trials = data.TrialHandler(trialList,2, method='random')

	# Run the experiment
	for trial in trials:
		print(trial)
		search_trial(trial)

	# Close the window
	mywin.close()
	
	# Close PsychoPy
	core.quit()

if __name__ == '__main__':

	
	run()