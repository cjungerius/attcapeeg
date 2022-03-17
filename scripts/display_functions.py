from psychopy import core, visual, event
from math import pi, atan2, degrees, cos, sin
import random


# -------------------------------------------------------------------------
# parameters
# -------------------------------------------------------------------------

win_width = 1250
win_height = 700

screen_height_cm = 28
screen_height_px = 1250
screen_distance = 60

deg_per_px = degrees(
    atan2(.5*screen_height_cm, screen_distance)) / (.5*screen_height_px)
px2deg = 36  # to later avoid magic numbers

# -------------------------------------------------------------------------
# window
# -------------------------------------------------------------------------

mywin = visual.Window([win_width, win_height], monitor="testMonitor")

# -------------------------------------------------------------------------
# stimuli
# -------------------------------------------------------------------------


stim_c = visual.Circle(win=mywin, units='pix',
                       radius=0.6/deg_per_px, lineWidth=6)
stim_d = visual.Circle(win=mywin, units='pix', radius=0.7 /
                       deg_per_px, edges=4, lineWidth=6, ori=90)
stim_h = visual.Circle(win=mywin, units='pix',
                       radius=0.7/deg_per_px, edges=6, lineWidth=6)
stim_s = visual.Circle(win=mywin, units='pix', radius=0.7 /
                       deg_per_px, edges=4, lineWidth=6, ori=45)

shapes = {'c': stim_c, 'd': stim_d, 'h': stim_h, 's': stim_s}

# set values for the fixation cross
fixSize = int(0.2/deg_per_px); LineWidth = int(0.05/deg_per_px)*3

fixCross = visual.ShapeStim(
win=mywin,
vertices=((0, -fixSize), (0, fixSize), (0, 0), (-fixSize, 0), (fixSize, 0)),
lineWidth=LineWidth,
closeShape=False,
units='pix')


# -------------------------------------------------------------------------
# functions
# -------------------------------------------------------------------------
def calculateCirclePosns(set_size=8, r=90):

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

def drawDisplay(my_win, shape_arr, color_arr, display_type, to_draw):
    fixCross.draw() # first draw a fixation cross once more
    
    circle_posns = calculateCirclePosns()
    stimuli = [shapes.get(shape) for shape in shape_arr]

    for i, stim in enumerate(stimuli):
        if stim is not None:            
            if color_arr[i] == 'r':
                stim.setLineColor((1,-1,-1)) #red
            elif color_arr[i] == 'g':
                stim.setLineColor((-1,1,-1)) # green
            else:
                stim.setLineColor((-1,-1,-1))
            stim.pos = circle_posns[i]
            stim.draw()

        if display_type == 'search': 
            line = visual.Line(win=my_win,units="pix",lineColor=[-1, -1, -1])
            
            if to_draw[i] == 'l': 
                line.start = [circle_posns[i][0]-0.3*px2deg, circle_posns[i][1]]
                line.end = [circle_posns[i][0]-0.6*px2deg, circle_posns[i][1]]
            
            else: 
                line.start = [circle_posns[i][0]+0.3*px2deg, circle_posns[i][1]]
                line.end = [circle_posns[i][0]+0.6*px2deg, circle_posns[i][1]]
                        
            line.lineWidth = 3
            line.draw()

        elif display_type == 'letter': 
            text = visual.TextStim(win=my_win, units='pix', text=to_draw[i], height= 36, pos=circle_posns[i])
            text.draw()

        elif display_type == 'mask': 
            text = visual.TextStim(win=my_win, units='pix', text='#', height = 36, pos=circle_posns[i])
            text.draw()

    my_win.flip()
    
if __name__ == "__main__":
    shape_arr = ['c', 's', 's', 's', 'd', 'h', 'h', 'h']
    color_arr = ['r', 'r', 'r', 'r', 'g', 'r', 'r','r']
    line_arr = ['l', 'r', 'l', 'r', 'r', 'l', 'l', 'r']
    letter_arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    random.shuffle(letter_arr)

    # exucute the functions press space to continue
    drawFixationDisplay(mywin)
    event.waitKeys(keyList=['space'])
    drawDisplay(mywin, shape_arr, color_arr, 'letter', letter_arr)
    event.waitKeys(keyList=['space'])
    drawDisplay(mywin, shape_arr, color_arr, 'mask', [])
    event.waitKeys(keyList=['space'])
    drawDisplay(mywin, shape_arr, color_arr, 'search', line_arr)
    event.waitKeys(keyList=['space'])
