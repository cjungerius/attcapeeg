from psychopy import visual, event
from display_functions import *
import os

# if images used than this 
path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir = dir.replace('scripts', 'media')
os.chdir(dir)

def drawBoxes(x,y): 
    # position: (.1, -.2) or (.1, -.6)
    polygon_next = visual.Rect(mywin, width = 0.14, height = 0.1, pos = (x,y), ori=0,
    lineWidth=1, lineColor=[0.6549, 0.6549, 0.6549], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, interpolate=True)

    polygon_next.draw()
    
    polygon_prev = visual.Rect(mywin, width = 0.18, height = 0.1, pos = (-x,y), ori=0,
    lineWidth=1, lineColor=[0.6549, 0.6549, 0.6549], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, interpolate=True)

    polygon_prev.draw()
    
    next_text = visual.TextStim(mywin,
    text='Next >',
    font='Arial',
    pos=(x,y), height=0.06, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1)

    next_text.draw()
    
    prev_text = visual.TextStim(mywin,
    text='< Previous',
    font='Arial',
    pos=(-x,y), height=0.06, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1)

    prev_text.draw()
    
    return polygon_next, polygon_prev



def instructionScreensPictures(mywin, target_shape = 'c', target_colour = 'r'): 
    i = 0 # initate start val
    mouse = event.Mouse(win=mywin)

    pn, pp = drawBoxes(.1,-.2)
    inst_text = visual.TextStim(mywin, 'Welcome to the experiment! We will instruct you to the task you will preform'
                                    , units = "pix")



    inst_text.color = 'black'
    inst_text.height = 20
    inst_text.draw()

    mywin.flip()

    while i < 7: 
        
        pressed = False

        if mouse.isPressedIn(pn):
            i = i + 1
            pressed = True

        if mouse.isPressedIn(pp) and i != 0: # make sure that in welcome no previous possible 
            i = i - 1
            pressed = True
            
        if pressed == True:
            if i == 1 or i == 2 or i == 3: 
                if i == 1: 
                    inst_text = visual.TextStim(mywin, 'In each trial, a brief fixation will appear - please center your gaze on the fiaxtion cross when it appears.', units="pix")
                    img = visual.ImageStim(mywin, image='inst_fix.png', units="pix")
                    img.size = img.size*0.3
                if i == 2: 
                    inst_text = visual.TextStim(mywin, 'Next, a number of coloured stimuli will appear.', units="pix")
                    img = visual.ImageStim(mywin, image='inst_search_'+ target_colour +'.png', units="pix")
                    img.size = img.size*0.3
                if i == 3: 
                    inst_text = visual.TextStim(mywin, text = 'Your task is to search for the *' + ("diamond" if target_shape == 'd' else "circle")+ '*, then react to the line segment inside it. If the line segment points to the left, press the left arrow key; if the line segment points to the right, press the right arrow key.', units="pix")
                    img = visual.ImageStim(mywin, image='inst_search_'+ target_colour + target_shape +'.png', units="pix")
                    img.size = img.size*0.4
                    
                    
                inst_text.pos = (0,-mywin.size[1]/10)
        
                pn, pp = drawBoxes(.1,-.6)
                
                img.pos = (0, mywin.size[1]/13)
        
                rect_outline = visual.Rect(mywin,
                lineWidth=30,
                units = 'pix',
                colorSpace='rgb',
                lineColor=[-1, -1, -1],
                size= img.size,
                pos = img.pos,
                fillColor=None,
                opacity=None,
                interpolate=False
                )
                
                img.draw()
                rect_outline.draw()
            
            elif i == 4:
                inst_text = visual.TextStim(mywin, 'Please try to be as fast and accurate as possible throughout the experiment!', units = "pix")
                pn, pp = drawBoxes(.1,-.2)

            elif i == 5: 
                inst_text = visual.TextStim(mywin, 'We will now begin with a brief practice run so you can get acquainted with the task. Press Next to start the practice run!', units = "pix")
                pn, pp = drawBoxes(.1,-.2)

            inst_text.color = 'black'
            inst_text.height = 20
            inst_text.draw()

            mywin.flip()





if __name__ == '__main__':
        instructionScreensPictures(mywin)