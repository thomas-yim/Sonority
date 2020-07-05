#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on July 05, 2020, at 14:55
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
stimulitrain1 = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
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
stimulitest1 = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
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
    text='Next part will automaticall start in 3 minutes.\n\nIn this next segment, you will be presented with 27 words presented in 3 blocks of \n9.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "train2"
train2Clock = core.Clock()
stimulitrain2 = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
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
stimulitest2 = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='stimulitest2')
stimulitest2.setVolume(1)
key_resp = keyboard.Keyboard()
correct2 = visual.ImageStim(
    win=win,
    name='correct2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
incorrect2 = visual.ImageStim(
    win=win,
    name='incorrect2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "testInstr"
testInstrClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='You are now entering the test portion of the experiment.\nSelect the pronunciation that sounds most correct to you.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "test"
testClock = core.Clock()

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
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        stimulitrain1.setSound(audio, secs=0.5, hamming=True)
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
                if tThisFlipGlobal > stimulitrain1.tStartRefresh + 0.5-frameTolerance:
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
                if tThisFlipGlobal > imagetrain1.tStartRefresh + 0.5-frameTolerance:
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
    blocktest1 = data.TrialHandler(nReps=1, method='random', 
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
        stimulitest1.setSound(audio, secs=2.0, hamming=True)
        stimulitest1.setVolume(1, log=False)
        correct.setPos(truePos)
        correct.setImage(imageTrue)
        incorrect.setPos(falsePos)
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
            if stimulitest1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stimulitest1.frameNStart = frameN  # exact frame index
                stimulitest1.tStart = t  # local t and not account for scr refresh
                stimulitest1.tStartRefresh = tThisFlipGlobal  # on global time
                stimulitest1.play(when=win)  # sync with win flip
            if stimulitest1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimulitest1.tStartRefresh + 2.0-frameTolerance:
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
            if train1TestAnswer.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
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
                if tThisFlipGlobal > train1TestAnswer.tStartRefresh + 5.0-frameTolerance:
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
routineTimer.add(2.000000)
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
        if tThisFlipGlobal > notice.tStartRefresh + 2.0-frameTolerance:
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
train2blocks = data.TrialHandler(nReps=1, method='sequential', 
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
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        stimulitrain2.setSound(audio, secs=0.5, hamming=True)
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
                if tThisFlipGlobal > stimulitrain2.tStartRefresh + 0.5-frameTolerance:
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
                if tThisFlipGlobal > imagetrain2.tStartRefresh + 0.5-frameTolerance:
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
        stimulitest2.setSound(audioTrue, secs=2.0, hamming=True)
        stimulitest2.setVolume(1, log=False)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        correct2.setImage(imageTrue)
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
                if tThisFlipGlobal > stimulitest2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    stimulitest2.tStop = t  # not accounting for scr refresh
                    stimulitest2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stimulitest2, 'tStopRefresh')  # time at next scr refresh
                    stimulitest2.stop()
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
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
                if tThisFlipGlobal > key_resp.tStartRefresh + 5.0-frameTolerance:
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
    
# completed 1 repeats of 'train2blocks'


# ------Prepare to start Routine "testInstr"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
testInstrComponents = [text_2]
for thisComponent in testInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testInstr"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = testInstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testInstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstr"-------
for thisComponent in testInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# ------Prepare to start Routine "test"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
testComponents = []
for thisComponent in testComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test"-------
while continueRoutine:
    # get current time
    t = testClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testClock)
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
    for thisComponent in testComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test"-------
for thisComponent in testComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "test" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
