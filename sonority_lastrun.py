#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on July 02, 2020, at 23:06
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'sonority'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\ThomasY21\\Dropbox\\Documents\\Prep\\Koehnlein\\experiment\\sonority_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='Welcome and thank you for participating!\n\nInstructions will go here',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instrResp = keyboard.Keyboard()

# Initialize components for Routine "train1"
train1Clock = core.Clock()
stimulitrain1r1 = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='stimulitrain1r1')
stimulitrain1r1.setVolume(1)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "trainquestions1"
trainquestions1Clock = core.Clock()
sound_1 = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1)
correct = visual.ImageStim(
    win=win,
    name='correct', 
    image='sin', mask=None,
    ori=0, pos=(0.5, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
incorrect = visual.ImageStim(
    win=win,
    name='incorrect', 
    image='sin', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
notice = visual.TextStim(win=win, name='notice',
    text='Next part will automaticall start in 3 minutes.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "train2"
train2Clock = core.Clock()

# Initialize components for Routine "trainquestions2"
trainquestions2Clock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
instrResp.keys = []
instrResp.rt = []
_instrResp_allKeys = []
# keep track of which components have finished
instrComponents = [instructions, instrResp]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    
    # *instrResp* updates
    waitOnFlip = False
    if instrResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrResp.frameNStart = frameN  # exact frame index
        instrResp.tStart = t  # local t and not account for scr refresh
        instrResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrResp, 'tStartRefresh')  # time at next scr refresh
        instrResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instrResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instrResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instrResp.status == STARTED and not waitOnFlip:
        theseKeys = instrResp.getKeys(keyList=None, waitRelease=False)
        _instrResp_allKeys.extend(theseKeys)
        if len(_instrResp_allKeys):
            instrResp.keys = _instrResp_allKeys[-1].name  # just the last key pressed
            instrResp.rt = _instrResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
train1blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('autoConditions\\train1LoopCondition.xlsx'),
    seed=None, name='train1blocks')
thisExp.addLoop(train1blocks)  # add the loop to the experiment
thisTrain1block = train1blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrain1block.rgb)
if thisTrain1block != None:
    for paramName in thisTrain1block:
        exec('{} = thisTrain1block[paramName]'.format(paramName))

for thisTrain1block in train1blocks:
    currentLoop = train1blocks
    # abbreviate parameter names if possible (e.g. rgb = thisTrain1block.rgb)
    if thisTrain1block != None:
        for paramName in thisTrain1block:
            exec('{} = thisTrain1block[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    testloop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condFiles),
        seed=None, name='testloop')
    thisExp.addLoop(testloop)  # add the loop to the experiment
    thisTestloop = testloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTestloop.rgb)
    if thisTestloop != None:
        for paramName in thisTestloop:
            exec('{} = thisTestloop[paramName]'.format(paramName))
    
    for thisTestloop in testloop:
        currentLoop = testloop
        # abbreviate parameter names if possible (e.g. rgb = thisTestloop.rgb)
        if thisTestloop != None:
            for paramName in thisTestloop:
                exec('{} = thisTestloop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "train1"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        stimulitrain1r1.setSound(audio, secs=2.0, hamming=True)
        stimulitrain1r1.setVolume(1, log=False)
        image.setImage(imageLoc)
        # keep track of which components have finished
        train1Components = [stimulitrain1r1, image]
        for thisComponent in train1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        train1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "train1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = train1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=train1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop stimulitrain1r1
            if stimulitrain1r1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                stimulitrain1r1.frameNStart = frameN  # exact frame index
                stimulitrain1r1.tStart = t  # local t and not account for scr refresh
                stimulitrain1r1.tStartRefresh = tThisFlipGlobal  # on global time
                stimulitrain1r1.play(when=win)  # sync with win flip
            if stimulitrain1r1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimulitrain1r1.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    stimulitrain1r1.tStop = t  # not accounting for scr refresh
                    stimulitrain1r1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stimulitrain1r1, 'tStopRefresh')  # time at next scr refresh
                    stimulitrain1r1.stop()
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                    image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in train1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "train1"-------
        for thisComponent in train1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        stimulitrain1r1.stop()  # ensure sound has stopped at end of routine
        testloop.addData('stimulitrain1r1.started', stimulitrain1r1.tStartRefresh)
        testloop.addData('stimulitrain1r1.stopped', stimulitrain1r1.tStopRefresh)
        testloop.addData('image.started', image.tStartRefresh)
        testloop.addData('image.stopped', image.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'testloop'
    
    
    # ------Prepare to start Routine "trainquestions1"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    sound_1.setSound(audio, secs=2.0, hamming=True)
    sound_1.setVolume(1, log=False)
    correct.setImage(imageLoc)
    incorrect.setImage(imageLoc)
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trainquestions1Components = [sound_1, correct, incorrect, mouse]
    for thisComponent in trainquestions1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trainquestions1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trainquestions1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trainquestions1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trainquestions1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # *correct* updates
        if correct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            correct.frameNStart = frameN  # exact frame index
            correct.tStart = t  # local t and not account for scr refresh
            correct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct, 'tStartRefresh')  # time at next scr refresh
            correct.setAutoDraw(True)
        if correct.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct.tStartRefresh + 7.0-frameTolerance:
                # keep track of stop time/frame for later
                correct.tStop = t  # not accounting for scr refresh
                correct.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct, 'tStopRefresh')  # time at next scr refresh
                correct.setAutoDraw(False)
        
        # *incorrect* updates
        if incorrect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            incorrect.frameNStart = frameN  # exact frame index
            incorrect.tStart = t  # local t and not account for scr refresh
            incorrect.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(incorrect, 'tStartRefresh')  # time at next scr refresh
            incorrect.setAutoDraw(True)
        if incorrect.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > incorrect.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                incorrect.tStop = t  # not accounting for scr refresh
                incorrect.frameNStop = frameN  # exact frame index
                win.timeOnFlip(incorrect, 'tStopRefresh')  # time at next scr refresh
                incorrect.setAutoDraw(False)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse.tStartRefresh + 7.0-frameTolerance:
                # keep track of stop time/frame for later
                mouse.tStop = t  # not accounting for scr refresh
                mouse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse, 'tStopRefresh')  # time at next scr refresh
                mouse.status = FINISHED
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [correct, incorrect]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trainquestions1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trainquestions1"-------
    for thisComponent in trainquestions1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    train1blocks.addData('sound_1.started', sound_1.tStartRefresh)
    train1blocks.addData('sound_1.stopped', sound_1.tStopRefresh)
    train1blocks.addData('correct.started', correct.tStartRefresh)
    train1blocks.addData('correct.stopped', correct.tStopRefresh)
    train1blocks.addData('incorrect.started', incorrect.tStartRefresh)
    train1blocks.addData('incorrect.stopped', incorrect.tStopRefresh)
    # store data for train1blocks (TrialHandler)
    if len(mouse.x): train1blocks.addData('mouse.x', mouse.x[0])
    if len(mouse.y): train1blocks.addData('mouse.y', mouse.y[0])
    if len(mouse.leftButton): train1blocks.addData('mouse.leftButton', mouse.leftButton[0])
    if len(mouse.midButton): train1blocks.addData('mouse.midButton', mouse.midButton[0])
    if len(mouse.rightButton): train1blocks.addData('mouse.rightButton', mouse.rightButton[0])
    if len(mouse.time): train1blocks.addData('mouse.time', mouse.time[0])
    if len(mouse.clicked_name): train1blocks.addData('mouse.clicked_name', mouse.clicked_name[0])
    train1blocks.addData('mouse.started', mouse.tStart)
    train1blocks.addData('mouse.stopped', mouse.tStop)
    thisExp.nextEntry()
    
# completed 1 repeats of 'train1blocks'


# ------Prepare to start Routine "instr2"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
instr2Components = [notice]
for thisComponent in instr2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instr2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *notice* updates
    if notice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        notice.frameNStart = frameN  # exact frame index
        notice.tStart = t  # local t and not account for scr refresh
        notice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(notice, 'tStartRefresh')  # time at next scr refresh
        notice.setAutoDraw(True)
    if notice.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > notice.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            notice.tStop = t  # not accounting for scr refresh
            notice.frameNStop = frameN  # exact frame index
            win.timeOnFlip(notice, 'tStopRefresh')  # time at next scr refresh
            notice.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr2"-------
for thisComponent in instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('notice.started', notice.tStartRefresh)
thisExp.addData('notice.stopped', notice.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "train2"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    train2Components = []
    for thisComponent in train2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    train2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "train2"-------
    while continueRoutine:
        # get current time
        t = train2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=train2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in train2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "train2"-------
    for thisComponent in train2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "train2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trainquestions2"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    trainquestions2Components = []
    for thisComponent in trainquestions2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trainquestions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trainquestions2"-------
    while continueRoutine:
        # get current time
        t = trainquestions2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trainquestions2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trainquestions2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trainquestions2"-------
    for thisComponent in trainquestions2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "trainquestions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
