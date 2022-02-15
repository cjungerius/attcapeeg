from psychopy import core, visual, event
from math import pi, atan2, degrees, cos, sin


# -------------------------------------------------------------------------
# parameters
# -------------------------------------------------------------------------

win_width = 1250
win_height = 700

screen_height_cm = 28
screen_height_px = 1250
screen_distance = 60

deg_per_px = degrees(atan2(.5*screen_height_cm, screen_distance)) / (.5*screen_height_px) 

# -------------------------------------------------------------------------
# window
# -------------------------------------------------------------------------

mywin = visual.Window([win_width, win_height], monitor="testMonitor")

# -------------------------------------------------------------------------
# stimuli
# -------------------------------------------------------------------------


stim_c   = visual.Circle(win=mywin,units = 'pix', radius=0.6/deg_per_px,lineWidth=6)
stim_d   = visual.Circle(win=mywin,units = 'pix', radius=0.7/deg_per_px,edges=4,lineWidth=6,ori=90)
stim_h   = visual.Circle(win=mywin,units = 'pix',radius=0.7/deg_per_px,edges=6,lineWidth=6)
stim_s   = visual.Circle(win=mywin,units = 'pix',radius=0.7/deg_per_px,edges=4,lineWidth=6,ori=45)

shapes = {'c': stim_c, 'd': stim_d, 'h': stim_h, 's': stim_s}

# set values for the fixation cross 
fixSize = int(0.2/deg_per_px); LineWidth = int(0.05/deg_per_px)*3

fixCross = visual.ShapeStim(
win = mywin, 
vertices = ((0,-fixSize), (0,fixSize), (0,0), (-fixSize,0), (fixSize,0)),
lineWidth = LineWidth,
closeShape = False,
units = 'pix')
 

# -------------------------------------------------------------------------
# functions 
# -------------------------------------------------------------------------
def calculateCirclePosns(set_size = 8, r = 90): 
    
    circle_posns = [] 
    anglesegment = 2*pi/set_size # calculates the space equally between circle positions depending on the set size
    
    for i in range(set_size):
        x = r * sin(i*anglesegment)    # calculates current x; it is sin as the picture looked like the one rectangle posn is vertaical and not horizintal
        y = r * cos(i*anglesegment)
        circle_posns.append((x, y)) # append circle posns with the current touple of current x and y
    
    return circle_posns # returns the now filled list of circle positions 

def drawFixationDisplay(my_win): 
    # Calculate the number of degrees that correspond to a single pixel
    fixCross.draw()
    my_win.flip()
    core.wait(0.500)

def drawSearchDisplay(my_win): 
    fixCross.draw() # first draw a fixation cross once more
    
    # NOTE: needs to change when clear what target and what distractor will be 
    # also then need to make sure that target and distractor only occur on orthogonals 
    # calculate the circle posns around the center of the screen 
    circle_posns = calculateCirclePosns()
    stimuli = [shapes['c']]*8
    for i, stim in enumerate(stimuli): 
        stim.setLineColor((1,-1,-1)) # set stimuli to red: can change to green (-1,1,-1)
        stim.pos = circle_posns[i]    
        stim.draw()

    my_win.flip()
    event.waitKeys(keyList = 'space')


if __name__ == "__main__": 
    # exucute the functions 
    drawFixationDisplay(mywin)
    drawSearchDisplay(mywin)
