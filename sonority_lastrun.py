#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on July 10, 2020, at 00:23
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
stimulitrain1 = sound.Sound('A', secs=1, stereo=True, hamming=True,
    name='stimulitrain1')
stimulitrain1.setVolume(1)
imagetrain1 = visual.ImageStim(
    win=win,
    name='imagetrain1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "trainquestions1"
trainquestions1Clock = core.Clock()
stimulitest1 = sound.Sound('A', secs=1, stereo=True, hamming=True,
    name='stimulitest1')
stimulitest1.setVolume(1)
correct = visual.ImageStim(
    win=win,
    name='correct', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
incorrect = visual.ImageStim(
    win=win,
    name='incorrect', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
train1TestAnswer = keyboard.Keyboard()

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
notice = visual.TextStim(win=win, name='notice',
    text='Next part will automaticall start in 3 minutes.\n\nPress any button to start',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "train2"
train2Clock = core.Clock()
stimulitrain2 = sound.Sound('A', secs=1, stereo=True, hamming=True,
    name='stimulitrain2')
stimulitrain2.setVolume(1)
imagetrain2 = visual.ImageStim(
    win=win,
    name='imagetrain2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "trainquestions2"
trainquestions2Clock = core.Clock()
stimulitest2 = sound.Sound('A', secs=1, stereo=True, hamming=True,
    name='stimulitest2')
stimulitest2.setVolume(1)
key_resp = keyboard.Keyboard()
correct2 = visual.ImageStim(
    win=win,
    name='correct2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
incorrect2 = visual.ImageStim(
    win=win,
    name='incorrect2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "testTrainInstr"
testTrainInstrClock = core.Clock()
test1Instr = visual.TextStim(win=win, name='test1Instr',
    text='Instructions For Test1 Go Here',
    font='Arial',
    pos=(0, 0.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
skipTest1Instr = keyboard.Keyboard()
oneWarningTest1 = visual.TextStim(win=win, name='oneWarningTest1',
    text='Less than 1 minute left',
    font='Arial',
    pos=(0, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
twoWarningTest1 = visual.TextStim(win=win, name='twoWarningTest1',
    text='Less than 2 minutes left',
    font='Arial',
    pos=(0, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "test1"
test1Clock = core.Clock()
test1AudioFirst = sound.Sound('A', secs=1, stereo=True, hamming=True,
    name='test1AudioFirst')
test1AudioFirst.setVolume(1)
test1AudioSecond = sound.Sound('A', secs=1, stereo=True, hamming=True,
    name='test1AudioSecond')
test1AudioSecond.setVolume(1)
test1Image = visual.ImageStim(
    win=win,
    name='test1Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
test1Response = keyboard.Keyboard()

# Initialize components for Routine "testNovel1Instr"
testNovel1InstrClock = core.Clock()
test2Instr = visual.TextStim(win=win, name='test2Instr',
    text='Instructions For Test2 Go Here',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
skipTest2Instr = keyboard.Keyboard()

# Initialize components for Routine "test2"
test2Clock = core.Clock()
test2AudioFirst = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='test2AudioFirst')
test2AudioFirst.setVolume(1)
test2AudioSecond = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='test2AudioSecond')
test2AudioSecond.setVolume(1)
test2Image = visual.ImageStim(
    win=win,
    name='test2Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
test2Response = keyboard.Keyboard()

# Initialize components for Routine "testNovel2Instr"
testNovel2InstrClock = core.Clock()
test3Instr = visual.TextStim(win=win, name='test3Instr',
    text='Instructions For Test3 Go Here\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
skipTest3Instr = keyboard.Keyboard()

# Initialize components for Routine "test3"
test3Clock = core.Clock()
test3AudioFirst = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='test3AudioFirst')
test3AudioFirst.setVolume(1)
test3AudioSecond = sound.Sound('A', secs=1, stereo=True, hamming=True,
    name='test3AudioSecond')
test3AudioSecond.setVolume(1)
test3Image = visual.ImageStim(
    win=win,
    name='test3Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
test3Response = keyboard.Keyboard()

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
train1blocks = data.TrialHandler(nReps=0, method='sequential', 
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
    blockwords1 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condFiles),
        seed=None, name='blockwords1')
    thisExp.addLoop(blockwords1)  # add the loop to the experiment
    thisBlockwords1 = blockwords1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockwords1.rgb)
    if thisBlockwords1 != None:
        for paramName in thisBlockwords1:
            exec('{} = thisBlockwords1[paramName]'.format(paramName))
    
    for thisBlockwords1 in blockwords1:
        currentLoop = blockwords1
        # abbreviate parameter names if possible (e.g. rgb = thisBlockwords1.rgb)
        if thisBlockwords1 != None:
            for paramName in thisBlockwords1:
                exec('{} = thisBlockwords1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "train1"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        stimulitrain1.setSound(audio, secs=1, hamming=True)
        stimulitrain1.setVolume(1, log=False)
        imagetrain1.setImage(imageLoc)
        # keep track of which components have finished
        train1Components = [stimulitrain1, imagetrain1]
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
            # start/stop stimulitrain1
            if stimulitrain1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                stimulitrain1.frameNStart = frameN  # exact frame index
                stimulitrain1.tStart = t  # local t and not account for scr refresh
                stimulitrain1.tStartRefresh = tThisFlipGlobal  # on global time
                stimulitrain1.play(when=win)  # sync with win flip
            if stimulitrain1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimulitrain1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    stimulitrain1.tStop = t  # not accounting for scr refresh
                    stimulitrain1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stimulitrain1, 'tStopRefresh')  # time at next scr refresh
                    stimulitrain1.stop()
            
            # *imagetrain1* updates
            if imagetrain1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                imagetrain1.frameNStart = frameN  # exact frame index
                imagetrain1.tStart = t  # local t and not account for scr refresh
                imagetrain1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imagetrain1, 'tStartRefresh')  # time at next scr refresh
                imagetrain1.setAutoDraw(True)
            if imagetrain1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > imagetrain1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    imagetrain1.tStop = t  # not accounting for scr refresh
                    imagetrain1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(imagetrain1, 'tStopRefresh')  # time at next scr refresh
                    imagetrain1.setAutoDraw(False)
            
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
        stimulitrain1.stop()  # ensure sound has stopped at end of routine
        blockwords1.addData('stimulitrain1.started', stimulitrain1.tStartRefresh)
        blockwords1.addData('stimulitrain1.stopped', stimulitrain1.tStopRefresh)
        blockwords1.addData('imagetrain1.started', imagetrain1.tStartRefresh)
        blockwords1.addData('imagetrain1.stopped', imagetrain1.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'blockwords1'
    
    
    # set up handler to look after randomisation of conditions etc
    blocktest1 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(testFiles),
        seed=None, name='blocktest1')
    thisExp.addLoop(blocktest1)  # add the loop to the experiment
    thisBlocktest1 = blocktest1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlocktest1.rgb)
    if thisBlocktest1 != None:
        for paramName in thisBlocktest1:
            exec('{} = thisBlocktest1[paramName]'.format(paramName))
    
    for thisBlocktest1 in blocktest1:
        currentLoop = blocktest1
        # abbreviate parameter names if possible (e.g. rgb = thisBlocktest1.rgb)
        if thisBlocktest1 != None:
            for paramName in thisBlocktest1:
                exec('{} = thisBlocktest1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trainquestions1"-------
        continueRoutine = True
        routineTimer.add(7.000000)
        # update component parameters for each repeat
        stimulitest1.setSound(audioTrue, secs=1, hamming=True)
        stimulitest1.setVolume(1, log=False)
        correct.setPos((truePos,0))
        correct.setImage(imageTrue)
        incorrect.setPos((falsePos,0))
        incorrect.setImage(imageFalse)
        train1TestAnswer.keys = []
        train1TestAnswer.rt = []
        _train1TestAnswer_allKeys = []
        # keep track of which components have finished
        trainquestions1Components = [stimulitest1, correct, incorrect, train1TestAnswer]
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
            # start/stop stimulitest1
            if stimulitest1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                stimulitest1.frameNStart = frameN  # exact frame index
                stimulitest1.tStart = t  # local t and not account for scr refresh
                stimulitest1.tStartRefresh = tThisFlipGlobal  # on global time
                stimulitest1.play(when=win)  # sync with win flip
            if stimulitest1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimulitest1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    stimulitest1.tStop = t  # not accounting for scr refresh
                    stimulitest1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stimulitest1, 'tStopRefresh')  # time at next scr refresh
                    stimulitest1.stop()
            
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
            
            # *train1TestAnswer* updates
            waitOnFlip = False
            if train1TestAnswer.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                train1TestAnswer.frameNStart = frameN  # exact frame index
                train1TestAnswer.tStart = t  # local t and not account for scr refresh
                train1TestAnswer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(train1TestAnswer, 'tStartRefresh')  # time at next scr refresh
                train1TestAnswer.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(train1TestAnswer.clock.reset)  # t=0 on next screen flip
            if train1TestAnswer.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > train1TestAnswer.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    train1TestAnswer.tStop = t  # not accounting for scr refresh
                    train1TestAnswer.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(train1TestAnswer, 'tStopRefresh')  # time at next scr refresh
                    train1TestAnswer.status = FINISHED
            if train1TestAnswer.status == STARTED and not waitOnFlip:
                theseKeys = train1TestAnswer.getKeys(keyList=['f', 'j'], waitRelease=False)
                _train1TestAnswer_allKeys.extend(theseKeys)
                if len(_train1TestAnswer_allKeys):
                    train1TestAnswer.keys = _train1TestAnswer_allKeys[-1].name  # just the last key pressed
                    train1TestAnswer.rt = _train1TestAnswer_allKeys[-1].rt
                    # a response ends the routine
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
        stimulitest1.stop()  # ensure sound has stopped at end of routine
        blocktest1.addData('stimulitest1.started', stimulitest1.tStartRefresh)
        blocktest1.addData('stimulitest1.stopped', stimulitest1.tStopRefresh)
        blocktest1.addData('correct.started', correct.tStartRefresh)
        blocktest1.addData('correct.stopped', correct.tStopRefresh)
        blocktest1.addData('incorrect.started', incorrect.tStartRefresh)
        blocktest1.addData('incorrect.stopped', incorrect.tStopRefresh)
        # check responses
        if train1TestAnswer.keys in ['', [], None]:  # No response was made
            train1TestAnswer.keys = None
        blocktest1.addData('train1TestAnswer.keys',train1TestAnswer.keys)
        if train1TestAnswer.keys != None:  # we had a response
            blocktest1.addData('train1TestAnswer.rt', train1TestAnswer.rt)
        blocktest1.addData('train1TestAnswer.started', train1TestAnswer.tStartRefresh)
        blocktest1.addData('train1TestAnswer.stopped', train1TestAnswer.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'blocktest1'
    
    thisExp.nextEntry()
    
# completed 0 repeats of 'train1blocks'


# ------Prepare to start Routine "instr2"-------
continueRoutine = True
routineTimer.add(600.000000)
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instr2Components = [notice, key_resp_3]
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
        if tThisFlipGlobal > notice.tStartRefresh + 600-frameTolerance:
            # keep track of stop time/frame for later
            notice.tStop = t  # not accounting for scr refresh
            notice.frameNStop = frameN  # exact frame index
            win.timeOnFlip(notice, 'tStopRefresh')  # time at next scr refresh
            notice.setAutoDraw(False)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_3.tStartRefresh + 600-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_3.tStop = t  # not accounting for scr refresh
            key_resp_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_3, 'tStopRefresh')  # time at next scr refresh
            key_resp_3.status = FINISHED
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=None, waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()

# set up handler to look after randomisation of conditions etc
train2blocks = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('autoConditions\\train2LoopCondition.xlsx'),
    seed=None, name='train2blocks')
thisExp.addLoop(train2blocks)  # add the loop to the experiment
thisTrain2block = train2blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrain2block.rgb)
if thisTrain2block != None:
    for paramName in thisTrain2block:
        exec('{} = thisTrain2block[paramName]'.format(paramName))

for thisTrain2block in train2blocks:
    currentLoop = train2blocks
    # abbreviate parameter names if possible (e.g. rgb = thisTrain2block.rgb)
    if thisTrain2block != None:
        for paramName in thisTrain2block:
            exec('{} = thisTrain2block[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    blockloop2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condFiles),
        seed=None, name='blockloop2')
    thisExp.addLoop(blockloop2)  # add the loop to the experiment
    thisBlockloop2 = blockloop2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockloop2.rgb)
    if thisBlockloop2 != None:
        for paramName in thisBlockloop2:
            exec('{} = thisBlockloop2[paramName]'.format(paramName))
    
    for thisBlockloop2 in blockloop2:
        currentLoop = blockloop2
        # abbreviate parameter names if possible (e.g. rgb = thisBlockloop2.rgb)
        if thisBlockloop2 != None:
            for paramName in thisBlockloop2:
                exec('{} = thisBlockloop2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "train2"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        stimulitrain2.setSound(audio, secs=1, hamming=True)
        stimulitrain2.setVolume(1, log=False)
        imagetrain2.setImage(imageLoc)
        # keep track of which components have finished
        train2Components = [stimulitrain2, imagetrain2]
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
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = train2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=train2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop stimulitrain2
            if stimulitrain2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stimulitrain2.frameNStart = frameN  # exact frame index
                stimulitrain2.tStart = t  # local t and not account for scr refresh
                stimulitrain2.tStartRefresh = tThisFlipGlobal  # on global time
                stimulitrain2.play(when=win)  # sync with win flip
            if stimulitrain2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimulitrain2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    stimulitrain2.tStop = t  # not accounting for scr refresh
                    stimulitrain2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stimulitrain2, 'tStopRefresh')  # time at next scr refresh
                    stimulitrain2.stop()
            
            # *imagetrain2* updates
            if imagetrain2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                imagetrain2.frameNStart = frameN  # exact frame index
                imagetrain2.tStart = t  # local t and not account for scr refresh
                imagetrain2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imagetrain2, 'tStartRefresh')  # time at next scr refresh
                imagetrain2.setAutoDraw(True)
            if imagetrain2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > imagetrain2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    imagetrain2.tStop = t  # not accounting for scr refresh
                    imagetrain2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(imagetrain2, 'tStopRefresh')  # time at next scr refresh
                    imagetrain2.setAutoDraw(False)
            
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
        stimulitrain2.stop()  # ensure sound has stopped at end of routine
        blockloop2.addData('stimulitrain2.started', stimulitrain2.tStartRefresh)
        blockloop2.addData('stimulitrain2.stopped', stimulitrain2.tStopRefresh)
        blockloop2.addData('imagetrain2.started', imagetrain2.tStartRefresh)
        blockloop2.addData('imagetrain2.stopped', imagetrain2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'blockloop2'
    
    
    # set up handler to look after randomisation of conditions etc
    blocktest2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(testFiles),
        seed=None, name='blocktest2')
    thisExp.addLoop(blocktest2)  # add the loop to the experiment
    thisBlocktest2 = blocktest2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlocktest2.rgb)
    if thisBlocktest2 != None:
        for paramName in thisBlocktest2:
            exec('{} = thisBlocktest2[paramName]'.format(paramName))
    
    for thisBlocktest2 in blocktest2:
        currentLoop = blocktest2
        # abbreviate parameter names if possible (e.g. rgb = thisBlocktest2.rgb)
        if thisBlocktest2 != None:
            for paramName in thisBlocktest2:
                exec('{} = thisBlocktest2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trainquestions2"-------
        continueRoutine = True
        routineTimer.add(7.000000)
        # update component parameters for each repeat
        stimulitest2.setSound(audioTrue, secs=1, hamming=True)
        stimulitest2.setVolume(1, log=False)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        correct2.setPos((truePos, 0))
        correct2.setImage(imageTrue)
        incorrect2.setPos((falsePos, 0))
        incorrect2.setImage(imageFalse)
        # keep track of which components have finished
        trainquestions2Components = [stimulitest2, key_resp, correct2, incorrect2]
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
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trainquestions2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trainquestions2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop stimulitest2
            if stimulitest2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stimulitest2.frameNStart = frameN  # exact frame index
                stimulitest2.tStart = t  # local t and not account for scr refresh
                stimulitest2.tStartRefresh = tThisFlipGlobal  # on global time
                stimulitest2.play(when=win)  # sync with win flip
            if stimulitest2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimulitest2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    stimulitest2.tStop = t  # not accounting for scr refresh
                    stimulitest2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stimulitest2, 'tStopRefresh')  # time at next scr refresh
                    stimulitest2.stop()
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *correct2* updates
            if correct2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                correct2.frameNStart = frameN  # exact frame index
                correct2.tStart = t  # local t and not account for scr refresh
                correct2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(correct2, 'tStartRefresh')  # time at next scr refresh
                correct2.setAutoDraw(True)
            if correct2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > correct2.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    correct2.tStop = t  # not accounting for scr refresh
                    correct2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(correct2, 'tStopRefresh')  # time at next scr refresh
                    correct2.setAutoDraw(False)
            
            # *incorrect2* updates
            if incorrect2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                incorrect2.frameNStart = frameN  # exact frame index
                incorrect2.tStart = t  # local t and not account for scr refresh
                incorrect2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(incorrect2, 'tStartRefresh')  # time at next scr refresh
                incorrect2.setAutoDraw(True)
            if incorrect2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > incorrect2.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    incorrect2.tStop = t  # not accounting for scr refresh
                    incorrect2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(incorrect2, 'tStopRefresh')  # time at next scr refresh
                    incorrect2.setAutoDraw(False)
            
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
        stimulitest2.stop()  # ensure sound has stopped at end of routine
        blocktest2.addData('stimulitest2.started', stimulitest2.tStartRefresh)
        blocktest2.addData('stimulitest2.stopped', stimulitest2.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        blocktest2.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            blocktest2.addData('key_resp.rt', key_resp.rt)
        blocktest2.addData('key_resp.started', key_resp.tStartRefresh)
        blocktest2.addData('key_resp.stopped', key_resp.tStopRefresh)
        blocktest2.addData('correct2.started', correct2.tStartRefresh)
        blocktest2.addData('correct2.stopped', correct2.tStopRefresh)
        blocktest2.addData('incorrect2.started', incorrect2.tStartRefresh)
        blocktest2.addData('incorrect2.stopped', incorrect2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'blocktest2'
    
    thisExp.nextEntry()
    
# completed 0 repeats of 'train2blocks'


# ------Prepare to start Routine "testTrainInstr"-------
continueRoutine = True
routineTimer.add(600.000000)
# update component parameters for each repeat
skipTest1Instr.keys = []
skipTest1Instr.rt = []
_skipTest1Instr_allKeys = []
# keep track of which components have finished
testTrainInstrComponents = [test1Instr, skipTest1Instr, oneWarningTest1, twoWarningTest1]
for thisComponent in testTrainInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testTrainInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testTrainInstr"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = testTrainInstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testTrainInstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test1Instr* updates
    if test1Instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test1Instr.frameNStart = frameN  # exact frame index
        test1Instr.tStart = t  # local t and not account for scr refresh
        test1Instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test1Instr, 'tStartRefresh')  # time at next scr refresh
        test1Instr.setAutoDraw(True)
    if test1Instr.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test1Instr.tStartRefresh + 600-frameTolerance:
            # keep track of stop time/frame for later
            test1Instr.tStop = t  # not accounting for scr refresh
            test1Instr.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test1Instr, 'tStopRefresh')  # time at next scr refresh
            test1Instr.setAutoDraw(False)
    
    # *skipTest1Instr* updates
    waitOnFlip = False
    if skipTest1Instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skipTest1Instr.frameNStart = frameN  # exact frame index
        skipTest1Instr.tStart = t  # local t and not account for scr refresh
        skipTest1Instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skipTest1Instr, 'tStartRefresh')  # time at next scr refresh
        skipTest1Instr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skipTest1Instr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skipTest1Instr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skipTest1Instr.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > skipTest1Instr.tStartRefresh + 600-frameTolerance:
            # keep track of stop time/frame for later
            skipTest1Instr.tStop = t  # not accounting for scr refresh
            skipTest1Instr.frameNStop = frameN  # exact frame index
            win.timeOnFlip(skipTest1Instr, 'tStopRefresh')  # time at next scr refresh
            skipTest1Instr.status = FINISHED
    if skipTest1Instr.status == STARTED and not waitOnFlip:
        theseKeys = skipTest1Instr.getKeys(keyList=None, waitRelease=False)
        _skipTest1Instr_allKeys.extend(theseKeys)
        if len(_skipTest1Instr_allKeys):
            skipTest1Instr.keys = _skipTest1Instr_allKeys[-1].name  # just the last key pressed
            skipTest1Instr.rt = _skipTest1Instr_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *oneWarningTest1* updates
    if oneWarningTest1.status == NOT_STARTED and tThisFlip >= 540-frameTolerance:
        # keep track of start time/frame for later
        oneWarningTest1.frameNStart = frameN  # exact frame index
        oneWarningTest1.tStart = t  # local t and not account for scr refresh
        oneWarningTest1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(oneWarningTest1, 'tStartRefresh')  # time at next scr refresh
        oneWarningTest1.setAutoDraw(True)
    if oneWarningTest1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > oneWarningTest1.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            oneWarningTest1.tStop = t  # not accounting for scr refresh
            oneWarningTest1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(oneWarningTest1, 'tStopRefresh')  # time at next scr refresh
            oneWarningTest1.setAutoDraw(False)
    
    # *twoWarningTest1* updates
    if twoWarningTest1.status == NOT_STARTED and tThisFlip >= 480-frameTolerance:
        # keep track of start time/frame for later
        twoWarningTest1.frameNStart = frameN  # exact frame index
        twoWarningTest1.tStart = t  # local t and not account for scr refresh
        twoWarningTest1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(twoWarningTest1, 'tStartRefresh')  # time at next scr refresh
        twoWarningTest1.setAutoDraw(True)
    if twoWarningTest1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > twoWarningTest1.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            twoWarningTest1.tStop = t  # not accounting for scr refresh
            twoWarningTest1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(twoWarningTest1, 'tStopRefresh')  # time at next scr refresh
            twoWarningTest1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testTrainInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testTrainInstr"-------
for thisComponent in testTrainInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('test1Instr.started', test1Instr.tStartRefresh)
thisExp.addData('test1Instr.stopped', test1Instr.tStopRefresh)
# check responses
if skipTest1Instr.keys in ['', [], None]:  # No response was made
    skipTest1Instr.keys = None
thisExp.addData('skipTest1Instr.keys',skipTest1Instr.keys)
if skipTest1Instr.keys != None:  # we had a response
    thisExp.addData('skipTest1Instr.rt', skipTest1Instr.rt)
thisExp.addData('skipTest1Instr.started', skipTest1Instr.tStartRefresh)
thisExp.addData('skipTest1Instr.stopped', skipTest1Instr.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('oneWarningTest1.started', oneWarningTest1.tStartRefresh)
thisExp.addData('oneWarningTest1.stopped', oneWarningTest1.tStopRefresh)
thisExp.addData('twoWarningTest1.started', twoWarningTest1.tStartRefresh)
thisExp.addData('twoWarningTest1.stopped', twoWarningTest1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
test1Loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('autoConditions\\test1Conditions.xlsx'),
    seed=None, name='test1Loop')
thisExp.addLoop(test1Loop)  # add the loop to the experiment
thisTest1Loop = test1Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest1Loop.rgb)
if thisTest1Loop != None:
    for paramName in thisTest1Loop:
        exec('{} = thisTest1Loop[paramName]'.format(paramName))

for thisTest1Loop in test1Loop:
    currentLoop = test1Loop
    # abbreviate parameter names if possible (e.g. rgb = thisTest1Loop.rgb)
    if thisTest1Loop != None:
        for paramName in thisTest1Loop:
            exec('{} = thisTest1Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "test1"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    test1AudioFirst.setSound(firstAudio, secs=1, hamming=True)
    test1AudioFirst.setVolume(1, log=False)
    test1AudioSecond.setSound(secondAudio, secs=1, hamming=True)
    test1AudioSecond.setVolume(1, log=False)
    test1Image.setImage(imageLoc)
    test1Response.keys = []
    test1Response.rt = []
    _test1Response_allKeys = []
    # keep track of which components have finished
    test1Components = [test1AudioFirst, test1AudioSecond, test1Image, test1Response]
    for thisComponent in test1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    test1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "test1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=test1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop test1AudioFirst
        if test1AudioFirst.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            test1AudioFirst.frameNStart = frameN  # exact frame index
            test1AudioFirst.tStart = t  # local t and not account for scr refresh
            test1AudioFirst.tStartRefresh = tThisFlipGlobal  # on global time
            test1AudioFirst.play(when=win)  # sync with win flip
        if test1AudioFirst.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test1AudioFirst.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                test1AudioFirst.tStop = t  # not accounting for scr refresh
                test1AudioFirst.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test1AudioFirst, 'tStopRefresh')  # time at next scr refresh
                test1AudioFirst.stop()
        # start/stop test1AudioSecond
        if test1AudioSecond.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            test1AudioSecond.frameNStart = frameN  # exact frame index
            test1AudioSecond.tStart = t  # local t and not account for scr refresh
            test1AudioSecond.tStartRefresh = tThisFlipGlobal  # on global time
            test1AudioSecond.play(when=win)  # sync with win flip
        if test1AudioSecond.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test1AudioSecond.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                test1AudioSecond.tStop = t  # not accounting for scr refresh
                test1AudioSecond.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test1AudioSecond, 'tStopRefresh')  # time at next scr refresh
                test1AudioSecond.stop()
        
        # *test1Image* updates
        if test1Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test1Image.frameNStart = frameN  # exact frame index
            test1Image.tStart = t  # local t and not account for scr refresh
            test1Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test1Image, 'tStartRefresh')  # time at next scr refresh
            test1Image.setAutoDraw(True)
        if test1Image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test1Image.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                test1Image.tStop = t  # not accounting for scr refresh
                test1Image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test1Image, 'tStopRefresh')  # time at next scr refresh
                test1Image.setAutoDraw(False)
        
        # *test1Response* updates
        waitOnFlip = False
        if test1Response.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            test1Response.frameNStart = frameN  # exact frame index
            test1Response.tStart = t  # local t and not account for scr refresh
            test1Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test1Response, 'tStartRefresh')  # time at next scr refresh
            test1Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(test1Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(test1Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if test1Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test1Response.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                test1Response.tStop = t  # not accounting for scr refresh
                test1Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test1Response, 'tStopRefresh')  # time at next scr refresh
                test1Response.status = FINISHED
        if test1Response.status == STARTED and not waitOnFlip:
            theseKeys = test1Response.getKeys(keyList=['f', 'j'], waitRelease=False)
            _test1Response_allKeys.extend(theseKeys)
            if len(_test1Response_allKeys):
                test1Response.keys = _test1Response_allKeys[-1].name  # just the last key pressed
                test1Response.rt = _test1Response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test1"-------
    for thisComponent in test1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    test1AudioFirst.stop()  # ensure sound has stopped at end of routine
    test1Loop.addData('test1AudioFirst.started', test1AudioFirst.tStartRefresh)
    test1Loop.addData('test1AudioFirst.stopped', test1AudioFirst.tStopRefresh)
    test1AudioSecond.stop()  # ensure sound has stopped at end of routine
    test1Loop.addData('test1AudioSecond.started', test1AudioSecond.tStartRefresh)
    test1Loop.addData('test1AudioSecond.stopped', test1AudioSecond.tStopRefresh)
    test1Loop.addData('test1Image.started', test1Image.tStartRefresh)
    test1Loop.addData('test1Image.stopped', test1Image.tStopRefresh)
    # check responses
    if test1Response.keys in ['', [], None]:  # No response was made
        test1Response.keys = None
    test1Loop.addData('test1Response.keys',test1Response.keys)
    if test1Response.keys != None:  # we had a response
        test1Loop.addData('test1Response.rt', test1Response.rt)
    test1Loop.addData('test1Response.started', test1Response.tStartRefresh)
    test1Loop.addData('test1Response.stopped', test1Response.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'test1Loop'


# ------Prepare to start Routine "testNovel1Instr"-------
continueRoutine = True
routineTimer.add(600.000000)
# update component parameters for each repeat
skipTest2Instr.keys = []
skipTest2Instr.rt = []
_skipTest2Instr_allKeys = []
# keep track of which components have finished
testNovel1InstrComponents = [test2Instr, skipTest2Instr]
for thisComponent in testNovel1InstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testNovel1InstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testNovel1Instr"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = testNovel1InstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testNovel1InstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test2Instr* updates
    if test2Instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test2Instr.frameNStart = frameN  # exact frame index
        test2Instr.tStart = t  # local t and not account for scr refresh
        test2Instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test2Instr, 'tStartRefresh')  # time at next scr refresh
        test2Instr.setAutoDraw(True)
    if test2Instr.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test2Instr.tStartRefresh + 600-frameTolerance:
            # keep track of stop time/frame for later
            test2Instr.tStop = t  # not accounting for scr refresh
            test2Instr.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test2Instr, 'tStopRefresh')  # time at next scr refresh
            test2Instr.setAutoDraw(False)
    
    # *skipTest2Instr* updates
    waitOnFlip = False
    if skipTest2Instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skipTest2Instr.frameNStart = frameN  # exact frame index
        skipTest2Instr.tStart = t  # local t and not account for scr refresh
        skipTest2Instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skipTest2Instr, 'tStartRefresh')  # time at next scr refresh
        skipTest2Instr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skipTest2Instr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skipTest2Instr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skipTest2Instr.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > skipTest2Instr.tStartRefresh + 600-frameTolerance:
            # keep track of stop time/frame for later
            skipTest2Instr.tStop = t  # not accounting for scr refresh
            skipTest2Instr.frameNStop = frameN  # exact frame index
            win.timeOnFlip(skipTest2Instr, 'tStopRefresh')  # time at next scr refresh
            skipTest2Instr.status = FINISHED
    if skipTest2Instr.status == STARTED and not waitOnFlip:
        theseKeys = skipTest2Instr.getKeys(keyList=None, waitRelease=False)
        _skipTest2Instr_allKeys.extend(theseKeys)
        if len(_skipTest2Instr_allKeys):
            skipTest2Instr.keys = _skipTest2Instr_allKeys[-1].name  # just the last key pressed
            skipTest2Instr.rt = _skipTest2Instr_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testNovel1InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testNovel1Instr"-------
for thisComponent in testNovel1InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('test2Instr.started', test2Instr.tStartRefresh)
thisExp.addData('test2Instr.stopped', test2Instr.tStopRefresh)
# check responses
if skipTest2Instr.keys in ['', [], None]:  # No response was made
    skipTest2Instr.keys = None
thisExp.addData('skipTest2Instr.keys',skipTest2Instr.keys)
if skipTest2Instr.keys != None:  # we had a response
    thisExp.addData('skipTest2Instr.rt', skipTest2Instr.rt)
thisExp.addData('skipTest2Instr.started', skipTest2Instr.tStartRefresh)
thisExp.addData('skipTest2Instr.stopped', skipTest2Instr.tStopRefresh)
thisExp.nextEntry()

# set up handler to look after randomisation of conditions etc
test2Loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('autoConditions\\test2Conditions.xlsx'),
    seed=None, name='test2Loop')
thisExp.addLoop(test2Loop)  # add the loop to the experiment
thisTest2Loop = test2Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest2Loop.rgb)
if thisTest2Loop != None:
    for paramName in thisTest2Loop:
        exec('{} = thisTest2Loop[paramName]'.format(paramName))

for thisTest2Loop in test2Loop:
    currentLoop = test2Loop
    # abbreviate parameter names if possible (e.g. rgb = thisTest2Loop.rgb)
    if thisTest2Loop != None:
        for paramName in thisTest2Loop:
            exec('{} = thisTest2Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "test2"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    test2AudioFirst.setSound(firstAudio, secs=1.0, hamming=True)
    test2AudioFirst.setVolume(1, log=False)
    test2AudioSecond.setSound(secondAudio, secs=1.0, hamming=True)
    test2AudioSecond.setVolume(1, log=False)
    test2Image.setImage(imageLoc)
    test2Response.keys = []
    test2Response.rt = []
    _test2Response_allKeys = []
    # keep track of which components have finished
    test2Components = [test2AudioFirst, test2AudioSecond, test2Image, test2Response]
    for thisComponent in test2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    test2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "test2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=test2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop test2AudioFirst
        if test2AudioFirst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test2AudioFirst.frameNStart = frameN  # exact frame index
            test2AudioFirst.tStart = t  # local t and not account for scr refresh
            test2AudioFirst.tStartRefresh = tThisFlipGlobal  # on global time
            test2AudioFirst.play(when=win)  # sync with win flip
        if test2AudioFirst.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test2AudioFirst.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                test2AudioFirst.tStop = t  # not accounting for scr refresh
                test2AudioFirst.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test2AudioFirst, 'tStopRefresh')  # time at next scr refresh
                test2AudioFirst.stop()
        # start/stop test2AudioSecond
        if test2AudioSecond.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            test2AudioSecond.frameNStart = frameN  # exact frame index
            test2AudioSecond.tStart = t  # local t and not account for scr refresh
            test2AudioSecond.tStartRefresh = tThisFlipGlobal  # on global time
            test2AudioSecond.play(when=win)  # sync with win flip
        if test2AudioSecond.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test2AudioSecond.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                test2AudioSecond.tStop = t  # not accounting for scr refresh
                test2AudioSecond.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test2AudioSecond, 'tStopRefresh')  # time at next scr refresh
                test2AudioSecond.stop()
        
        # *test2Image* updates
        if test2Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test2Image.frameNStart = frameN  # exact frame index
            test2Image.tStart = t  # local t and not account for scr refresh
            test2Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test2Image, 'tStartRefresh')  # time at next scr refresh
            test2Image.setAutoDraw(True)
        if test2Image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test2Image.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                test2Image.tStop = t  # not accounting for scr refresh
                test2Image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test2Image, 'tStopRefresh')  # time at next scr refresh
                test2Image.setAutoDraw(False)
        
        # *test2Response* updates
        waitOnFlip = False
        if test2Response.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            test2Response.frameNStart = frameN  # exact frame index
            test2Response.tStart = t  # local t and not account for scr refresh
            test2Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test2Response, 'tStartRefresh')  # time at next scr refresh
            test2Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(test2Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(test2Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if test2Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test2Response.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                test2Response.tStop = t  # not accounting for scr refresh
                test2Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test2Response, 'tStopRefresh')  # time at next scr refresh
                test2Response.status = FINISHED
        if test2Response.status == STARTED and not waitOnFlip:
            theseKeys = test2Response.getKeys(keyList=['f', 'j'], waitRelease=False)
            _test2Response_allKeys.extend(theseKeys)
            if len(_test2Response_allKeys):
                test2Response.keys = _test2Response_allKeys[-1].name  # just the last key pressed
                test2Response.rt = _test2Response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test2"-------
    for thisComponent in test2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    test2AudioFirst.stop()  # ensure sound has stopped at end of routine
    test2Loop.addData('test2AudioFirst.started', test2AudioFirst.tStartRefresh)
    test2Loop.addData('test2AudioFirst.stopped', test2AudioFirst.tStopRefresh)
    test2AudioSecond.stop()  # ensure sound has stopped at end of routine
    test2Loop.addData('test2AudioSecond.started', test2AudioSecond.tStartRefresh)
    test2Loop.addData('test2AudioSecond.stopped', test2AudioSecond.tStopRefresh)
    test2Loop.addData('test2Image.started', test2Image.tStartRefresh)
    test2Loop.addData('test2Image.stopped', test2Image.tStopRefresh)
    # check responses
    if test2Response.keys in ['', [], None]:  # No response was made
        test2Response.keys = None
    test2Loop.addData('test2Response.keys',test2Response.keys)
    if test2Response.keys != None:  # we had a response
        test2Loop.addData('test2Response.rt', test2Response.rt)
    test2Loop.addData('test2Response.started', test2Response.tStartRefresh)
    test2Loop.addData('test2Response.stopped', test2Response.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'test2Loop'


# ------Prepare to start Routine "testNovel2Instr"-------
continueRoutine = True
routineTimer.add(600.000000)
# update component parameters for each repeat
skipTest3Instr.keys = []
skipTest3Instr.rt = []
_skipTest3Instr_allKeys = []
# keep track of which components have finished
testNovel2InstrComponents = [test3Instr, skipTest3Instr]
for thisComponent in testNovel2InstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testNovel2InstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testNovel2Instr"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = testNovel2InstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testNovel2InstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test3Instr* updates
    if test3Instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test3Instr.frameNStart = frameN  # exact frame index
        test3Instr.tStart = t  # local t and not account for scr refresh
        test3Instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test3Instr, 'tStartRefresh')  # time at next scr refresh
        test3Instr.setAutoDraw(True)
    if test3Instr.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test3Instr.tStartRefresh + 600-frameTolerance:
            # keep track of stop time/frame for later
            test3Instr.tStop = t  # not accounting for scr refresh
            test3Instr.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test3Instr, 'tStopRefresh')  # time at next scr refresh
            test3Instr.setAutoDraw(False)
    
    # *skipTest3Instr* updates
    waitOnFlip = False
    if skipTest3Instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skipTest3Instr.frameNStart = frameN  # exact frame index
        skipTest3Instr.tStart = t  # local t and not account for scr refresh
        skipTest3Instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skipTest3Instr, 'tStartRefresh')  # time at next scr refresh
        skipTest3Instr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skipTest3Instr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skipTest3Instr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skipTest3Instr.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > skipTest3Instr.tStartRefresh + 600-frameTolerance:
            # keep track of stop time/frame for later
            skipTest3Instr.tStop = t  # not accounting for scr refresh
            skipTest3Instr.frameNStop = frameN  # exact frame index
            win.timeOnFlip(skipTest3Instr, 'tStopRefresh')  # time at next scr refresh
            skipTest3Instr.status = FINISHED
    if skipTest3Instr.status == STARTED and not waitOnFlip:
        theseKeys = skipTest3Instr.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _skipTest3Instr_allKeys.extend(theseKeys)
        if len(_skipTest3Instr_allKeys):
            skipTest3Instr.keys = _skipTest3Instr_allKeys[-1].name  # just the last key pressed
            skipTest3Instr.rt = _skipTest3Instr_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testNovel2InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testNovel2Instr"-------
for thisComponent in testNovel2InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('test3Instr.started', test3Instr.tStartRefresh)
thisExp.addData('test3Instr.stopped', test3Instr.tStopRefresh)
# check responses
if skipTest3Instr.keys in ['', [], None]:  # No response was made
    skipTest3Instr.keys = None
thisExp.addData('skipTest3Instr.keys',skipTest3Instr.keys)
if skipTest3Instr.keys != None:  # we had a response
    thisExp.addData('skipTest3Instr.rt', skipTest3Instr.rt)
thisExp.addData('skipTest3Instr.started', skipTest3Instr.tStartRefresh)
thisExp.addData('skipTest3Instr.stopped', skipTest3Instr.tStopRefresh)
thisExp.nextEntry()

# set up handler to look after randomisation of conditions etc
test3Loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='test3Loop')
thisExp.addLoop(test3Loop)  # add the loop to the experiment
thisTest3Loop = test3Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest3Loop.rgb)
if thisTest3Loop != None:
    for paramName in thisTest3Loop:
        exec('{} = thisTest3Loop[paramName]'.format(paramName))

for thisTest3Loop in test3Loop:
    currentLoop = test3Loop
    # abbreviate parameter names if possible (e.g. rgb = thisTest3Loop.rgb)
    if thisTest3Loop != None:
        for paramName in thisTest3Loop:
            exec('{} = thisTest3Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "test3"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    test3AudioFirst.setSound(firstAudio, secs=1.0, hamming=True)
    test3AudioFirst.setVolume(1, log=False)
    test3AudioSecond.setSound(secondAudio, secs=1, hamming=True)
    test3AudioSecond.setVolume(1, log=False)
    test3Image.setImage(imageLoc)
    test3Response.keys = []
    test3Response.rt = []
    _test3Response_allKeys = []
    # keep track of which components have finished
    test3Components = [test3AudioFirst, test3AudioSecond, test3Image, test3Response]
    for thisComponent in test3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    test3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "test3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=test3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop test3AudioFirst
        if test3AudioFirst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test3AudioFirst.frameNStart = frameN  # exact frame index
            test3AudioFirst.tStart = t  # local t and not account for scr refresh
            test3AudioFirst.tStartRefresh = tThisFlipGlobal  # on global time
            test3AudioFirst.play(when=win)  # sync with win flip
        if test3AudioFirst.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test3AudioFirst.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                test3AudioFirst.tStop = t  # not accounting for scr refresh
                test3AudioFirst.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test3AudioFirst, 'tStopRefresh')  # time at next scr refresh
                test3AudioFirst.stop()
        # start/stop test3AudioSecond
        if test3AudioSecond.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            test3AudioSecond.frameNStart = frameN  # exact frame index
            test3AudioSecond.tStart = t  # local t and not account for scr refresh
            test3AudioSecond.tStartRefresh = tThisFlipGlobal  # on global time
            test3AudioSecond.play(when=win)  # sync with win flip
        if test3AudioSecond.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test3AudioSecond.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                test3AudioSecond.tStop = t  # not accounting for scr refresh
                test3AudioSecond.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test3AudioSecond, 'tStopRefresh')  # time at next scr refresh
                test3AudioSecond.stop()
        
        # *test3Image* updates
        if test3Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test3Image.frameNStart = frameN  # exact frame index
            test3Image.tStart = t  # local t and not account for scr refresh
            test3Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test3Image, 'tStartRefresh')  # time at next scr refresh
            test3Image.setAutoDraw(True)
        if test3Image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test3Image.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                test3Image.tStop = t  # not accounting for scr refresh
                test3Image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test3Image, 'tStopRefresh')  # time at next scr refresh
                test3Image.setAutoDraw(False)
        
        # *test3Response* updates
        waitOnFlip = False
        if test3Response.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            test3Response.frameNStart = frameN  # exact frame index
            test3Response.tStart = t  # local t and not account for scr refresh
            test3Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test3Response, 'tStartRefresh')  # time at next scr refresh
            test3Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(test3Response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(test3Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if test3Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test3Response.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                test3Response.tStop = t  # not accounting for scr refresh
                test3Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test3Response, 'tStopRefresh')  # time at next scr refresh
                test3Response.status = FINISHED
        if test3Response.status == STARTED and not waitOnFlip:
            theseKeys = test3Response.getKeys(keyList=['f', 'j'], waitRelease=False)
            _test3Response_allKeys.extend(theseKeys)
            if len(_test3Response_allKeys):
                test3Response.keys = _test3Response_allKeys[-1].name  # just the last key pressed
                test3Response.rt = _test3Response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test3"-------
    for thisComponent in test3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    test3AudioFirst.stop()  # ensure sound has stopped at end of routine
    test3Loop.addData('test3AudioFirst.started', test3AudioFirst.tStartRefresh)
    test3Loop.addData('test3AudioFirst.stopped', test3AudioFirst.tStopRefresh)
    test3AudioSecond.stop()  # ensure sound has stopped at end of routine
    test3Loop.addData('test3AudioSecond.started', test3AudioSecond.tStartRefresh)
    test3Loop.addData('test3AudioSecond.stopped', test3AudioSecond.tStopRefresh)
    test3Loop.addData('test3Image.started', test3Image.tStartRefresh)
    test3Loop.addData('test3Image.stopped', test3Image.tStopRefresh)
    # check responses
    if test3Response.keys in ['', [], None]:  # No response was made
        test3Response.keys = None
    test3Loop.addData('test3Response.keys',test3Response.keys)
    if test3Response.keys != None:  # we had a response
        test3Loop.addData('test3Response.rt', test3Response.rt)
    test3Loop.addData('test3Response.started', test3Response.tStartRefresh)
    test3Loop.addData('test3Response.stopped', test3Response.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'test3Loop'


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
