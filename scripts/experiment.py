from psychopy import core, data
from trial_functions import *
from util_functions import *


def run():

	info = get_subject_info(1234)

# Create factorial design

	mapperfactors = {
		'targetloc': [0,1,2,3,4,5,6,7]
	}

	mapperTrialList = data.createFactorialTrialList(mapperfactors)
	mappertrials = data.TrialHandler(mapperTrialList, 10, method='random')

	for trial in mappertrials:
		print(trial)
		g = mapper_trial(trial)
		print(g)

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
