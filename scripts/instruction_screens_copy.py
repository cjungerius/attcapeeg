from psychopy import visual, event
from display_functions import *
import os

# if images used than this 
path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir = dir.replace('scripts', 'media')
os.chdir(dir)

def drawBoxesWelcome(): 
    polygon_next = visual.Rect(mywin, width = 0.14, height = 0.1, pos = (.1,-.2), ori=0,
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, interpolate=True)
    
    polygon_prev = visual.Rect(mywin, width = 0.18, height = 0.1, pos = (-.1,-.2), ori=0,
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, interpolate=True)
    
    next_text = visual.TextStim(mywin,
    text='Next >',
    font='Arial',
    pos=(.1,-.2), height=0.06, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1)
    
    prev_text = visual.TextStim(mywin,
    text='< Previous',
    font='Arial',
    pos=(-.1,-.2), height=0.06, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1)
    
    return polygon_next, polygon_prev, next_text, prev_text

def drawBoxesScreens(): 
    polygon_next = visual.Rect(mywin, width = 0.14, height = 0.1, pos = (.1,-.6), ori=0,
    lineWidth=3, lineColor=[0.6549, 0.6549, 0.6549], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, interpolate=True)
    
    polygon_prev = visual.Rect(mywin, width = 0.18, height = 0.1, pos = (-.1,-.6), ori=0,
    lineWidth=3, lineColor=[0.6549, 0.6549, 0.6549], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, interpolate=True)
    
    next_text = visual.TextStim(mywin,
    text='Next >',
    font='Arial',
    pos=(.1,-.6), height=0.06, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1)
    
    prev_text = visual.TextStim(mywin,
    text='< Previous',
    font='Arial',
    pos=(-.1,-.6), height=0.06, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1)
    
    return polygon_next, polygon_prev, next_text, prev_text


def instructionScreensPictures(mywin, target_shape = 'c', target_colour = 'r'): 
    i = 0 # initate start val
    mouse = event.Mouse(win=mywin)

    pn, pp, nt, pt = drawBoxesWelcome()
    inst_text = visual.TextStim(mywin, 'Welcome to the experiment! We will instruct you to the task you will preform'
                                    , units = "pix")
    pn.draw()
    pp.draw()
    nt.draw()
    pt.draw()

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
                    inst_text = visual.TextStim(mywin, text = 'Your task is to search for the               , then react to the line segment inside it. If the line segment points to the left, press the left arrow key; if the line segment points to the right, press the right arrow key.', units="pix")
                    img = visual.ImageStim(mywin, image='inst_search_'+ target_colour + target_shape +'.png', units="pix")
                    img.size = img.size*0.4
                    
                    # if we want to make this work I need to know the exact screen size of our expi otherwise cannot make it bold 
                    if target_shape == 'd':
                        g_text = visual.TextStim(mywin, text = 'diamond', units = "pix", bold = True)
                    
                    if target_shape == 'c':
                        g_text = visual.TextStim(mywin, text = 'circle', units = "pix", bold = True)
                        
                    g_text.pos = (0+mywin.size[0]/37,-mywin.size[1]/13)
                    g_text.color = 'black'
                    g_text.height = 20
                    
                inst_text.pos = (0,-mywin.size[1]/10)
        
                pn, pp, nt, pt = drawBoxesScreens()
                
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
                pn, pp, nt, pt = drawBoxesWelcome()

            elif i == 5: 
                inst_text = visual.TextStim(mywin, 'We will now begin with a brief practice run so you can get acquainted with the task. Press Next to start the practice run!', units = "pix")
                pn, pp, nt, pt = drawBoxesWelcome()

            inst_text.color = 'black'
            inst_text.height = 20
            inst_text.draw()
            if i == 3: # needs to be here bc first the text with the space needs to be drawn where then the bold text of the starget shape can be drawn onto
                g_text.draw()
            
            pn.draw()
            pp.draw()
            nt.draw()
            pt.draw()
            mywin.flip()





if __name__ == '__main__':
        instructionScreensPictures(mywin)