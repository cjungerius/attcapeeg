from psychopy import core, data
from trial_functions import *
from util_functions import *


def run():

	info = get_subject_info(1234)

# either like this or it is given by the subject info..
	blockTypes = ['search 8', 'search 8/4']
	random.shuffle(blockTypes)

	for blockType in blockTypes:
		targetLocs = [0,1,2,3,4,5,6,7]
		print(blockType)

		if blockType == 'search 8/4': 
			targetLocs = [0,2,4,6]  * 2 # to get same trails num per block?


		factors = {
			'distractor': [True, False],
			'targetloc': targetLocs, # now store block type but no longer target loc
			'trialType': ['search', 'search', 'probe'],
			'lineDir': ['l','r'], 
		}

		trialList = data.createFactorialTrialList(factors)

		trials = data.TrialHandler(trialList,2, method='random')

		# Run the experiment
		for trial in trials:
			print(trial)
			g = general_trial(trial, info, blockType)
			print(g)

	# Close the window
	mywin.close()

	# Close PsychoPy
	core.quit()

if __name__ == '__main__':
	run()

