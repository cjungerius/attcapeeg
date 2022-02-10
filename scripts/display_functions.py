# -------------------------------------------------------------------------
# Import libraries 
# -------------------------------------------------------------------------
from psychopy import core, visual, event
from math import pi, atan2, degrees, cos, sin, pi, radians
import random # to later use randomizations

# -------------------------------------------------------------------------
# important functions 
# -------------------------------------------------------------------------
def calculateCirclePosns(center_x, center_y, set_size = 8, r = 90): 
    
    circle_posns = [] # creates the list circle positons will be stored in
    anglesegment = 2*pi/set_size # calculates the space equally between circle positions depending on the set size
    
    for i in range(set_size):
        curr_x = r * sin(i*anglesegment) + center_x # calculates current x; it is sin as the picture looked like the one rectangle posn is vertaical and not horizintal
        curr_y = r * cos(i*anglesegment) + center_y
        circle_posns.append((curr_x, curr_y)) # append circle posns with the current touple of current x and y
    
    return circle_posns # returns the now filled list of circle positions 

# -------------------------------------------------------------------------
# defining (stimulus) properties 
# -------------------------------------------------------------------------
# create a samller window for visualisation and tests 
win_width = 1250
win_height = 700
win_size = [win_width, win_height] 
height = 28; distance = 60; vertResolution = 1250 

# set the set size to 8 
set_size = 8

# inidate the stimuli with the respective colours 
shape_colours = ['green', 'red']

shapes_green = ['green_circle.png', 'green_diamond.png', 
                'green_hexagon.png', 'green_square.png'] * 2

shapes_red = ['red_circle.png', 'red_diamond.png', 
                'red_hexagon.png', 'red_square.png'] * 2

# to randomize the pictures 
random.shuffle(shapes_green)
random.shuffle(shapes_red)



# Calculate the number of degrees that correspond to a single pixel
deg_per_px = degrees(atan2(.5*height, distance)) / (.5*vertResolution) 

# set values for the fixation cross 
fixSize = int(0.2/deg_per_px); LineWidth = int(0.05/deg_per_px)

# this later is replaced by the canvas of participants screens
mywin = visual.Window(win_size, monitor="testMonitor")

# create the fixation cross 
fixCross = visual.ShapeStim(
    win = mywin, 
    vertices = ((0,-fixSize), (0,fixSize), (0,0), (-fixSize,0), (fixSize,0)),
    lineWidth = LineWidth*3,
    closeShape = False,
    units = 'pix')
    

# calculate the circle posns around the center of the screen 
circle_posns = calculateCirclePosns(0,0)

print(circle_posns) # see if they are correct 
# -------------------------------------------------------------------------
# draw fixation display to see if the fixation calculation works 
# -------------------------------------------------------------------------
fixCross.draw()
mywin.flip()
core.wait(0.500) # so that the fixation display is shown for 500ms 
#event.waitKeys(keyList = 'space')

# -------------------------------------------------------------------------
# now draw the second display to see if the calculated circle posns work
# -------------------------------------------------------------------------
# first draw a fixation cross once more
fixCross.draw()

# then loop through stimuli (here green but with a simple if-else you could 
# descide if red or green shown)
# NOTE: needs to change when clear what target and what distractor will be 
# also then need to make sure that target and distractor only occur on orthogonals 

for i in range(set_size): 
    mypic = shapes_red[i-1] # or shapes_green[i-1]
    img = visual.ImageStim(
        win=mywin,
        image=mypic,
        units="pix",
        pos=circle_posns[i-1]
    )
    # scale the images to be smaller
    size_x = img.size[0]
    size_y = img.size[1]

    img.size = [size_x * 0.5, size_y * 0.5]
    
    img.draw()

mywin.flip()
event.waitKeys(keyList = 'space')
