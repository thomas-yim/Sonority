#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on August 06, 2020, at 22:57
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
    originPath='C:\\Users\\ThomasY21\\Dropbox\\Documents\\Prep\\Koehnlein\\experiment\\condition1_lastrun.py',
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
    text='Welcome and thank you for participating!\n\nInstructions will go here.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
advanceTrain1 = keyboard.Keyboard()

# Initialize components for Routine "train1"
train1Clock = core.Clock()
imagetrain1 = visual.ImageStim(
    win=win,
    name='imagetrain1', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
stimuli1train1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='stimuli1train1')
stimuli1train1.setVolume(1)
stimuli2train1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='stimuli2train1')
stimuli2train1.setVolume(1)
stimuli3train1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='stimuli3train1')
stimuli3train1.setVolume(1)
stimuli4train1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='stimuli4train1')
stimuli4train1.setVolume(1)
stimuli5train1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='stimuli5train1')
stimuli5train1.setVolume(1)
listenTrain1 = visual.TextStim(win=win, name='listenTrain1',
    text='Listen to the words:',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "train1QuestInstr"
train1QuestInstrClock = core.Clock()
train1QuestText = visual.TextStim(win=win, name='train1QuestText',
    text='You will now be presented with three questions. For each, you will hear one word and you will choose the image that corresponds to it by clicking the keys F or J.\n\nPress any key to advance',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
train1QuestAdvance = keyboard.Keyboard()

# Initialize components for Routine "trainquestions1"
trainquestions1Clock = core.Clock()
stimulitest1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='stimulitest1')
stimulitest1.setVolume(1)
correct = visual.ImageStim(
    win=win,
    name='correct', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
incorrect = visual.ImageStim(
    win=win,
    name='incorrect', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
train1Response = keyboard.Keyboard()
chooseImageTrain1 = visual.TextStim(win=win, name='chooseImageTrain1',
    text='Choose the image (f or j) that matches the audio:',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
train1F = visual.TextStim(win=win, name='train1F',
    text='F',
    font='Arial',
    pos=(-0.5, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
train1J = visual.TextStim(win=win, name='train1J',
    text='J',
    font='Arial',
    pos=(0.5, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
train2warning10 = visual.TextStim(win=win, name='train2warning10',
    text='Next part will  start automatically\nin less than 10 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
train2warning5 = visual.TextStim(win=win, name='train2warning5',
    text='Next part will  start automatically\nin less than 5 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
train2warning4 = visual.TextStim(win=win, name='train2warning4',
    text='Next part will  start automatically\nin less than 4 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
train2warning3 = visual.TextStim(win=win, name='train2warning3',
    text='Next part will  start automatically\nin less than 3 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
train2warning2 = visual.TextStim(win=win, name='train2warning2',
    text='Next part will  start automatically\nin less than 2 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
train2warning1 = visual.TextStim(win=win, name='train2warning1',
    text='Next part will  start automatically\nin less than 1 minute.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
skipTrain2Instr = keyboard.Keyboard()

# Initialize components for Routine "train2"
train2Clock = core.Clock()
imagetrain2 = visual.ImageStim(
    win=win,
    name='imagetrain2', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
stimuli1train2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='stimuli1train2')
stimuli1train2.setVolume(1)
stimuli2train2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='stimuli2train2')
stimuli2train2.setVolume(1)
stimuli3train2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='stimuli3train2')
stimuli3train2.setVolume(1)
stimuli4train2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='stimuli4train2')
stimuli4train2.setVolume(1)
stimuli5train2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='stimuli5train2')
stimuli5train2.setVolume(1)
listenTrain2 = visual.TextStim(win=win, name='listenTrain2',
    text='Listen to the words:',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "train2QuestInstr"
train2QuestInstrClock = core.Clock()
train2QuestText = visual.TextStim(win=win, name='train2QuestText',
    text='You will now be presented with three questions. For each, you will hear one word and you will choose the image that corresponds to it by clicking the keys F or J.\n\nPress any key to advance',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
train2QuestAdvance = keyboard.Keyboard()

# Initialize components for Routine "trainquestions2"
trainquestions2Clock = core.Clock()
stimulitest2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='stimulitest2')
stimulitest2.setVolume(1)
correct2 = visual.ImageStim(
    win=win,
    name='correct2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
incorrect2 = visual.ImageStim(
    win=win,
    name='incorrect2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
train2Response = keyboard.Keyboard()
chooseImageTrain2 = visual.TextStim(win=win, name='chooseImageTrain2',
    text='Choose the image (f or j) that matches the audio:',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
train2F = visual.TextStim(win=win, name='train2F',
    text='F',
    font='Arial',
    pos=(-0.5, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
train2J = visual.TextStim(win=win, name='train2J',
    text='J',
    font='Arial',
    pos=(0.5, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "testTrainInstr"
testTrainInstrClock = core.Clock()
skipTest1Instr = keyboard.Keyboard()
test1warning10 = visual.TextStim(win=win, name='test1warning10',
    text='Next part will  start automatically\nin less than 10 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
test1warning5 = visual.TextStim(win=win, name='test1warning5',
    text='Next part will  start automatically\nin less than 5 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
test1warning4 = visual.TextStim(win=win, name='test1warning4',
    text='Next part will  start automatically\nin less than 4 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
test1warning3 = visual.TextStim(win=win, name='test1warning3',
    text='Next part will  start automatically\nin less than 3 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
test1warning2 = visual.TextStim(win=win, name='test1warning2',
    text='Next part will  start automatically\nin less than 2 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
test1warning1 = visual.TextStim(win=win, name='test1warning1',
    text='Next part will  start automatically\nin less than 1 minute.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "test1"
test1Clock = core.Clock()
test1Audio1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='test1Audio1')
test1Audio1.setVolume(1)
test1Audio1Sound = visual.ImageStim(
    win=win,
    name='test1Audio1Sound', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
test1Audio1Mute = visual.ImageStim(
    win=win,
    name='test1Audio1Mute', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
test1Audio2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='test1Audio2')
test1Audio2.setVolume(1)
test1Audio2Mute1 = visual.ImageStim(
    win=win,
    name='test1Audio2Mute1', 
    image='sin', mask=None,
    ori=0, pos=(0.3, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
test1Audio2Sound = visual.ImageStim(
    win=win,
    name='test1Audio2Sound', 
    image='sin', mask=None,
    ori=0, pos=(0.3, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
test1Audio2Mute2 = visual.ImageStim(
    win=win,
    name='test1Audio2Mute2', 
    image='sin', mask=None,
    ori=0, pos=(0.3, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
test1Response = keyboard.Keyboard()
test1Image = visual.ImageStim(
    win=win,
    name='test1Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.1), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
test1F = visual.TextStim(win=win, name='test1F',
    text='F',
    font='Arial',
    pos=(-0.3, -0.1), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
test1J = visual.TextStim(win=win, name='test1J',
    text='J',
    font='Arial',
    pos=(0.3, -0.1), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
test1Instr = visual.TextStim(win=win, name='test1Instr',
    text='Choose the audio that has the correct pronunciation (F or J)',
    font='Arial',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "testNovel1Instr"
testNovel1InstrClock = core.Clock()
skipTest2Instr = keyboard.Keyboard()
test2warning10 = visual.TextStim(win=win, name='test2warning10',
    text='Next part will  start automatically\nin less than 10 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
test2warning5 = visual.TextStim(win=win, name='test2warning5',
    text='Next part will  start automatically\nin less than 5 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
test2warning4 = visual.TextStim(win=win, name='test2warning4',
    text='Next part will  start automatically\nin less than 4 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
test2warning3 = visual.TextStim(win=win, name='test2warning3',
    text='Next part will  start automatically\nin less than 3 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
test2warning2 = visual.TextStim(win=win, name='test2warning2',
    text='Next part will  start automatically\nin less than 2 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
test2warning1 = visual.TextStim(win=win, name='test2warning1',
    text='Next part will  start automatically\nin less than 1 minute.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "test2"
test2Clock = core.Clock()
test2Audio1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='test2Audio1')
test2Audio1.setVolume(1)
test2Audio1Sound = visual.ImageStim(
    win=win,
    name='test2Audio1Sound', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
test1Audio2Mute = visual.ImageStim(
    win=win,
    name='test1Audio2Mute', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
test2Audio2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='test2Audio2')
test2Audio2.setVolume(1)
test2Audio2Mute1 = visual.ImageStim(
    win=win,
    name='test2Audio2Mute1', 
    image='sin', mask=None,
    ori=0, pos=(0.3, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
test2Audio2Sound = visual.ImageStim(
    win=win,
    name='test2Audio2Sound', 
    image='sin', mask=None,
    ori=0, pos=(0.3, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
test2Audio2Mute2 = visual.ImageStim(
    win=win,
    name='test2Audio2Mute2', 
    image='mute.png', mask=None,
    ori=0, pos=(0.3, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
test2Response = keyboard.Keyboard()
test2Image = visual.ImageStim(
    win=win,
    name='test2Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.1), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
test2F = visual.TextStim(win=win, name='test2F',
    text='F',
    font='Arial',
    pos=(-0.3, -0.1), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
test2J = visual.TextStim(win=win, name='test2J',
    text='J',
    font='Arial',
    pos=(0.3, -0.1), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
test2Instr = visual.TextStim(win=win, name='test2Instr',
    text='Choose the audio that has the correct pronunciation (F or J)',
    font='Arial',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "testNovel2Instr"
testNovel2InstrClock = core.Clock()
skipTest3Instr = keyboard.Keyboard()
test3warning10 = visual.TextStim(win=win, name='test3warning10',
    text='Next part will  start automatically\nin less than 10 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
test3warning5 = visual.TextStim(win=win, name='test3warning5',
    text='Next part will  start automatically\nin less than 5 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
test3warning4 = visual.TextStim(win=win, name='test3warning4',
    text='Next part will  start automatically\nin less than 4 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
test3warning3 = visual.TextStim(win=win, name='test3warning3',
    text='Next part will  start automatically\nin less than 3 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
test3warning2 = visual.TextStim(win=win, name='test3warning2',
    text='Next part will  start automatically\nin less than 2 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
test3warning1 = visual.TextStim(win=win, name='test3warning1',
    text='Next part will  start automatically\nin less than 1 minute.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "test3"
test3Clock = core.Clock()
test3Audio1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='test3Audio1')
test3Audio1.setVolume(1)
test3Audio1Sound = visual.ImageStim(
    win=win,
    name='test3Audio1Sound', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
test3Audio1Mute = visual.ImageStim(
    win=win,
    name='test3Audio1Mute', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
test3Audio2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='test3Audio2')
test3Audio2.setVolume(1)
test3Audio2Mute1 = visual.ImageStim(
    win=win,
    name='test3Audio2Mute1', 
    image='sin', mask=None,
    ori=0, pos=(0.3, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
test3Audio2Sound = visual.ImageStim(
    win=win,
    name='test3Audio2Sound', 
    image='sin', mask=None,
    ori=0, pos=(0.3, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
test3Audio2Mute2 = visual.ImageStim(
    win=win,
    name='test3Audio2Mute2', 
    image='sin', mask=None,
    ori=0, pos=(0.3, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
test3Response = keyboard.Keyboard()
test3Image = visual.ImageStim(
    win=win,
    name='test3Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.1), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
test3F = visual.TextStim(win=win, name='test3F',
    text='F',
    font='Arial',
    pos=(-0.3, -0.1), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
test3J = visual.TextStim(win=win, name='test3J',
    text='J',
    font='Arial',
    pos=(0.3, -0.1), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
test3Instr = visual.TextStim(win=win, name='test3Instr',
    text='Choose the audio that has the correct pronunciation (F or J)',
    font='Arial',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "postTestInstr"
postTestInstrClock = core.Clock()
skipPostTestInstr = keyboard.Keyboard()
postTestWarning10 = visual.TextStim(win=win, name='postTestWarning10',
    text='Next part will  start automatically\nin less than 10 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
postTestWarning5 = visual.TextStim(win=win, name='postTestWarning5',
    text='Next part will  start automatically\nin less than 5 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
postTestWarning4 = visual.TextStim(win=win, name='postTestWarning4',
    text='Next part will  start automatically\nin less than 4 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
postTestWarning3 = visual.TextStim(win=win, name='postTestWarning3',
    text='Next part will  start automatically\nin less than 3 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
postTestWarning2 = visual.TextStim(win=win, name='postTestWarning2',
    text='Next part will  start automatically\nin less than 2 minutes.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
postTestWarning1 = visual.TextStim(win=win, name='postTestWarning1',
    text='Next part will  start automatically\nin less than 1 minute.\n\nPress any button to start now',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "posttest"
posttestClock = core.Clock()
postTestResponse = keyboard.Keyboard()
postTestAudio1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='postTestAudio1')
postTestAudio1.setVolume(1)
fSound = visual.ImageStim(
    win=win,
    name='fSound', 
    image='sound.png', mask=None,
    ori=0, pos=(-0.5, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
fMute = visual.ImageStim(
    win=win,
    name='fMute', 
    image='mute.png', mask=None,
    ori=0, pos=(-0.5, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
postTestAudio2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='postTestAudio2')
postTestAudio2.setVolume(1)
xMute1 = visual.ImageStim(
    win=win,
    name='xMute1', 
    image='mute.png', mask=None,
    ori=0, pos=(0, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
xSound = visual.ImageStim(
    win=win,
    name='xSound', 
    image='sound.png', mask=None,
    ori=0, pos=(0, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
xMute2 = visual.ImageStim(
    win=win,
    name='xMute2', 
    image='mute.png', mask=None,
    ori=0, pos=(0, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
postTestAudio3 = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='postTestAudio3')
postTestAudio3.setVolume(1)
jMute1 = visual.ImageStim(
    win=win,
    name='jMute1', 
    image='mute.png', mask=None,
    ori=0, pos=(0.5, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
jSound = visual.ImageStim(
    win=win,
    name='jSound', 
    image='sound.png', mask=None,
    ori=0, pos=(0.5, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
jMute2 = visual.ImageStim(
    win=win,
    name='jMute2', 
    image='mute.png', mask=None,
    ori=0, pos=(0.5, -0.3), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
textInstrPostTest = visual.TextStim(win=win, name='textInstrPostTest',
    text='Does the middle audio (X) match in stress with F or J? (Press F or J)',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
fText = visual.TextStim(win=win, name='fText',
    text='F',
    font='Arial',
    pos=(-0.5, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
xText = visual.TextStim(win=win, name='xText',
    text='X',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
jText = visual.TextStim(win=win, name='jText',
    text='J',
    font='Arial',
    pos=(0.5, 0), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);

# Initialize components for Routine "thankuser"
thankuserClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Thank you for participating!\n\nPress any button to end this experiment',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
quit = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
advanceTrain1.keys = []
advanceTrain1.rt = []
_advanceTrain1_allKeys = []
# keep track of which components have finished
instrComponents = [instructions, advanceTrain1]
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
    
    # *advanceTrain1* updates
    waitOnFlip = False
    if advanceTrain1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        advanceTrain1.frameNStart = frameN  # exact frame index
        advanceTrain1.tStart = t  # local t and not account for scr refresh
        advanceTrain1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(advanceTrain1, 'tStartRefresh')  # time at next scr refresh
        advanceTrain1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(advanceTrain1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(advanceTrain1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if advanceTrain1.status == STARTED and not waitOnFlip:
        theseKeys = advanceTrain1.getKeys(keyList=None, waitRelease=False)
        _advanceTrain1_allKeys.extend(theseKeys)
        if len(_advanceTrain1_allKeys):
            advanceTrain1.keys = _advanceTrain1_allKeys[-1].name  # just the last key pressed
            advanceTrain1.rt = _advanceTrain1_allKeys[-1].rt
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
    trialList=data.importConditions('aoiConditions\\train1LoopCondition.xlsx'),
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
        # update component parameters for each repeat
        imagetrain1.setImage(imageLoc)
        stimuli1train1.setSound(audio, hamming=True)
        stimuli1train1.setVolume(1, log=False)
        stimuli2train1.setSound(audio, hamming=True)
        stimuli2train1.setVolume(1, log=False)
        stimuli3train1.setSound(audio, hamming=True)
        stimuli3train1.setVolume(1, log=False)
        stimuli4train1.setSound(audio, hamming=True)
        stimuli4train1.setVolume(1, log=False)
        stimuli5train1.setSound(audio, hamming=True)
        stimuli5train1.setVolume(1, log=False)
        # keep track of which components have finished
        train1Components = [imagetrain1, stimuli1train1, stimuli2train1, stimuli3train1, stimuli4train1, stimuli5train1, listenTrain1]
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
        while continueRoutine:
            # get current time
            t = train1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=train1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *imagetrain1* updates
            if imagetrain1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                imagetrain1.frameNStart = frameN  # exact frame index
                imagetrain1.tStart = t  # local t and not account for scr refresh
                imagetrain1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imagetrain1, 'tStartRefresh')  # time at next scr refresh
                imagetrain1.setAutoDraw(True)
            if imagetrain1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > imagetrain1.tStartRefresh + 9-frameTolerance:
                    # keep track of stop time/frame for later
                    imagetrain1.tStop = t  # not accounting for scr refresh
                    imagetrain1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(imagetrain1, 'tStopRefresh')  # time at next scr refresh
                    imagetrain1.setAutoDraw(False)
            # start/stop stimuli1train1
            if stimuli1train1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                stimuli1train1.frameNStart = frameN  # exact frame index
                stimuli1train1.tStart = t  # local t and not account for scr refresh
                stimuli1train1.tStartRefresh = tThisFlipGlobal  # on global time
                stimuli1train1.play(when=win)  # sync with win flip
            # start/stop stimuli2train1
            if stimuli2train1.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                stimuli2train1.frameNStart = frameN  # exact frame index
                stimuli2train1.tStart = t  # local t and not account for scr refresh
                stimuli2train1.tStartRefresh = tThisFlipGlobal  # on global time
                stimuli2train1.play(when=win)  # sync with win flip
            # start/stop stimuli3train1
            if stimuli3train1.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
                # keep track of start time/frame for later
                stimuli3train1.frameNStart = frameN  # exact frame index
                stimuli3train1.tStart = t  # local t and not account for scr refresh
                stimuli3train1.tStartRefresh = tThisFlipGlobal  # on global time
                stimuli3train1.play(when=win)  # sync with win flip
            # start/stop stimuli4train1
            if stimuli4train1.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
                # keep track of start time/frame for later
                stimuli4train1.frameNStart = frameN  # exact frame index
                stimuli4train1.tStart = t  # local t and not account for scr refresh
                stimuli4train1.tStartRefresh = tThisFlipGlobal  # on global time
                stimuli4train1.play(when=win)  # sync with win flip
            # start/stop stimuli5train1
            if stimuli5train1.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
                # keep track of start time/frame for later
                stimuli5train1.frameNStart = frameN  # exact frame index
                stimuli5train1.tStart = t  # local t and not account for scr refresh
                stimuli5train1.tStartRefresh = tThisFlipGlobal  # on global time
                stimuli5train1.play(when=win)  # sync with win flip
            
            # *listenTrain1* updates
            if listenTrain1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                listenTrain1.frameNStart = frameN  # exact frame index
                listenTrain1.tStart = t  # local t and not account for scr refresh
                listenTrain1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(listenTrain1, 'tStartRefresh')  # time at next scr refresh
                listenTrain1.setAutoDraw(True)
            if listenTrain1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > listenTrain1.tStartRefresh + 11-frameTolerance:
                    # keep track of stop time/frame for later
                    listenTrain1.tStop = t  # not accounting for scr refresh
                    listenTrain1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(listenTrain1, 'tStopRefresh')  # time at next scr refresh
                    listenTrain1.setAutoDraw(False)
            
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
        blockwords1.addData('imagetrain1.started', imagetrain1.tStartRefresh)
        blockwords1.addData('imagetrain1.stopped', imagetrain1.tStopRefresh)
        stimuli1train1.stop()  # ensure sound has stopped at end of routine
        blockwords1.addData('stimuli1train1.started', stimuli1train1.tStartRefresh)
        blockwords1.addData('stimuli1train1.stopped', stimuli1train1.tStopRefresh)
        stimuli2train1.stop()  # ensure sound has stopped at end of routine
        blockwords1.addData('stimuli2train1.started', stimuli2train1.tStartRefresh)
        blockwords1.addData('stimuli2train1.stopped', stimuli2train1.tStopRefresh)
        stimuli3train1.stop()  # ensure sound has stopped at end of routine
        blockwords1.addData('stimuli3train1.started', stimuli3train1.tStartRefresh)
        blockwords1.addData('stimuli3train1.stopped', stimuli3train1.tStopRefresh)
        stimuli4train1.stop()  # ensure sound has stopped at end of routine
        blockwords1.addData('stimuli4train1.started', stimuli4train1.tStartRefresh)
        blockwords1.addData('stimuli4train1.stopped', stimuli4train1.tStopRefresh)
        stimuli5train1.stop()  # ensure sound has stopped at end of routine
        blockwords1.addData('stimuli5train1.started', stimuli5train1.tStartRefresh)
        blockwords1.addData('stimuli5train1.stopped', stimuli5train1.tStopRefresh)
        blockwords1.addData('listenTrain1.started', listenTrain1.tStartRefresh)
        blockwords1.addData('listenTrain1.stopped', listenTrain1.tStopRefresh)
        # the Routine "train1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'blockwords1'
    
    
    # ------Prepare to start Routine "train1QuestInstr"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    train1QuestAdvance.keys = []
    train1QuestAdvance.rt = []
    _train1QuestAdvance_allKeys = []
    # keep track of which components have finished
    train1QuestInstrComponents = [train1QuestText, train1QuestAdvance]
    for thisComponent in train1QuestInstrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    train1QuestInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "train1QuestInstr"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = train1QuestInstrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=train1QuestInstrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *train1QuestText* updates
        if train1QuestText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            train1QuestText.frameNStart = frameN  # exact frame index
            train1QuestText.tStart = t  # local t and not account for scr refresh
            train1QuestText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(train1QuestText, 'tStartRefresh')  # time at next scr refresh
            train1QuestText.setAutoDraw(True)
        if train1QuestText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > train1QuestText.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                train1QuestText.tStop = t  # not accounting for scr refresh
                train1QuestText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(train1QuestText, 'tStopRefresh')  # time at next scr refresh
                train1QuestText.setAutoDraw(False)
        
        # *train1QuestAdvance* updates
        waitOnFlip = False
        if train1QuestAdvance.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            train1QuestAdvance.frameNStart = frameN  # exact frame index
            train1QuestAdvance.tStart = t  # local t and not account for scr refresh
            train1QuestAdvance.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(train1QuestAdvance, 'tStartRefresh')  # time at next scr refresh
            train1QuestAdvance.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(train1QuestAdvance.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(train1QuestAdvance.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if train1QuestAdvance.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > train1QuestAdvance.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                train1QuestAdvance.tStop = t  # not accounting for scr refresh
                train1QuestAdvance.frameNStop = frameN  # exact frame index
                win.timeOnFlip(train1QuestAdvance, 'tStopRefresh')  # time at next scr refresh
                train1QuestAdvance.status = FINISHED
        if train1QuestAdvance.status == STARTED and not waitOnFlip:
            theseKeys = train1QuestAdvance.getKeys(keyList=None, waitRelease=False)
            _train1QuestAdvance_allKeys.extend(theseKeys)
            if len(_train1QuestAdvance_allKeys):
                train1QuestAdvance.keys = _train1QuestAdvance_allKeys[-1].name  # just the last key pressed
                train1QuestAdvance.rt = _train1QuestAdvance_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in train1QuestInstrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "train1QuestInstr"-------
    for thisComponent in train1QuestInstrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    train1blocks.addData('train1QuestText.started', train1QuestText.tStartRefresh)
    train1blocks.addData('train1QuestText.stopped', train1QuestText.tStopRefresh)
    # check responses
    if train1QuestAdvance.keys in ['', [], None]:  # No response was made
        train1QuestAdvance.keys = None
    train1blocks.addData('train1QuestAdvance.keys',train1QuestAdvance.keys)
    if train1QuestAdvance.keys != None:  # we had a response
        train1blocks.addData('train1QuestAdvance.rt', train1QuestAdvance.rt)
    train1blocks.addData('train1QuestAdvance.started', train1QuestAdvance.tStartRefresh)
    train1blocks.addData('train1QuestAdvance.stopped', train1QuestAdvance.tStopRefresh)
    
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
        # update component parameters for each repeat
        stimulitest1.setSound(audioTrue, hamming=True)
        stimulitest1.setVolume(1, log=False)
        correct.setPos((truePos,-0.3))
        correct.setImage(imageTrue)
        incorrect.setPos((falsePos,-0.3))
        incorrect.setImage(imageFalse)
        train1Response.keys = []
        train1Response.rt = []
        _train1Response_allKeys = []
        # keep track of which components have finished
        trainquestions1Components = [stimulitest1, correct, incorrect, train1Response, chooseImageTrain1, train1F, train1J]
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
        while continueRoutine:
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
            
            # *train1Response* updates
            waitOnFlip = False
            if train1Response.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                train1Response.frameNStart = frameN  # exact frame index
                train1Response.tStart = t  # local t and not account for scr refresh
                train1Response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(train1Response, 'tStartRefresh')  # time at next scr refresh
                train1Response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(train1Response.clock.reset)  # t=0 on next screen flip
            if train1Response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > train1Response.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    train1Response.tStop = t  # not accounting for scr refresh
                    train1Response.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(train1Response, 'tStopRefresh')  # time at next scr refresh
                    train1Response.status = FINISHED
            if train1Response.status == STARTED and not waitOnFlip:
                theseKeys = train1Response.getKeys(keyList=['f', 'j'], waitRelease=False)
                _train1Response_allKeys.extend(theseKeys)
                if len(_train1Response_allKeys):
                    train1Response.keys = _train1Response_allKeys[-1].name  # just the last key pressed
                    train1Response.rt = _train1Response_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *chooseImageTrain1* updates
            if chooseImageTrain1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                chooseImageTrain1.frameNStart = frameN  # exact frame index
                chooseImageTrain1.tStart = t  # local t and not account for scr refresh
                chooseImageTrain1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(chooseImageTrain1, 'tStartRefresh')  # time at next scr refresh
                chooseImageTrain1.setAutoDraw(True)
            if chooseImageTrain1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > chooseImageTrain1.tStartRefresh + 7-frameTolerance:
                    # keep track of stop time/frame for later
                    chooseImageTrain1.tStop = t  # not accounting for scr refresh
                    chooseImageTrain1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(chooseImageTrain1, 'tStopRefresh')  # time at next scr refresh
                    chooseImageTrain1.setAutoDraw(False)
            
            # *train1F* updates
            if train1F.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                train1F.frameNStart = frameN  # exact frame index
                train1F.tStart = t  # local t and not account for scr refresh
                train1F.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(train1F, 'tStartRefresh')  # time at next scr refresh
                train1F.setAutoDraw(True)
            if train1F.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > train1F.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    train1F.tStop = t  # not accounting for scr refresh
                    train1F.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(train1F, 'tStopRefresh')  # time at next scr refresh
                    train1F.setAutoDraw(False)
            
            # *train1J* updates
            if train1J.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                train1J.frameNStart = frameN  # exact frame index
                train1J.tStart = t  # local t and not account for scr refresh
                train1J.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(train1J, 'tStartRefresh')  # time at next scr refresh
                train1J.setAutoDraw(True)
            if train1J.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > train1J.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    train1J.tStop = t  # not accounting for scr refresh
                    train1J.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(train1J, 'tStopRefresh')  # time at next scr refresh
                    train1J.setAutoDraw(False)
            
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
        if train1Response.keys in ['', [], None]:  # No response was made
            train1Response.keys = None
        blocktest1.addData('train1Response.keys',train1Response.keys)
        if train1Response.keys != None:  # we had a response
            blocktest1.addData('train1Response.rt', train1Response.rt)
        blocktest1.addData('train1Response.started', train1Response.tStartRefresh)
        blocktest1.addData('train1Response.stopped', train1Response.tStopRefresh)
        blocktest1.addData('chooseImageTrain1.started', chooseImageTrain1.tStartRefresh)
        blocktest1.addData('chooseImageTrain1.stopped', chooseImageTrain1.tStopRefresh)
        blocktest1.addData('train1F.started', train1F.tStartRefresh)
        blocktest1.addData('train1F.stopped', train1F.tStopRefresh)
        blocktest1.addData('train1J.started', train1J.tStartRefresh)
        blocktest1.addData('train1J.stopped', train1J.tStopRefresh)
        # the Routine "trainquestions1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'blocktest1'
    
    thisExp.nextEntry()
    
# completed 0 repeats of 'train1blocks'


# ------Prepare to start Routine "instr2"-------
continueRoutine = True
routineTimer.add(600.000000)
# update component parameters for each repeat
skipTrain2Instr.keys = []
skipTrain2Instr.rt = []
_skipTrain2Instr_allKeys = []
# keep track of which components have finished
instr2Components = [train2warning10, train2warning5, train2warning4, train2warning3, train2warning2, train2warning1, skipTrain2Instr]
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
    
    # *train2warning10* updates
    if train2warning10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        train2warning10.frameNStart = frameN  # exact frame index
        train2warning10.tStart = t  # local t and not account for scr refresh
        train2warning10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(train2warning10, 'tStartRefresh')  # time at next scr refresh
        train2warning10.setAutoDraw(True)
    if train2warning10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > train2warning10.tStartRefresh + 300-frameTolerance:
            # keep track of stop time/frame for later
            train2warning10.tStop = t  # not accounting for scr refresh
            train2warning10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(train2warning10, 'tStopRefresh')  # time at next scr refresh
            train2warning10.setAutoDraw(False)
    
    # *train2warning5* updates
    if train2warning5.status == NOT_STARTED and tThisFlip >= 300-frameTolerance:
        # keep track of start time/frame for later
        train2warning5.frameNStart = frameN  # exact frame index
        train2warning5.tStart = t  # local t and not account for scr refresh
        train2warning5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(train2warning5, 'tStartRefresh')  # time at next scr refresh
        train2warning5.setAutoDraw(True)
    if train2warning5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > train2warning5.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            train2warning5.tStop = t  # not accounting for scr refresh
            train2warning5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(train2warning5, 'tStopRefresh')  # time at next scr refresh
            train2warning5.setAutoDraw(False)
    
    # *train2warning4* updates
    if train2warning4.status == NOT_STARTED and tThisFlip >= 360-frameTolerance:
        # keep track of start time/frame for later
        train2warning4.frameNStart = frameN  # exact frame index
        train2warning4.tStart = t  # local t and not account for scr refresh
        train2warning4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(train2warning4, 'tStartRefresh')  # time at next scr refresh
        train2warning4.setAutoDraw(True)
    if train2warning4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > train2warning4.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            train2warning4.tStop = t  # not accounting for scr refresh
            train2warning4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(train2warning4, 'tStopRefresh')  # time at next scr refresh
            train2warning4.setAutoDraw(False)
    
    # *train2warning3* updates
    if train2warning3.status == NOT_STARTED and tThisFlip >= 420-frameTolerance:
        # keep track of start time/frame for later
        train2warning3.frameNStart = frameN  # exact frame index
        train2warning3.tStart = t  # local t and not account for scr refresh
        train2warning3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(train2warning3, 'tStartRefresh')  # time at next scr refresh
        train2warning3.setAutoDraw(True)
    if train2warning3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > train2warning3.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            train2warning3.tStop = t  # not accounting for scr refresh
            train2warning3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(train2warning3, 'tStopRefresh')  # time at next scr refresh
            train2warning3.setAutoDraw(False)
    
    # *train2warning2* updates
    if train2warning2.status == NOT_STARTED and tThisFlip >= 480-frameTolerance:
        # keep track of start time/frame for later
        train2warning2.frameNStart = frameN  # exact frame index
        train2warning2.tStart = t  # local t and not account for scr refresh
        train2warning2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(train2warning2, 'tStartRefresh')  # time at next scr refresh
        train2warning2.setAutoDraw(True)
    if train2warning2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > train2warning2.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            train2warning2.tStop = t  # not accounting for scr refresh
            train2warning2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(train2warning2, 'tStopRefresh')  # time at next scr refresh
            train2warning2.setAutoDraw(False)
    
    # *train2warning1* updates
    if train2warning1.status == NOT_STARTED and tThisFlip >= 540-frameTolerance:
        # keep track of start time/frame for later
        train2warning1.frameNStart = frameN  # exact frame index
        train2warning1.tStart = t  # local t and not account for scr refresh
        train2warning1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(train2warning1, 'tStartRefresh')  # time at next scr refresh
        train2warning1.setAutoDraw(True)
    if train2warning1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > train2warning1.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            train2warning1.tStop = t  # not accounting for scr refresh
            train2warning1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(train2warning1, 'tStopRefresh')  # time at next scr refresh
            train2warning1.setAutoDraw(False)
    
    # *skipTrain2Instr* updates
    waitOnFlip = False
    if skipTrain2Instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skipTrain2Instr.frameNStart = frameN  # exact frame index
        skipTrain2Instr.tStart = t  # local t and not account for scr refresh
        skipTrain2Instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skipTrain2Instr, 'tStartRefresh')  # time at next scr refresh
        skipTrain2Instr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skipTrain2Instr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skipTrain2Instr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skipTrain2Instr.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > skipTrain2Instr.tStartRefresh + 600-frameTolerance:
            # keep track of stop time/frame for later
            skipTrain2Instr.tStop = t  # not accounting for scr refresh
            skipTrain2Instr.frameNStop = frameN  # exact frame index
            win.timeOnFlip(skipTrain2Instr, 'tStopRefresh')  # time at next scr refresh
            skipTrain2Instr.status = FINISHED
    if skipTrain2Instr.status == STARTED and not waitOnFlip:
        theseKeys = skipTrain2Instr.getKeys(keyList=None, waitRelease=False)
        _skipTrain2Instr_allKeys.extend(theseKeys)
        if len(_skipTrain2Instr_allKeys):
            skipTrain2Instr.keys = _skipTrain2Instr_allKeys[-1].name  # just the last key pressed
            skipTrain2Instr.rt = _skipTrain2Instr_allKeys[-1].rt
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
thisExp.addData('train2warning10.started', train2warning10.tStartRefresh)
thisExp.addData('train2warning10.stopped', train2warning10.tStopRefresh)
thisExp.addData('train2warning5.started', train2warning5.tStartRefresh)
thisExp.addData('train2warning5.stopped', train2warning5.tStopRefresh)
thisExp.addData('train2warning4.started', train2warning4.tStartRefresh)
thisExp.addData('train2warning4.stopped', train2warning4.tStopRefresh)
thisExp.addData('train2warning3.started', train2warning3.tStartRefresh)
thisExp.addData('train2warning3.stopped', train2warning3.tStopRefresh)
thisExp.addData('train2warning2.started', train2warning2.tStartRefresh)
thisExp.addData('train2warning2.stopped', train2warning2.tStopRefresh)
thisExp.addData('train2warning1.started', train2warning1.tStartRefresh)
thisExp.addData('train2warning1.stopped', train2warning1.tStopRefresh)
# check responses
if skipTrain2Instr.keys in ['', [], None]:  # No response was made
    skipTrain2Instr.keys = None
thisExp.addData('skipTrain2Instr.keys',skipTrain2Instr.keys)
if skipTrain2Instr.keys != None:  # we had a response
    thisExp.addData('skipTrain2Instr.rt', skipTrain2Instr.rt)
thisExp.addData('skipTrain2Instr.started', skipTrain2Instr.tStartRefresh)
thisExp.addData('skipTrain2Instr.stopped', skipTrain2Instr.tStopRefresh)
thisExp.nextEntry()

# set up handler to look after randomisation of conditions etc
train2blocks = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('aoiConditions\\train2LoopCondition.xlsx'),
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
        # update component parameters for each repeat
        imagetrain2.setImage(imageLoc)
        stimuli1train2.setSound(audio, hamming=True)
        stimuli1train2.setVolume(1, log=False)
        stimuli2train2.setSound(audio, hamming=True)
        stimuli2train2.setVolume(1, log=False)
        stimuli3train2.setSound(audio, hamming=True)
        stimuli3train2.setVolume(1, log=False)
        stimuli4train2.setSound(audio, hamming=True)
        stimuli4train2.setVolume(1, log=False)
        stimuli5train2.setSound(audio, hamming=True)
        stimuli5train2.setVolume(1, log=False)
        # keep track of which components have finished
        train2Components = [imagetrain2, stimuli1train2, stimuli2train2, stimuli3train2, stimuli4train2, stimuli5train2, listenTrain2]
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
            
            # *imagetrain2* updates
            if imagetrain2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                imagetrain2.frameNStart = frameN  # exact frame index
                imagetrain2.tStart = t  # local t and not account for scr refresh
                imagetrain2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imagetrain2, 'tStartRefresh')  # time at next scr refresh
                imagetrain2.setAutoDraw(True)
            if imagetrain2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > imagetrain2.tStartRefresh + 9-frameTolerance:
                    # keep track of stop time/frame for later
                    imagetrain2.tStop = t  # not accounting for scr refresh
                    imagetrain2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(imagetrain2, 'tStopRefresh')  # time at next scr refresh
                    imagetrain2.setAutoDraw(False)
            # start/stop stimuli1train2
            if stimuli1train2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                stimuli1train2.frameNStart = frameN  # exact frame index
                stimuli1train2.tStart = t  # local t and not account for scr refresh
                stimuli1train2.tStartRefresh = tThisFlipGlobal  # on global time
                stimuli1train2.play(when=win)  # sync with win flip
            # start/stop stimuli2train2
            if stimuli2train2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                stimuli2train2.frameNStart = frameN  # exact frame index
                stimuli2train2.tStart = t  # local t and not account for scr refresh
                stimuli2train2.tStartRefresh = tThisFlipGlobal  # on global time
                stimuli2train2.play(when=win)  # sync with win flip
            # start/stop stimuli3train2
            if stimuli3train2.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
                # keep track of start time/frame for later
                stimuli3train2.frameNStart = frameN  # exact frame index
                stimuli3train2.tStart = t  # local t and not account for scr refresh
                stimuli3train2.tStartRefresh = tThisFlipGlobal  # on global time
                stimuli3train2.play(when=win)  # sync with win flip
            # start/stop stimuli4train2
            if stimuli4train2.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
                # keep track of start time/frame for later
                stimuli4train2.frameNStart = frameN  # exact frame index
                stimuli4train2.tStart = t  # local t and not account for scr refresh
                stimuli4train2.tStartRefresh = tThisFlipGlobal  # on global time
                stimuli4train2.play(when=win)  # sync with win flip
            # start/stop stimuli5train2
            if stimuli5train2.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
                # keep track of start time/frame for later
                stimuli5train2.frameNStart = frameN  # exact frame index
                stimuli5train2.tStart = t  # local t and not account for scr refresh
                stimuli5train2.tStartRefresh = tThisFlipGlobal  # on global time
                stimuli5train2.play(when=win)  # sync with win flip
            
            # *listenTrain2* updates
            if listenTrain2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                listenTrain2.frameNStart = frameN  # exact frame index
                listenTrain2.tStart = t  # local t and not account for scr refresh
                listenTrain2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(listenTrain2, 'tStartRefresh')  # time at next scr refresh
                listenTrain2.setAutoDraw(True)
            if listenTrain2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > listenTrain2.tStartRefresh + 11-frameTolerance:
                    # keep track of stop time/frame for later
                    listenTrain2.tStop = t  # not accounting for scr refresh
                    listenTrain2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(listenTrain2, 'tStopRefresh')  # time at next scr refresh
                    listenTrain2.setAutoDraw(False)
            
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
        blockloop2.addData('imagetrain2.started', imagetrain2.tStartRefresh)
        blockloop2.addData('imagetrain2.stopped', imagetrain2.tStopRefresh)
        stimuli1train2.stop()  # ensure sound has stopped at end of routine
        blockloop2.addData('stimuli1train2.started', stimuli1train2.tStartRefresh)
        blockloop2.addData('stimuli1train2.stopped', stimuli1train2.tStopRefresh)
        stimuli2train2.stop()  # ensure sound has stopped at end of routine
        blockloop2.addData('stimuli2train2.started', stimuli2train2.tStartRefresh)
        blockloop2.addData('stimuli2train2.stopped', stimuli2train2.tStopRefresh)
        stimuli3train2.stop()  # ensure sound has stopped at end of routine
        blockloop2.addData('stimuli3train2.started', stimuli3train2.tStartRefresh)
        blockloop2.addData('stimuli3train2.stopped', stimuli3train2.tStopRefresh)
        stimuli4train2.stop()  # ensure sound has stopped at end of routine
        blockloop2.addData('stimuli4train2.started', stimuli4train2.tStartRefresh)
        blockloop2.addData('stimuli4train2.stopped', stimuli4train2.tStopRefresh)
        stimuli5train2.stop()  # ensure sound has stopped at end of routine
        blockloop2.addData('stimuli5train2.started', stimuli5train2.tStartRefresh)
        blockloop2.addData('stimuli5train2.stopped', stimuli5train2.tStopRefresh)
        blockloop2.addData('listenTrain2.started', listenTrain2.tStartRefresh)
        blockloop2.addData('listenTrain2.stopped', listenTrain2.tStopRefresh)
        # the Routine "train2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'blockloop2'
    
    
    # ------Prepare to start Routine "train2QuestInstr"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    train2QuestAdvance.keys = []
    train2QuestAdvance.rt = []
    _train2QuestAdvance_allKeys = []
    # keep track of which components have finished
    train2QuestInstrComponents = [train2QuestText, train2QuestAdvance]
    for thisComponent in train2QuestInstrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    train2QuestInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "train2QuestInstr"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = train2QuestInstrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=train2QuestInstrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *train2QuestText* updates
        if train2QuestText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            train2QuestText.frameNStart = frameN  # exact frame index
            train2QuestText.tStart = t  # local t and not account for scr refresh
            train2QuestText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(train2QuestText, 'tStartRefresh')  # time at next scr refresh
            train2QuestText.setAutoDraw(True)
        if train2QuestText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > train2QuestText.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                train2QuestText.tStop = t  # not accounting for scr refresh
                train2QuestText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(train2QuestText, 'tStopRefresh')  # time at next scr refresh
                train2QuestText.setAutoDraw(False)
        
        # *train2QuestAdvance* updates
        waitOnFlip = False
        if train2QuestAdvance.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            train2QuestAdvance.frameNStart = frameN  # exact frame index
            train2QuestAdvance.tStart = t  # local t and not account for scr refresh
            train2QuestAdvance.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(train2QuestAdvance, 'tStartRefresh')  # time at next scr refresh
            train2QuestAdvance.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(train2QuestAdvance.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(train2QuestAdvance.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if train2QuestAdvance.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > train2QuestAdvance.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                train2QuestAdvance.tStop = t  # not accounting for scr refresh
                train2QuestAdvance.frameNStop = frameN  # exact frame index
                win.timeOnFlip(train2QuestAdvance, 'tStopRefresh')  # time at next scr refresh
                train2QuestAdvance.status = FINISHED
        if train2QuestAdvance.status == STARTED and not waitOnFlip:
            theseKeys = train2QuestAdvance.getKeys(keyList=None, waitRelease=False)
            _train2QuestAdvance_allKeys.extend(theseKeys)
            if len(_train2QuestAdvance_allKeys):
                train2QuestAdvance.keys = _train2QuestAdvance_allKeys[-1].name  # just the last key pressed
                train2QuestAdvance.rt = _train2QuestAdvance_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in train2QuestInstrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "train2QuestInstr"-------
    for thisComponent in train2QuestInstrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    train2blocks.addData('train2QuestText.started', train2QuestText.tStartRefresh)
    train2blocks.addData('train2QuestText.stopped', train2QuestText.tStopRefresh)
    # check responses
    if train2QuestAdvance.keys in ['', [], None]:  # No response was made
        train2QuestAdvance.keys = None
    train2blocks.addData('train2QuestAdvance.keys',train2QuestAdvance.keys)
    if train2QuestAdvance.keys != None:  # we had a response
        train2blocks.addData('train2QuestAdvance.rt', train2QuestAdvance.rt)
    train2blocks.addData('train2QuestAdvance.started', train2QuestAdvance.tStartRefresh)
    train2blocks.addData('train2QuestAdvance.stopped', train2QuestAdvance.tStopRefresh)
    
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
        # update component parameters for each repeat
        stimulitest2.setSound(audioTrue, hamming=True)
        stimulitest2.setVolume(1, log=False)
        correct2.setPos((truePos, -0.3))
        correct2.setImage(imageTrue)
        incorrect2.setPos((falsePos, -0.3))
        incorrect2.setImage(imageFalse)
        train2Response.keys = []
        train2Response.rt = []
        _train2Response_allKeys = []
        # keep track of which components have finished
        trainquestions2Components = [stimulitest2, correct2, incorrect2, train2Response, chooseImageTrain2, train2F, train2J]
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
            # start/stop stimulitest2
            if stimulitest2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stimulitest2.frameNStart = frameN  # exact frame index
                stimulitest2.tStart = t  # local t and not account for scr refresh
                stimulitest2.tStartRefresh = tThisFlipGlobal  # on global time
                stimulitest2.play(when=win)  # sync with win flip
            
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
            
            # *train2Response* updates
            waitOnFlip = False
            if train2Response.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                train2Response.frameNStart = frameN  # exact frame index
                train2Response.tStart = t  # local t and not account for scr refresh
                train2Response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(train2Response, 'tStartRefresh')  # time at next scr refresh
                train2Response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(train2Response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(train2Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if train2Response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > train2Response.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    train2Response.tStop = t  # not accounting for scr refresh
                    train2Response.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(train2Response, 'tStopRefresh')  # time at next scr refresh
                    train2Response.status = FINISHED
            if train2Response.status == STARTED and not waitOnFlip:
                theseKeys = train2Response.getKeys(keyList=['f', 'j'], waitRelease=False)
                _train2Response_allKeys.extend(theseKeys)
                if len(_train2Response_allKeys):
                    train2Response.keys = _train2Response_allKeys[-1].name  # just the last key pressed
                    train2Response.rt = _train2Response_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *chooseImageTrain2* updates
            if chooseImageTrain2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                chooseImageTrain2.frameNStart = frameN  # exact frame index
                chooseImageTrain2.tStart = t  # local t and not account for scr refresh
                chooseImageTrain2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(chooseImageTrain2, 'tStartRefresh')  # time at next scr refresh
                chooseImageTrain2.setAutoDraw(True)
            if chooseImageTrain2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > chooseImageTrain2.tStartRefresh + 7-frameTolerance:
                    # keep track of stop time/frame for later
                    chooseImageTrain2.tStop = t  # not accounting for scr refresh
                    chooseImageTrain2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(chooseImageTrain2, 'tStopRefresh')  # time at next scr refresh
                    chooseImageTrain2.setAutoDraw(False)
            
            # *train2F* updates
            if train2F.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                train2F.frameNStart = frameN  # exact frame index
                train2F.tStart = t  # local t and not account for scr refresh
                train2F.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(train2F, 'tStartRefresh')  # time at next scr refresh
                train2F.setAutoDraw(True)
            if train2F.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > train2F.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    train2F.tStop = t  # not accounting for scr refresh
                    train2F.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(train2F, 'tStopRefresh')  # time at next scr refresh
                    train2F.setAutoDraw(False)
            
            # *train2J* updates
            if train2J.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                train2J.frameNStart = frameN  # exact frame index
                train2J.tStart = t  # local t and not account for scr refresh
                train2J.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(train2J, 'tStartRefresh')  # time at next scr refresh
                train2J.setAutoDraw(True)
            if train2J.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > train2J.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    train2J.tStop = t  # not accounting for scr refresh
                    train2J.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(train2J, 'tStopRefresh')  # time at next scr refresh
                    train2J.setAutoDraw(False)
            
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
        blocktest2.addData('correct2.started', correct2.tStartRefresh)
        blocktest2.addData('correct2.stopped', correct2.tStopRefresh)
        blocktest2.addData('incorrect2.started', incorrect2.tStartRefresh)
        blocktest2.addData('incorrect2.stopped', incorrect2.tStopRefresh)
        # check responses
        if train2Response.keys in ['', [], None]:  # No response was made
            train2Response.keys = None
        blocktest2.addData('train2Response.keys',train2Response.keys)
        if train2Response.keys != None:  # we had a response
            blocktest2.addData('train2Response.rt', train2Response.rt)
        blocktest2.addData('train2Response.started', train2Response.tStartRefresh)
        blocktest2.addData('train2Response.stopped', train2Response.tStopRefresh)
        blocktest2.addData('chooseImageTrain2.started', chooseImageTrain2.tStartRefresh)
        blocktest2.addData('chooseImageTrain2.stopped', chooseImageTrain2.tStopRefresh)
        blocktest2.addData('train2F.started', train2F.tStartRefresh)
        blocktest2.addData('train2F.stopped', train2F.tStopRefresh)
        blocktest2.addData('train2J.started', train2J.tStartRefresh)
        blocktest2.addData('train2J.stopped', train2J.tStopRefresh)
        # the Routine "trainquestions2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
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
testTrainInstrComponents = [skipTest1Instr, test1warning10, test1warning5, test1warning4, test1warning3, test1warning2, test1warning1]
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
    
    # *test1warning10* updates
    if test1warning10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test1warning10.frameNStart = frameN  # exact frame index
        test1warning10.tStart = t  # local t and not account for scr refresh
        test1warning10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test1warning10, 'tStartRefresh')  # time at next scr refresh
        test1warning10.setAutoDraw(True)
    if test1warning10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test1warning10.tStartRefresh + 300-frameTolerance:
            # keep track of stop time/frame for later
            test1warning10.tStop = t  # not accounting for scr refresh
            test1warning10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test1warning10, 'tStopRefresh')  # time at next scr refresh
            test1warning10.setAutoDraw(False)
    
    # *test1warning5* updates
    if test1warning5.status == NOT_STARTED and tThisFlip >= 300-frameTolerance:
        # keep track of start time/frame for later
        test1warning5.frameNStart = frameN  # exact frame index
        test1warning5.tStart = t  # local t and not account for scr refresh
        test1warning5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test1warning5, 'tStartRefresh')  # time at next scr refresh
        test1warning5.setAutoDraw(True)
    if test1warning5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test1warning5.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            test1warning5.tStop = t  # not accounting for scr refresh
            test1warning5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test1warning5, 'tStopRefresh')  # time at next scr refresh
            test1warning5.setAutoDraw(False)
    
    # *test1warning4* updates
    if test1warning4.status == NOT_STARTED and tThisFlip >= 360-frameTolerance:
        # keep track of start time/frame for later
        test1warning4.frameNStart = frameN  # exact frame index
        test1warning4.tStart = t  # local t and not account for scr refresh
        test1warning4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test1warning4, 'tStartRefresh')  # time at next scr refresh
        test1warning4.setAutoDraw(True)
    if test1warning4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test1warning4.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            test1warning4.tStop = t  # not accounting for scr refresh
            test1warning4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test1warning4, 'tStopRefresh')  # time at next scr refresh
            test1warning4.setAutoDraw(False)
    
    # *test1warning3* updates
    if test1warning3.status == NOT_STARTED and tThisFlip >= 420-frameTolerance:
        # keep track of start time/frame for later
        test1warning3.frameNStart = frameN  # exact frame index
        test1warning3.tStart = t  # local t and not account for scr refresh
        test1warning3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test1warning3, 'tStartRefresh')  # time at next scr refresh
        test1warning3.setAutoDraw(True)
    if test1warning3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test1warning3.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            test1warning3.tStop = t  # not accounting for scr refresh
            test1warning3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test1warning3, 'tStopRefresh')  # time at next scr refresh
            test1warning3.setAutoDraw(False)
    
    # *test1warning2* updates
    if test1warning2.status == NOT_STARTED and tThisFlip >= 480-frameTolerance:
        # keep track of start time/frame for later
        test1warning2.frameNStart = frameN  # exact frame index
        test1warning2.tStart = t  # local t and not account for scr refresh
        test1warning2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test1warning2, 'tStartRefresh')  # time at next scr refresh
        test1warning2.setAutoDraw(True)
    if test1warning2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test1warning2.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            test1warning2.tStop = t  # not accounting for scr refresh
            test1warning2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test1warning2, 'tStopRefresh')  # time at next scr refresh
            test1warning2.setAutoDraw(False)
    
    # *test1warning1* updates
    if test1warning1.status == NOT_STARTED and tThisFlip >= 540-frameTolerance:
        # keep track of start time/frame for later
        test1warning1.frameNStart = frameN  # exact frame index
        test1warning1.tStart = t  # local t and not account for scr refresh
        test1warning1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test1warning1, 'tStartRefresh')  # time at next scr refresh
        test1warning1.setAutoDraw(True)
    if test1warning1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test1warning1.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            test1warning1.tStop = t  # not accounting for scr refresh
            test1warning1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test1warning1, 'tStopRefresh')  # time at next scr refresh
            test1warning1.setAutoDraw(False)
    
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
# check responses
if skipTest1Instr.keys in ['', [], None]:  # No response was made
    skipTest1Instr.keys = None
thisExp.addData('skipTest1Instr.keys',skipTest1Instr.keys)
if skipTest1Instr.keys != None:  # we had a response
    thisExp.addData('skipTest1Instr.rt', skipTest1Instr.rt)
thisExp.addData('skipTest1Instr.started', skipTest1Instr.tStartRefresh)
thisExp.addData('skipTest1Instr.stopped', skipTest1Instr.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('test1warning10.started', test1warning10.tStartRefresh)
thisExp.addData('test1warning10.stopped', test1warning10.tStopRefresh)
thisExp.addData('test1warning5.started', test1warning5.tStartRefresh)
thisExp.addData('test1warning5.stopped', test1warning5.tStopRefresh)
thisExp.addData('test1warning4.started', test1warning4.tStartRefresh)
thisExp.addData('test1warning4.stopped', test1warning4.tStopRefresh)
thisExp.addData('test1warning3.started', test1warning3.tStartRefresh)
thisExp.addData('test1warning3.stopped', test1warning3.tStopRefresh)
thisExp.addData('test1warning2.started', test1warning2.tStartRefresh)
thisExp.addData('test1warning2.stopped', test1warning2.tStopRefresh)
thisExp.addData('test1warning1.started', test1warning1.tStartRefresh)
thisExp.addData('test1warning1.stopped', test1warning1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
test1Loop = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('aoiConditions\\test1Conditions.xlsx'),
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
    # update component parameters for each repeat
    test1Audio1.setSound(firstAudio, hamming=True)
    test1Audio1.setVolume(1, log=False)
    test1Audio1Sound.setImage('sound.png')
    test1Audio1Mute.setImage('mute.png')
    test1Audio2.setSound(secondAudio, hamming=True)
    test1Audio2.setVolume(1, log=False)
    test1Audio2Mute1.setImage('mute.png')
    test1Audio2Sound.setImage('sound.png')
    test1Audio2Mute2.setImage('mute.png')
    test1Response.keys = []
    test1Response.rt = []
    _test1Response_allKeys = []
    test1Image.setImage(imageLoc)
    # keep track of which components have finished
    test1Components = [test1Audio1, test1Audio1Sound, test1Audio1Mute, test1Audio2, test1Audio2Mute1, test1Audio2Sound, test1Audio2Mute2, test1Response, test1Image, test1F, test1J, test1Instr]
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
    while continueRoutine:
        # get current time
        t = test1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=test1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop test1Audio1
        if test1Audio1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            test1Audio1.frameNStart = frameN  # exact frame index
            test1Audio1.tStart = t  # local t and not account for scr refresh
            test1Audio1.tStartRefresh = tThisFlipGlobal  # on global time
            test1Audio1.play(when=win)  # sync with win flip
        
        # *test1Audio1Sound* updates
        if test1Audio1Sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test1Audio1Sound.frameNStart = frameN  # exact frame index
            test1Audio1Sound.tStart = t  # local t and not account for scr refresh
            test1Audio1Sound.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test1Audio1Sound, 'tStartRefresh')  # time at next scr refresh
            test1Audio1Sound.setAutoDraw(True)
        if test1Audio1Sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test1Audio1Sound.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                test1Audio1Sound.tStop = t  # not accounting for scr refresh
                test1Audio1Sound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test1Audio1Sound, 'tStopRefresh')  # time at next scr refresh
                test1Audio1Sound.setAutoDraw(False)
        
        # *test1Audio1Mute* updates
        if test1Audio1Mute.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            test1Audio1Mute.frameNStart = frameN  # exact frame index
            test1Audio1Mute.tStart = t  # local t and not account for scr refresh
            test1Audio1Mute.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test1Audio1Mute, 'tStartRefresh')  # time at next scr refresh
            test1Audio1Mute.setAutoDraw(True)
        if test1Audio1Mute.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test1Audio1Mute.tStartRefresh + 9-frameTolerance:
                # keep track of stop time/frame for later
                test1Audio1Mute.tStop = t  # not accounting for scr refresh
                test1Audio1Mute.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test1Audio1Mute, 'tStopRefresh')  # time at next scr refresh
                test1Audio1Mute.setAutoDraw(False)
        # start/stop test1Audio2
        if test1Audio2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            test1Audio2.frameNStart = frameN  # exact frame index
            test1Audio2.tStart = t  # local t and not account for scr refresh
            test1Audio2.tStartRefresh = tThisFlipGlobal  # on global time
            test1Audio2.play(when=win)  # sync with win flip
        
        # *test1Audio2Mute1* updates
        if test1Audio2Mute1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test1Audio2Mute1.frameNStart = frameN  # exact frame index
            test1Audio2Mute1.tStart = t  # local t and not account for scr refresh
            test1Audio2Mute1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test1Audio2Mute1, 'tStartRefresh')  # time at next scr refresh
            test1Audio2Mute1.setAutoDraw(True)
        if test1Audio2Mute1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test1Audio2Mute1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                test1Audio2Mute1.tStop = t  # not accounting for scr refresh
                test1Audio2Mute1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test1Audio2Mute1, 'tStopRefresh')  # time at next scr refresh
                test1Audio2Mute1.setAutoDraw(False)
        
        # *test1Audio2Sound* updates
        if test1Audio2Sound.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            test1Audio2Sound.frameNStart = frameN  # exact frame index
            test1Audio2Sound.tStart = t  # local t and not account for scr refresh
            test1Audio2Sound.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test1Audio2Sound, 'tStartRefresh')  # time at next scr refresh
            test1Audio2Sound.setAutoDraw(True)
        if test1Audio2Sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test1Audio2Sound.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                test1Audio2Sound.tStop = t  # not accounting for scr refresh
                test1Audio2Sound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test1Audio2Sound, 'tStopRefresh')  # time at next scr refresh
                test1Audio2Sound.setAutoDraw(False)
        
        # *test1Audio2Mute2* updates
        if test1Audio2Mute2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            test1Audio2Mute2.frameNStart = frameN  # exact frame index
            test1Audio2Mute2.tStart = t  # local t and not account for scr refresh
            test1Audio2Mute2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test1Audio2Mute2, 'tStartRefresh')  # time at next scr refresh
            test1Audio2Mute2.setAutoDraw(True)
        if test1Audio2Mute2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test1Audio2Mute2.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                test1Audio2Mute2.tStop = t  # not accounting for scr refresh
                test1Audio2Mute2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test1Audio2Mute2, 'tStopRefresh')  # time at next scr refresh
                test1Audio2Mute2.setAutoDraw(False)
        
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
        
        # *test1F* updates
        if test1F.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test1F.frameNStart = frameN  # exact frame index
            test1F.tStart = t  # local t and not account for scr refresh
            test1F.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test1F, 'tStartRefresh')  # time at next scr refresh
            test1F.setAutoDraw(True)
        if test1F.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test1F.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                test1F.tStop = t  # not accounting for scr refresh
                test1F.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test1F, 'tStopRefresh')  # time at next scr refresh
                test1F.setAutoDraw(False)
        
        # *test1J* updates
        if test1J.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test1J.frameNStart = frameN  # exact frame index
            test1J.tStart = t  # local t and not account for scr refresh
            test1J.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test1J, 'tStartRefresh')  # time at next scr refresh
            test1J.setAutoDraw(True)
        if test1J.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test1J.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                test1J.tStop = t  # not accounting for scr refresh
                test1J.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test1J, 'tStopRefresh')  # time at next scr refresh
                test1J.setAutoDraw(False)
        
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
            if tThisFlipGlobal > test1Instr.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                test1Instr.tStop = t  # not accounting for scr refresh
                test1Instr.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test1Instr, 'tStopRefresh')  # time at next scr refresh
                test1Instr.setAutoDraw(False)
        
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
    test1Audio1.stop()  # ensure sound has stopped at end of routine
    test1Loop.addData('test1Audio1.started', test1Audio1.tStartRefresh)
    test1Loop.addData('test1Audio1.stopped', test1Audio1.tStopRefresh)
    test1Loop.addData('test1Audio1Sound.started', test1Audio1Sound.tStartRefresh)
    test1Loop.addData('test1Audio1Sound.stopped', test1Audio1Sound.tStopRefresh)
    test1Loop.addData('test1Audio1Mute.started', test1Audio1Mute.tStartRefresh)
    test1Loop.addData('test1Audio1Mute.stopped', test1Audio1Mute.tStopRefresh)
    test1Audio2.stop()  # ensure sound has stopped at end of routine
    test1Loop.addData('test1Audio2.started', test1Audio2.tStartRefresh)
    test1Loop.addData('test1Audio2.stopped', test1Audio2.tStopRefresh)
    test1Loop.addData('test1Audio2Mute1.started', test1Audio2Mute1.tStartRefresh)
    test1Loop.addData('test1Audio2Mute1.stopped', test1Audio2Mute1.tStopRefresh)
    test1Loop.addData('test1Audio2Sound.started', test1Audio2Sound.tStartRefresh)
    test1Loop.addData('test1Audio2Sound.stopped', test1Audio2Sound.tStopRefresh)
    test1Loop.addData('test1Audio2Mute2.started', test1Audio2Mute2.tStartRefresh)
    test1Loop.addData('test1Audio2Mute2.stopped', test1Audio2Mute2.tStopRefresh)
    # check responses
    if test1Response.keys in ['', [], None]:  # No response was made
        test1Response.keys = None
    test1Loop.addData('test1Response.keys',test1Response.keys)
    if test1Response.keys != None:  # we had a response
        test1Loop.addData('test1Response.rt', test1Response.rt)
    test1Loop.addData('test1Response.started', test1Response.tStartRefresh)
    test1Loop.addData('test1Response.stopped', test1Response.tStopRefresh)
    test1Loop.addData('test1Image.started', test1Image.tStartRefresh)
    test1Loop.addData('test1Image.stopped', test1Image.tStopRefresh)
    test1Loop.addData('test1F.started', test1F.tStartRefresh)
    test1Loop.addData('test1F.stopped', test1F.tStopRefresh)
    test1Loop.addData('test1J.started', test1J.tStartRefresh)
    test1Loop.addData('test1J.stopped', test1J.tStopRefresh)
    test1Loop.addData('test1Instr.started', test1Instr.tStartRefresh)
    test1Loop.addData('test1Instr.stopped', test1Instr.tStopRefresh)
    # the Routine "test1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'test1Loop'


# ------Prepare to start Routine "testNovel1Instr"-------
continueRoutine = True
routineTimer.add(600.000000)
# update component parameters for each repeat
skipTest2Instr.keys = []
skipTest2Instr.rt = []
_skipTest2Instr_allKeys = []
# keep track of which components have finished
testNovel1InstrComponents = [skipTest2Instr, test2warning10, test2warning5, test2warning4, test2warning3, test2warning2, test2warning1]
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
    
    # *test2warning10* updates
    if test2warning10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test2warning10.frameNStart = frameN  # exact frame index
        test2warning10.tStart = t  # local t and not account for scr refresh
        test2warning10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test2warning10, 'tStartRefresh')  # time at next scr refresh
        test2warning10.setAutoDraw(True)
    if test2warning10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test2warning10.tStartRefresh + 300-frameTolerance:
            # keep track of stop time/frame for later
            test2warning10.tStop = t  # not accounting for scr refresh
            test2warning10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test2warning10, 'tStopRefresh')  # time at next scr refresh
            test2warning10.setAutoDraw(False)
    
    # *test2warning5* updates
    if test2warning5.status == NOT_STARTED and tThisFlip >= 300-frameTolerance:
        # keep track of start time/frame for later
        test2warning5.frameNStart = frameN  # exact frame index
        test2warning5.tStart = t  # local t and not account for scr refresh
        test2warning5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test2warning5, 'tStartRefresh')  # time at next scr refresh
        test2warning5.setAutoDraw(True)
    if test2warning5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test2warning5.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            test2warning5.tStop = t  # not accounting for scr refresh
            test2warning5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test2warning5, 'tStopRefresh')  # time at next scr refresh
            test2warning5.setAutoDraw(False)
    
    # *test2warning4* updates
    if test2warning4.status == NOT_STARTED and tThisFlip >= 360-frameTolerance:
        # keep track of start time/frame for later
        test2warning4.frameNStart = frameN  # exact frame index
        test2warning4.tStart = t  # local t and not account for scr refresh
        test2warning4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test2warning4, 'tStartRefresh')  # time at next scr refresh
        test2warning4.setAutoDraw(True)
    if test2warning4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test2warning4.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            test2warning4.tStop = t  # not accounting for scr refresh
            test2warning4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test2warning4, 'tStopRefresh')  # time at next scr refresh
            test2warning4.setAutoDraw(False)
    
    # *test2warning3* updates
    if test2warning3.status == NOT_STARTED and tThisFlip >= 420-frameTolerance:
        # keep track of start time/frame for later
        test2warning3.frameNStart = frameN  # exact frame index
        test2warning3.tStart = t  # local t and not account for scr refresh
        test2warning3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test2warning3, 'tStartRefresh')  # time at next scr refresh
        test2warning3.setAutoDraw(True)
    if test2warning3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test2warning3.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            test2warning3.tStop = t  # not accounting for scr refresh
            test2warning3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test2warning3, 'tStopRefresh')  # time at next scr refresh
            test2warning3.setAutoDraw(False)
    
    # *test2warning2* updates
    if test2warning2.status == NOT_STARTED and tThisFlip >= 480-frameTolerance:
        # keep track of start time/frame for later
        test2warning2.frameNStart = frameN  # exact frame index
        test2warning2.tStart = t  # local t and not account for scr refresh
        test2warning2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test2warning2, 'tStartRefresh')  # time at next scr refresh
        test2warning2.setAutoDraw(True)
    if test2warning2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test2warning2.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            test2warning2.tStop = t  # not accounting for scr refresh
            test2warning2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test2warning2, 'tStopRefresh')  # time at next scr refresh
            test2warning2.setAutoDraw(False)
    
    # *test2warning1* updates
    if test2warning1.status == NOT_STARTED and tThisFlip >= 540-frameTolerance:
        # keep track of start time/frame for later
        test2warning1.frameNStart = frameN  # exact frame index
        test2warning1.tStart = t  # local t and not account for scr refresh
        test2warning1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test2warning1, 'tStartRefresh')  # time at next scr refresh
        test2warning1.setAutoDraw(True)
    if test2warning1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test2warning1.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            test2warning1.tStop = t  # not accounting for scr refresh
            test2warning1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test2warning1, 'tStopRefresh')  # time at next scr refresh
            test2warning1.setAutoDraw(False)
    
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
# check responses
if skipTest2Instr.keys in ['', [], None]:  # No response was made
    skipTest2Instr.keys = None
thisExp.addData('skipTest2Instr.keys',skipTest2Instr.keys)
if skipTest2Instr.keys != None:  # we had a response
    thisExp.addData('skipTest2Instr.rt', skipTest2Instr.rt)
thisExp.addData('skipTest2Instr.started', skipTest2Instr.tStartRefresh)
thisExp.addData('skipTest2Instr.stopped', skipTest2Instr.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('test2warning10.started', test2warning10.tStartRefresh)
thisExp.addData('test2warning10.stopped', test2warning10.tStopRefresh)
thisExp.addData('test2warning5.started', test2warning5.tStartRefresh)
thisExp.addData('test2warning5.stopped', test2warning5.tStopRefresh)
thisExp.addData('test2warning4.started', test2warning4.tStartRefresh)
thisExp.addData('test2warning4.stopped', test2warning4.tStopRefresh)
thisExp.addData('test2warning3.started', test2warning3.tStartRefresh)
thisExp.addData('test2warning3.stopped', test2warning3.tStopRefresh)
thisExp.addData('test2warning2.started', test2warning2.tStartRefresh)
thisExp.addData('test2warning2.stopped', test2warning2.tStopRefresh)
thisExp.addData('test2warning1.started', test2warning1.tStartRefresh)
thisExp.addData('test2warning1.stopped', test2warning1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
test2Loop = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('aoiConditions\\test2Conditions.xlsx'),
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
    # update component parameters for each repeat
    test2Audio1.setSound(firstAudio, hamming=True)
    test2Audio1.setVolume(1, log=False)
    test2Audio1Sound.setImage('sound.png')
    test1Audio2Mute.setImage('mute.png')
    test2Audio2.setSound(secondAudio, hamming=True)
    test2Audio2.setVolume(1, log=False)
    test2Audio2Mute1.setImage('mute.png')
    test2Audio2Sound.setImage('sound.png')
    test2Response.keys = []
    test2Response.rt = []
    _test2Response_allKeys = []
    test2Image.setImage(imageLoc)
    # keep track of which components have finished
    test2Components = [test2Audio1, test2Audio1Sound, test1Audio2Mute, test2Audio2, test2Audio2Mute1, test2Audio2Sound, test2Audio2Mute2, test2Response, test2Image, test2F, test2J, test2Instr]
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
    while continueRoutine:
        # get current time
        t = test2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=test2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop test2Audio1
        if test2Audio1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test2Audio1.frameNStart = frameN  # exact frame index
            test2Audio1.tStart = t  # local t and not account for scr refresh
            test2Audio1.tStartRefresh = tThisFlipGlobal  # on global time
            test2Audio1.play(when=win)  # sync with win flip
        
        # *test2Audio1Sound* updates
        if test2Audio1Sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test2Audio1Sound.frameNStart = frameN  # exact frame index
            test2Audio1Sound.tStart = t  # local t and not account for scr refresh
            test2Audio1Sound.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test2Audio1Sound, 'tStartRefresh')  # time at next scr refresh
            test2Audio1Sound.setAutoDraw(True)
        if test2Audio1Sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test2Audio1Sound.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                test2Audio1Sound.tStop = t  # not accounting for scr refresh
                test2Audio1Sound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test2Audio1Sound, 'tStopRefresh')  # time at next scr refresh
                test2Audio1Sound.setAutoDraw(False)
        
        # *test1Audio2Mute* updates
        if test1Audio2Mute.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            test1Audio2Mute.frameNStart = frameN  # exact frame index
            test1Audio2Mute.tStart = t  # local t and not account for scr refresh
            test1Audio2Mute.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test1Audio2Mute, 'tStartRefresh')  # time at next scr refresh
            test1Audio2Mute.setAutoDraw(True)
        if test1Audio2Mute.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test1Audio2Mute.tStartRefresh + 9-frameTolerance:
                # keep track of stop time/frame for later
                test1Audio2Mute.tStop = t  # not accounting for scr refresh
                test1Audio2Mute.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test1Audio2Mute, 'tStopRefresh')  # time at next scr refresh
                test1Audio2Mute.setAutoDraw(False)
        # start/stop test2Audio2
        if test2Audio2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            test2Audio2.frameNStart = frameN  # exact frame index
            test2Audio2.tStart = t  # local t and not account for scr refresh
            test2Audio2.tStartRefresh = tThisFlipGlobal  # on global time
            test2Audio2.play(when=win)  # sync with win flip
        
        # *test2Audio2Mute1* updates
        if test2Audio2Mute1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test2Audio2Mute1.frameNStart = frameN  # exact frame index
            test2Audio2Mute1.tStart = t  # local t and not account for scr refresh
            test2Audio2Mute1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test2Audio2Mute1, 'tStartRefresh')  # time at next scr refresh
            test2Audio2Mute1.setAutoDraw(True)
        if test2Audio2Mute1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test2Audio2Mute1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                test2Audio2Mute1.tStop = t  # not accounting for scr refresh
                test2Audio2Mute1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test2Audio2Mute1, 'tStopRefresh')  # time at next scr refresh
                test2Audio2Mute1.setAutoDraw(False)
        
        # *test2Audio2Sound* updates
        if test2Audio2Sound.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            test2Audio2Sound.frameNStart = frameN  # exact frame index
            test2Audio2Sound.tStart = t  # local t and not account for scr refresh
            test2Audio2Sound.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test2Audio2Sound, 'tStartRefresh')  # time at next scr refresh
            test2Audio2Sound.setAutoDraw(True)
        if test2Audio2Sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test2Audio2Sound.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                test2Audio2Sound.tStop = t  # not accounting for scr refresh
                test2Audio2Sound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test2Audio2Sound, 'tStopRefresh')  # time at next scr refresh
                test2Audio2Sound.setAutoDraw(False)
        
        # *test2Audio2Mute2* updates
        if test2Audio2Mute2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            test2Audio2Mute2.frameNStart = frameN  # exact frame index
            test2Audio2Mute2.tStart = t  # local t and not account for scr refresh
            test2Audio2Mute2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test2Audio2Mute2, 'tStartRefresh')  # time at next scr refresh
            test2Audio2Mute2.setAutoDraw(True)
        if test2Audio2Mute2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test2Audio2Mute2.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                test2Audio2Mute2.tStop = t  # not accounting for scr refresh
                test2Audio2Mute2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test2Audio2Mute2, 'tStopRefresh')  # time at next scr refresh
                test2Audio2Mute2.setAutoDraw(False)
        
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
        
        # *test2F* updates
        if test2F.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test2F.frameNStart = frameN  # exact frame index
            test2F.tStart = t  # local t and not account for scr refresh
            test2F.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test2F, 'tStartRefresh')  # time at next scr refresh
            test2F.setAutoDraw(True)
        if test2F.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test2F.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                test2F.tStop = t  # not accounting for scr refresh
                test2F.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test2F, 'tStopRefresh')  # time at next scr refresh
                test2F.setAutoDraw(False)
        
        # *test2J* updates
        if test2J.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test2J.frameNStart = frameN  # exact frame index
            test2J.tStart = t  # local t and not account for scr refresh
            test2J.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test2J, 'tStartRefresh')  # time at next scr refresh
            test2J.setAutoDraw(True)
        if test2J.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test2J.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                test2J.tStop = t  # not accounting for scr refresh
                test2J.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test2J, 'tStopRefresh')  # time at next scr refresh
                test2J.setAutoDraw(False)
        
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
            if tThisFlipGlobal > test2Instr.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                test2Instr.tStop = t  # not accounting for scr refresh
                test2Instr.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test2Instr, 'tStopRefresh')  # time at next scr refresh
                test2Instr.setAutoDraw(False)
        
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
    test2Audio1.stop()  # ensure sound has stopped at end of routine
    test2Loop.addData('test2Audio1.started', test2Audio1.tStartRefresh)
    test2Loop.addData('test2Audio1.stopped', test2Audio1.tStopRefresh)
    test2Loop.addData('test2Audio1Sound.started', test2Audio1Sound.tStartRefresh)
    test2Loop.addData('test2Audio1Sound.stopped', test2Audio1Sound.tStopRefresh)
    test2Loop.addData('test1Audio2Mute.started', test1Audio2Mute.tStartRefresh)
    test2Loop.addData('test1Audio2Mute.stopped', test1Audio2Mute.tStopRefresh)
    test2Audio2.stop()  # ensure sound has stopped at end of routine
    test2Loop.addData('test2Audio2.started', test2Audio2.tStartRefresh)
    test2Loop.addData('test2Audio2.stopped', test2Audio2.tStopRefresh)
    test2Loop.addData('test2Audio2Mute1.started', test2Audio2Mute1.tStartRefresh)
    test2Loop.addData('test2Audio2Mute1.stopped', test2Audio2Mute1.tStopRefresh)
    test2Loop.addData('test2Audio2Sound.started', test2Audio2Sound.tStartRefresh)
    test2Loop.addData('test2Audio2Sound.stopped', test2Audio2Sound.tStopRefresh)
    test2Loop.addData('test2Audio2Mute2.started', test2Audio2Mute2.tStartRefresh)
    test2Loop.addData('test2Audio2Mute2.stopped', test2Audio2Mute2.tStopRefresh)
    # check responses
    if test2Response.keys in ['', [], None]:  # No response was made
        test2Response.keys = None
    test2Loop.addData('test2Response.keys',test2Response.keys)
    if test2Response.keys != None:  # we had a response
        test2Loop.addData('test2Response.rt', test2Response.rt)
    test2Loop.addData('test2Response.started', test2Response.tStartRefresh)
    test2Loop.addData('test2Response.stopped', test2Response.tStopRefresh)
    test2Loop.addData('test2Image.started', test2Image.tStartRefresh)
    test2Loop.addData('test2Image.stopped', test2Image.tStopRefresh)
    test2Loop.addData('test2F.started', test2F.tStartRefresh)
    test2Loop.addData('test2F.stopped', test2F.tStopRefresh)
    test2Loop.addData('test2J.started', test2J.tStartRefresh)
    test2Loop.addData('test2J.stopped', test2J.tStopRefresh)
    test2Loop.addData('test2Instr.started', test2Instr.tStartRefresh)
    test2Loop.addData('test2Instr.stopped', test2Instr.tStopRefresh)
    # the Routine "test2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'test2Loop'


# ------Prepare to start Routine "testNovel2Instr"-------
continueRoutine = True
routineTimer.add(600.000000)
# update component parameters for each repeat
skipTest3Instr.keys = []
skipTest3Instr.rt = []
_skipTest3Instr_allKeys = []
# keep track of which components have finished
testNovel2InstrComponents = [skipTest3Instr, test3warning10, test3warning5, test3warning4, test3warning3, test3warning2, test3warning1]
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
        theseKeys = skipTest3Instr.getKeys(keyList=None, waitRelease=False)
        _skipTest3Instr_allKeys.extend(theseKeys)
        if len(_skipTest3Instr_allKeys):
            skipTest3Instr.keys = _skipTest3Instr_allKeys[-1].name  # just the last key pressed
            skipTest3Instr.rt = _skipTest3Instr_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *test3warning10* updates
    if test3warning10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test3warning10.frameNStart = frameN  # exact frame index
        test3warning10.tStart = t  # local t and not account for scr refresh
        test3warning10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test3warning10, 'tStartRefresh')  # time at next scr refresh
        test3warning10.setAutoDraw(True)
    if test3warning10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test3warning10.tStartRefresh + 300-frameTolerance:
            # keep track of stop time/frame for later
            test3warning10.tStop = t  # not accounting for scr refresh
            test3warning10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test3warning10, 'tStopRefresh')  # time at next scr refresh
            test3warning10.setAutoDraw(False)
    
    # *test3warning5* updates
    if test3warning5.status == NOT_STARTED and tThisFlip >= 300-frameTolerance:
        # keep track of start time/frame for later
        test3warning5.frameNStart = frameN  # exact frame index
        test3warning5.tStart = t  # local t and not account for scr refresh
        test3warning5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test3warning5, 'tStartRefresh')  # time at next scr refresh
        test3warning5.setAutoDraw(True)
    if test3warning5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test3warning5.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            test3warning5.tStop = t  # not accounting for scr refresh
            test3warning5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test3warning5, 'tStopRefresh')  # time at next scr refresh
            test3warning5.setAutoDraw(False)
    
    # *test3warning4* updates
    if test3warning4.status == NOT_STARTED and tThisFlip >= 360-frameTolerance:
        # keep track of start time/frame for later
        test3warning4.frameNStart = frameN  # exact frame index
        test3warning4.tStart = t  # local t and not account for scr refresh
        test3warning4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test3warning4, 'tStartRefresh')  # time at next scr refresh
        test3warning4.setAutoDraw(True)
    if test3warning4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test3warning4.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            test3warning4.tStop = t  # not accounting for scr refresh
            test3warning4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test3warning4, 'tStopRefresh')  # time at next scr refresh
            test3warning4.setAutoDraw(False)
    
    # *test3warning3* updates
    if test3warning3.status == NOT_STARTED and tThisFlip >= 420-frameTolerance:
        # keep track of start time/frame for later
        test3warning3.frameNStart = frameN  # exact frame index
        test3warning3.tStart = t  # local t and not account for scr refresh
        test3warning3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test3warning3, 'tStartRefresh')  # time at next scr refresh
        test3warning3.setAutoDraw(True)
    if test3warning3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test3warning3.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            test3warning3.tStop = t  # not accounting for scr refresh
            test3warning3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test3warning3, 'tStopRefresh')  # time at next scr refresh
            test3warning3.setAutoDraw(False)
    
    # *test3warning2* updates
    if test3warning2.status == NOT_STARTED and tThisFlip >= 480-frameTolerance:
        # keep track of start time/frame for later
        test3warning2.frameNStart = frameN  # exact frame index
        test3warning2.tStart = t  # local t and not account for scr refresh
        test3warning2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test3warning2, 'tStartRefresh')  # time at next scr refresh
        test3warning2.setAutoDraw(True)
    if test3warning2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test3warning2.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            test3warning2.tStop = t  # not accounting for scr refresh
            test3warning2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test3warning2, 'tStopRefresh')  # time at next scr refresh
            test3warning2.setAutoDraw(False)
    
    # *test3warning1* updates
    if test3warning1.status == NOT_STARTED and tThisFlip >= 540-frameTolerance:
        # keep track of start time/frame for later
        test3warning1.frameNStart = frameN  # exact frame index
        test3warning1.tStart = t  # local t and not account for scr refresh
        test3warning1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test3warning1, 'tStartRefresh')  # time at next scr refresh
        test3warning1.setAutoDraw(True)
    if test3warning1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test3warning1.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            test3warning1.tStop = t  # not accounting for scr refresh
            test3warning1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test3warning1, 'tStopRefresh')  # time at next scr refresh
            test3warning1.setAutoDraw(False)
    
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
# check responses
if skipTest3Instr.keys in ['', [], None]:  # No response was made
    skipTest3Instr.keys = None
thisExp.addData('skipTest3Instr.keys',skipTest3Instr.keys)
if skipTest3Instr.keys != None:  # we had a response
    thisExp.addData('skipTest3Instr.rt', skipTest3Instr.rt)
thisExp.addData('skipTest3Instr.started', skipTest3Instr.tStartRefresh)
thisExp.addData('skipTest3Instr.stopped', skipTest3Instr.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('test3warning10.started', test3warning10.tStartRefresh)
thisExp.addData('test3warning10.stopped', test3warning10.tStopRefresh)
thisExp.addData('test3warning5.started', test3warning5.tStartRefresh)
thisExp.addData('test3warning5.stopped', test3warning5.tStopRefresh)
thisExp.addData('test3warning4.started', test3warning4.tStartRefresh)
thisExp.addData('test3warning4.stopped', test3warning4.tStopRefresh)
thisExp.addData('test3warning3.started', test3warning3.tStartRefresh)
thisExp.addData('test3warning3.stopped', test3warning3.tStopRefresh)
thisExp.addData('test3warning2.started', test3warning2.tStartRefresh)
thisExp.addData('test3warning2.stopped', test3warning2.tStopRefresh)
thisExp.addData('test3warning1.started', test3warning1.tStartRefresh)
thisExp.addData('test3warning1.stopped', test3warning1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
test3Loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('aoiConditions\\test3Conditions.xlsx'),
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
    # update component parameters for each repeat
    test3Audio1.setSound(firstAudio, hamming=True)
    test3Audio1.setVolume(1, log=False)
    test3Audio1Sound.setImage('sound.png')
    test3Audio1Mute.setImage('mute.png')
    test3Audio2.setSound(secondAudio, hamming=True)
    test3Audio2.setVolume(1, log=False)
    test3Audio2Mute1.setImage('mute.png')
    test3Audio2Sound.setImage('sound.png')
    test3Audio2Mute2.setImage('mute.png')
    test3Response.keys = []
    test3Response.rt = []
    _test3Response_allKeys = []
    test3Image.setImage(imageLoc)
    # keep track of which components have finished
    test3Components = [test3Audio1, test3Audio1Sound, test3Audio1Mute, test3Audio2, test3Audio2Mute1, test3Audio2Sound, test3Audio2Mute2, test3Response, test3Image, test3F, test3J, test3Instr]
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
    while continueRoutine:
        # get current time
        t = test3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=test3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop test3Audio1
        if test3Audio1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test3Audio1.frameNStart = frameN  # exact frame index
            test3Audio1.tStart = t  # local t and not account for scr refresh
            test3Audio1.tStartRefresh = tThisFlipGlobal  # on global time
            test3Audio1.play(when=win)  # sync with win flip
        
        # *test3Audio1Sound* updates
        if test3Audio1Sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test3Audio1Sound.frameNStart = frameN  # exact frame index
            test3Audio1Sound.tStart = t  # local t and not account for scr refresh
            test3Audio1Sound.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test3Audio1Sound, 'tStartRefresh')  # time at next scr refresh
            test3Audio1Sound.setAutoDraw(True)
        if test3Audio1Sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test3Audio1Sound.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                test3Audio1Sound.tStop = t  # not accounting for scr refresh
                test3Audio1Sound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test3Audio1Sound, 'tStopRefresh')  # time at next scr refresh
                test3Audio1Sound.setAutoDraw(False)
        
        # *test3Audio1Mute* updates
        if test3Audio1Mute.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            test3Audio1Mute.frameNStart = frameN  # exact frame index
            test3Audio1Mute.tStart = t  # local t and not account for scr refresh
            test3Audio1Mute.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test3Audio1Mute, 'tStartRefresh')  # time at next scr refresh
            test3Audio1Mute.setAutoDraw(True)
        if test3Audio1Mute.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test3Audio1Mute.tStartRefresh + 9-frameTolerance:
                # keep track of stop time/frame for later
                test3Audio1Mute.tStop = t  # not accounting for scr refresh
                test3Audio1Mute.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test3Audio1Mute, 'tStopRefresh')  # time at next scr refresh
                test3Audio1Mute.setAutoDraw(False)
        # start/stop test3Audio2
        if test3Audio2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            test3Audio2.frameNStart = frameN  # exact frame index
            test3Audio2.tStart = t  # local t and not account for scr refresh
            test3Audio2.tStartRefresh = tThisFlipGlobal  # on global time
            test3Audio2.play(when=win)  # sync with win flip
        
        # *test3Audio2Mute1* updates
        if test3Audio2Mute1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test3Audio2Mute1.frameNStart = frameN  # exact frame index
            test3Audio2Mute1.tStart = t  # local t and not account for scr refresh
            test3Audio2Mute1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test3Audio2Mute1, 'tStartRefresh')  # time at next scr refresh
            test3Audio2Mute1.setAutoDraw(True)
        if test3Audio2Mute1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test3Audio2Mute1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                test3Audio2Mute1.tStop = t  # not accounting for scr refresh
                test3Audio2Mute1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test3Audio2Mute1, 'tStopRefresh')  # time at next scr refresh
                test3Audio2Mute1.setAutoDraw(False)
        
        # *test3Audio2Sound* updates
        if test3Audio2Sound.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            test3Audio2Sound.frameNStart = frameN  # exact frame index
            test3Audio2Sound.tStart = t  # local t and not account for scr refresh
            test3Audio2Sound.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test3Audio2Sound, 'tStartRefresh')  # time at next scr refresh
            test3Audio2Sound.setAutoDraw(True)
        if test3Audio2Sound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test3Audio2Sound.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                test3Audio2Sound.tStop = t  # not accounting for scr refresh
                test3Audio2Sound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test3Audio2Sound, 'tStopRefresh')  # time at next scr refresh
                test3Audio2Sound.setAutoDraw(False)
        
        # *test3Audio2Mute2* updates
        if test3Audio2Mute2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            test3Audio2Mute2.frameNStart = frameN  # exact frame index
            test3Audio2Mute2.tStart = t  # local t and not account for scr refresh
            test3Audio2Mute2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test3Audio2Mute2, 'tStartRefresh')  # time at next scr refresh
            test3Audio2Mute2.setAutoDraw(True)
        if test3Audio2Mute2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test3Audio2Mute2.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                test3Audio2Mute2.tStop = t  # not accounting for scr refresh
                test3Audio2Mute2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test3Audio2Mute2, 'tStopRefresh')  # time at next scr refresh
                test3Audio2Mute2.setAutoDraw(False)
        
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
        
        # *test3F* updates
        if test3F.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test3F.frameNStart = frameN  # exact frame index
            test3F.tStart = t  # local t and not account for scr refresh
            test3F.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test3F, 'tStartRefresh')  # time at next scr refresh
            test3F.setAutoDraw(True)
        if test3F.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test3F.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                test3F.tStop = t  # not accounting for scr refresh
                test3F.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test3F, 'tStopRefresh')  # time at next scr refresh
                test3F.setAutoDraw(False)
        
        # *test3J* updates
        if test3J.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test3J.frameNStart = frameN  # exact frame index
            test3J.tStart = t  # local t and not account for scr refresh
            test3J.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test3J, 'tStartRefresh')  # time at next scr refresh
            test3J.setAutoDraw(True)
        if test3J.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test3J.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                test3J.tStop = t  # not accounting for scr refresh
                test3J.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test3J, 'tStopRefresh')  # time at next scr refresh
                test3J.setAutoDraw(False)
        
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
            if tThisFlipGlobal > test3Instr.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                test3Instr.tStop = t  # not accounting for scr refresh
                test3Instr.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test3Instr, 'tStopRefresh')  # time at next scr refresh
                test3Instr.setAutoDraw(False)
        
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
    test3Audio1.stop()  # ensure sound has stopped at end of routine
    test3Loop.addData('test3Audio1.started', test3Audio1.tStartRefresh)
    test3Loop.addData('test3Audio1.stopped', test3Audio1.tStopRefresh)
    test3Loop.addData('test3Audio1Sound.started', test3Audio1Sound.tStartRefresh)
    test3Loop.addData('test3Audio1Sound.stopped', test3Audio1Sound.tStopRefresh)
    test3Loop.addData('test3Audio1Mute.started', test3Audio1Mute.tStartRefresh)
    test3Loop.addData('test3Audio1Mute.stopped', test3Audio1Mute.tStopRefresh)
    test3Audio2.stop()  # ensure sound has stopped at end of routine
    test3Loop.addData('test3Audio2.started', test3Audio2.tStartRefresh)
    test3Loop.addData('test3Audio2.stopped', test3Audio2.tStopRefresh)
    test3Loop.addData('test3Audio2Mute1.started', test3Audio2Mute1.tStartRefresh)
    test3Loop.addData('test3Audio2Mute1.stopped', test3Audio2Mute1.tStopRefresh)
    test3Loop.addData('test3Audio2Sound.started', test3Audio2Sound.tStartRefresh)
    test3Loop.addData('test3Audio2Sound.stopped', test3Audio2Sound.tStopRefresh)
    test3Loop.addData('test3Audio2Mute2.started', test3Audio2Mute2.tStartRefresh)
    test3Loop.addData('test3Audio2Mute2.stopped', test3Audio2Mute2.tStopRefresh)
    # check responses
    if test3Response.keys in ['', [], None]:  # No response was made
        test3Response.keys = None
    test3Loop.addData('test3Response.keys',test3Response.keys)
    if test3Response.keys != None:  # we had a response
        test3Loop.addData('test3Response.rt', test3Response.rt)
    test3Loop.addData('test3Response.started', test3Response.tStartRefresh)
    test3Loop.addData('test3Response.stopped', test3Response.tStopRefresh)
    test3Loop.addData('test3Image.started', test3Image.tStartRefresh)
    test3Loop.addData('test3Image.stopped', test3Image.tStopRefresh)
    test3Loop.addData('test3F.started', test3F.tStartRefresh)
    test3Loop.addData('test3F.stopped', test3F.tStopRefresh)
    test3Loop.addData('test3J.started', test3J.tStartRefresh)
    test3Loop.addData('test3J.stopped', test3J.tStopRefresh)
    test3Loop.addData('test3Instr.started', test3Instr.tStartRefresh)
    test3Loop.addData('test3Instr.stopped', test3Instr.tStopRefresh)
    # the Routine "test3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'test3Loop'


# ------Prepare to start Routine "postTestInstr"-------
continueRoutine = True
routineTimer.add(600.000000)
# update component parameters for each repeat
skipPostTestInstr.keys = []
skipPostTestInstr.rt = []
_skipPostTestInstr_allKeys = []
# keep track of which components have finished
postTestInstrComponents = [skipPostTestInstr, postTestWarning10, postTestWarning5, postTestWarning4, postTestWarning3, postTestWarning2, postTestWarning1]
for thisComponent in postTestInstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
postTestInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "postTestInstr"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = postTestInstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=postTestInstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *skipPostTestInstr* updates
    waitOnFlip = False
    if skipPostTestInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skipPostTestInstr.frameNStart = frameN  # exact frame index
        skipPostTestInstr.tStart = t  # local t and not account for scr refresh
        skipPostTestInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skipPostTestInstr, 'tStartRefresh')  # time at next scr refresh
        skipPostTestInstr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skipPostTestInstr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skipPostTestInstr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skipPostTestInstr.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > skipPostTestInstr.tStartRefresh + 600-frameTolerance:
            # keep track of stop time/frame for later
            skipPostTestInstr.tStop = t  # not accounting for scr refresh
            skipPostTestInstr.frameNStop = frameN  # exact frame index
            win.timeOnFlip(skipPostTestInstr, 'tStopRefresh')  # time at next scr refresh
            skipPostTestInstr.status = FINISHED
    if skipPostTestInstr.status == STARTED and not waitOnFlip:
        theseKeys = skipPostTestInstr.getKeys(keyList=None, waitRelease=False)
        _skipPostTestInstr_allKeys.extend(theseKeys)
        if len(_skipPostTestInstr_allKeys):
            skipPostTestInstr.keys = _skipPostTestInstr_allKeys[-1].name  # just the last key pressed
            skipPostTestInstr.rt = _skipPostTestInstr_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *postTestWarning10* updates
    if postTestWarning10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        postTestWarning10.frameNStart = frameN  # exact frame index
        postTestWarning10.tStart = t  # local t and not account for scr refresh
        postTestWarning10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(postTestWarning10, 'tStartRefresh')  # time at next scr refresh
        postTestWarning10.setAutoDraw(True)
    if postTestWarning10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > postTestWarning10.tStartRefresh + 300-frameTolerance:
            # keep track of stop time/frame for later
            postTestWarning10.tStop = t  # not accounting for scr refresh
            postTestWarning10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(postTestWarning10, 'tStopRefresh')  # time at next scr refresh
            postTestWarning10.setAutoDraw(False)
    
    # *postTestWarning5* updates
    if postTestWarning5.status == NOT_STARTED and tThisFlip >= 300-frameTolerance:
        # keep track of start time/frame for later
        postTestWarning5.frameNStart = frameN  # exact frame index
        postTestWarning5.tStart = t  # local t and not account for scr refresh
        postTestWarning5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(postTestWarning5, 'tStartRefresh')  # time at next scr refresh
        postTestWarning5.setAutoDraw(True)
    if postTestWarning5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > postTestWarning5.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            postTestWarning5.tStop = t  # not accounting for scr refresh
            postTestWarning5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(postTestWarning5, 'tStopRefresh')  # time at next scr refresh
            postTestWarning5.setAutoDraw(False)
    
    # *postTestWarning4* updates
    if postTestWarning4.status == NOT_STARTED and tThisFlip >= 360-frameTolerance:
        # keep track of start time/frame for later
        postTestWarning4.frameNStart = frameN  # exact frame index
        postTestWarning4.tStart = t  # local t and not account for scr refresh
        postTestWarning4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(postTestWarning4, 'tStartRefresh')  # time at next scr refresh
        postTestWarning4.setAutoDraw(True)
    if postTestWarning4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > postTestWarning4.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            postTestWarning4.tStop = t  # not accounting for scr refresh
            postTestWarning4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(postTestWarning4, 'tStopRefresh')  # time at next scr refresh
            postTestWarning4.setAutoDraw(False)
    
    # *postTestWarning3* updates
    if postTestWarning3.status == NOT_STARTED and tThisFlip >= 420-frameTolerance:
        # keep track of start time/frame for later
        postTestWarning3.frameNStart = frameN  # exact frame index
        postTestWarning3.tStart = t  # local t and not account for scr refresh
        postTestWarning3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(postTestWarning3, 'tStartRefresh')  # time at next scr refresh
        postTestWarning3.setAutoDraw(True)
    if postTestWarning3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > postTestWarning3.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            postTestWarning3.tStop = t  # not accounting for scr refresh
            postTestWarning3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(postTestWarning3, 'tStopRefresh')  # time at next scr refresh
            postTestWarning3.setAutoDraw(False)
    
    # *postTestWarning2* updates
    if postTestWarning2.status == NOT_STARTED and tThisFlip >= 480-frameTolerance:
        # keep track of start time/frame for later
        postTestWarning2.frameNStart = frameN  # exact frame index
        postTestWarning2.tStart = t  # local t and not account for scr refresh
        postTestWarning2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(postTestWarning2, 'tStartRefresh')  # time at next scr refresh
        postTestWarning2.setAutoDraw(True)
    if postTestWarning2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > postTestWarning2.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            postTestWarning2.tStop = t  # not accounting for scr refresh
            postTestWarning2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(postTestWarning2, 'tStopRefresh')  # time at next scr refresh
            postTestWarning2.setAutoDraw(False)
    
    # *postTestWarning1* updates
    if postTestWarning1.status == NOT_STARTED and tThisFlip >= 540-frameTolerance:
        # keep track of start time/frame for later
        postTestWarning1.frameNStart = frameN  # exact frame index
        postTestWarning1.tStart = t  # local t and not account for scr refresh
        postTestWarning1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(postTestWarning1, 'tStartRefresh')  # time at next scr refresh
        postTestWarning1.setAutoDraw(True)
    if postTestWarning1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > postTestWarning1.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            postTestWarning1.tStop = t  # not accounting for scr refresh
            postTestWarning1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(postTestWarning1, 'tStopRefresh')  # time at next scr refresh
            postTestWarning1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postTestInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "postTestInstr"-------
for thisComponent in postTestInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if skipPostTestInstr.keys in ['', [], None]:  # No response was made
    skipPostTestInstr.keys = None
thisExp.addData('skipPostTestInstr.keys',skipPostTestInstr.keys)
if skipPostTestInstr.keys != None:  # we had a response
    thisExp.addData('skipPostTestInstr.rt', skipPostTestInstr.rt)
thisExp.addData('skipPostTestInstr.started', skipPostTestInstr.tStartRefresh)
thisExp.addData('skipPostTestInstr.stopped', skipPostTestInstr.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('postTestWarning10.started', postTestWarning10.tStartRefresh)
thisExp.addData('postTestWarning10.stopped', postTestWarning10.tStopRefresh)
thisExp.addData('postTestWarning5.started', postTestWarning5.tStartRefresh)
thisExp.addData('postTestWarning5.stopped', postTestWarning5.tStopRefresh)
thisExp.addData('postTestWarning4.started', postTestWarning4.tStartRefresh)
thisExp.addData('postTestWarning4.stopped', postTestWarning4.tStopRefresh)
thisExp.addData('postTestWarning3.started', postTestWarning3.tStartRefresh)
thisExp.addData('postTestWarning3.stopped', postTestWarning3.tStopRefresh)
thisExp.addData('postTestWarning2.started', postTestWarning2.tStartRefresh)
thisExp.addData('postTestWarning2.stopped', postTestWarning2.tStopRefresh)
thisExp.addData('postTestWarning1.started', postTestWarning1.tStartRefresh)
thisExp.addData('postTestWarning1.stopped', postTestWarning1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
postTestLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('postTestConditions.xlsx'),
    seed=None, name='postTestLoop')
thisExp.addLoop(postTestLoop)  # add the loop to the experiment
thisPostTestLoop = postTestLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPostTestLoop.rgb)
if thisPostTestLoop != None:
    for paramName in thisPostTestLoop:
        exec('{} = thisPostTestLoop[paramName]'.format(paramName))

for thisPostTestLoop in postTestLoop:
    currentLoop = postTestLoop
    # abbreviate parameter names if possible (e.g. rgb = thisPostTestLoop.rgb)
    if thisPostTestLoop != None:
        for paramName in thisPostTestLoop:
            exec('{} = thisPostTestLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "posttest"-------
    continueRoutine = True
    # update component parameters for each repeat
    postTestResponse.keys = []
    postTestResponse.rt = []
    _postTestResponse_allKeys = []
    postTestAudio1.setSound(audioA, hamming=True)
    postTestAudio1.setVolume(1, log=False)
    postTestAudio2.setSound(audioX, hamming=True)
    postTestAudio2.setVolume(1, log=False)
    postTestAudio3.setSound(audioB, hamming=False)
    postTestAudio3.setVolume(1, log=False)
    # keep track of which components have finished
    posttestComponents = [postTestResponse, postTestAudio1, fSound, fMute, postTestAudio2, xMute1, xSound, xMute2, postTestAudio3, jMute1, jSound, jMute2, textInstrPostTest, fText, xText, jText]
    for thisComponent in posttestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    posttestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "posttest"-------
    while continueRoutine:
        # get current time
        t = posttestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=posttestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *postTestResponse* updates
        waitOnFlip = False
        if postTestResponse.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            postTestResponse.frameNStart = frameN  # exact frame index
            postTestResponse.tStart = t  # local t and not account for scr refresh
            postTestResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(postTestResponse, 'tStartRefresh')  # time at next scr refresh
            postTestResponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(postTestResponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(postTestResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if postTestResponse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > postTestResponse.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                postTestResponse.tStop = t  # not accounting for scr refresh
                postTestResponse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(postTestResponse, 'tStopRefresh')  # time at next scr refresh
                postTestResponse.status = FINISHED
        if postTestResponse.status == STARTED and not waitOnFlip:
            theseKeys = postTestResponse.getKeys(keyList=['f', 'j'], waitRelease=False)
            _postTestResponse_allKeys.extend(theseKeys)
            if len(_postTestResponse_allKeys):
                postTestResponse.keys = _postTestResponse_allKeys[-1].name  # just the last key pressed
                postTestResponse.rt = _postTestResponse_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop postTestAudio1
        if postTestAudio1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            postTestAudio1.frameNStart = frameN  # exact frame index
            postTestAudio1.tStart = t  # local t and not account for scr refresh
            postTestAudio1.tStartRefresh = tThisFlipGlobal  # on global time
            postTestAudio1.play(when=win)  # sync with win flip
        
        # *fSound* updates
        if fSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fSound.frameNStart = frameN  # exact frame index
            fSound.tStart = t  # local t and not account for scr refresh
            fSound.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fSound, 'tStartRefresh')  # time at next scr refresh
            fSound.setAutoDraw(True)
        if fSound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fSound.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fSound.tStop = t  # not accounting for scr refresh
                fSound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fSound, 'tStopRefresh')  # time at next scr refresh
                fSound.setAutoDraw(False)
        
        # *fMute* updates
        if fMute.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            fMute.frameNStart = frameN  # exact frame index
            fMute.tStart = t  # local t and not account for scr refresh
            fMute.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fMute, 'tStartRefresh')  # time at next scr refresh
            fMute.setAutoDraw(True)
        if fMute.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fMute.tStartRefresh + 9-frameTolerance:
                # keep track of stop time/frame for later
                fMute.tStop = t  # not accounting for scr refresh
                fMute.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fMute, 'tStopRefresh')  # time at next scr refresh
                fMute.setAutoDraw(False)
        # start/stop postTestAudio2
        if postTestAudio2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            postTestAudio2.frameNStart = frameN  # exact frame index
            postTestAudio2.tStart = t  # local t and not account for scr refresh
            postTestAudio2.tStartRefresh = tThisFlipGlobal  # on global time
            postTestAudio2.play(when=win)  # sync with win flip
        
        # *xMute1* updates
        if xMute1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            xMute1.frameNStart = frameN  # exact frame index
            xMute1.tStart = t  # local t and not account for scr refresh
            xMute1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(xMute1, 'tStartRefresh')  # time at next scr refresh
            xMute1.setAutoDraw(True)
        if xMute1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > xMute1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                xMute1.tStop = t  # not accounting for scr refresh
                xMute1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(xMute1, 'tStopRefresh')  # time at next scr refresh
                xMute1.setAutoDraw(False)
        
        # *xSound* updates
        if xSound.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            xSound.frameNStart = frameN  # exact frame index
            xSound.tStart = t  # local t and not account for scr refresh
            xSound.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(xSound, 'tStartRefresh')  # time at next scr refresh
            xSound.setAutoDraw(True)
        if xSound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > xSound.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                xSound.tStop = t  # not accounting for scr refresh
                xSound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(xSound, 'tStopRefresh')  # time at next scr refresh
                xSound.setAutoDraw(False)
        
        # *xMute2* updates
        if xMute2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            xMute2.frameNStart = frameN  # exact frame index
            xMute2.tStart = t  # local t and not account for scr refresh
            xMute2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(xMute2, 'tStartRefresh')  # time at next scr refresh
            xMute2.setAutoDraw(True)
        if xMute2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > xMute2.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                xMute2.tStop = t  # not accounting for scr refresh
                xMute2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(xMute2, 'tStopRefresh')  # time at next scr refresh
                xMute2.setAutoDraw(False)
        # start/stop postTestAudio3
        if postTestAudio3.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            postTestAudio3.frameNStart = frameN  # exact frame index
            postTestAudio3.tStart = t  # local t and not account for scr refresh
            postTestAudio3.tStartRefresh = tThisFlipGlobal  # on global time
            postTestAudio3.play(when=win)  # sync with win flip
        
        # *jMute1* updates
        if jMute1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            jMute1.frameNStart = frameN  # exact frame index
            jMute1.tStart = t  # local t and not account for scr refresh
            jMute1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jMute1, 'tStartRefresh')  # time at next scr refresh
            jMute1.setAutoDraw(True)
        if jMute1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jMute1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                jMute1.tStop = t  # not accounting for scr refresh
                jMute1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(jMute1, 'tStopRefresh')  # time at next scr refresh
                jMute1.setAutoDraw(False)
        
        # *jSound* updates
        if jSound.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            jSound.frameNStart = frameN  # exact frame index
            jSound.tStart = t  # local t and not account for scr refresh
            jSound.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jSound, 'tStartRefresh')  # time at next scr refresh
            jSound.setAutoDraw(True)
        if jSound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jSound.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                jSound.tStop = t  # not accounting for scr refresh
                jSound.frameNStop = frameN  # exact frame index
                win.timeOnFlip(jSound, 'tStopRefresh')  # time at next scr refresh
                jSound.setAutoDraw(False)
        
        # *jMute2* updates
        if jMute2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            jMute2.frameNStart = frameN  # exact frame index
            jMute2.tStart = t  # local t and not account for scr refresh
            jMute2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jMute2, 'tStartRefresh')  # time at next scr refresh
            jMute2.setAutoDraw(True)
        if jMute2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jMute2.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                jMute2.tStop = t  # not accounting for scr refresh
                jMute2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(jMute2, 'tStopRefresh')  # time at next scr refresh
                jMute2.setAutoDraw(False)
        
        # *textInstrPostTest* updates
        if textInstrPostTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textInstrPostTest.frameNStart = frameN  # exact frame index
            textInstrPostTest.tStart = t  # local t and not account for scr refresh
            textInstrPostTest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInstrPostTest, 'tStartRefresh')  # time at next scr refresh
            textInstrPostTest.setAutoDraw(True)
        if textInstrPostTest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textInstrPostTest.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                textInstrPostTest.tStop = t  # not accounting for scr refresh
                textInstrPostTest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textInstrPostTest, 'tStopRefresh')  # time at next scr refresh
                textInstrPostTest.setAutoDraw(False)
        
        # *fText* updates
        if fText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fText.frameNStart = frameN  # exact frame index
            fText.tStart = t  # local t and not account for scr refresh
            fText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fText, 'tStartRefresh')  # time at next scr refresh
            fText.setAutoDraw(True)
        if fText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fText.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                fText.tStop = t  # not accounting for scr refresh
                fText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fText, 'tStopRefresh')  # time at next scr refresh
                fText.setAutoDraw(False)
        
        # *xText* updates
        if xText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            xText.frameNStart = frameN  # exact frame index
            xText.tStart = t  # local t and not account for scr refresh
            xText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(xText, 'tStartRefresh')  # time at next scr refresh
            xText.setAutoDraw(True)
        if xText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > xText.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                xText.tStop = t  # not accounting for scr refresh
                xText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(xText, 'tStopRefresh')  # time at next scr refresh
                xText.setAutoDraw(False)
        
        # *jText* updates
        if jText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            jText.frameNStart = frameN  # exact frame index
            jText.tStart = t  # local t and not account for scr refresh
            jText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jText, 'tStartRefresh')  # time at next scr refresh
            jText.setAutoDraw(True)
        if jText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jText.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                jText.tStop = t  # not accounting for scr refresh
                jText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(jText, 'tStopRefresh')  # time at next scr refresh
                jText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in posttestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "posttest"-------
    for thisComponent in posttestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if postTestResponse.keys in ['', [], None]:  # No response was made
        postTestResponse.keys = None
    postTestLoop.addData('postTestResponse.keys',postTestResponse.keys)
    if postTestResponse.keys != None:  # we had a response
        postTestLoop.addData('postTestResponse.rt', postTestResponse.rt)
    postTestLoop.addData('postTestResponse.started', postTestResponse.tStartRefresh)
    postTestLoop.addData('postTestResponse.stopped', postTestResponse.tStopRefresh)
    postTestAudio1.stop()  # ensure sound has stopped at end of routine
    postTestLoop.addData('postTestAudio1.started', postTestAudio1.tStartRefresh)
    postTestLoop.addData('postTestAudio1.stopped', postTestAudio1.tStopRefresh)
    postTestLoop.addData('fSound.started', fSound.tStartRefresh)
    postTestLoop.addData('fSound.stopped', fSound.tStopRefresh)
    postTestLoop.addData('fMute.started', fMute.tStartRefresh)
    postTestLoop.addData('fMute.stopped', fMute.tStopRefresh)
    postTestAudio2.stop()  # ensure sound has stopped at end of routine
    postTestLoop.addData('postTestAudio2.started', postTestAudio2.tStartRefresh)
    postTestLoop.addData('postTestAudio2.stopped', postTestAudio2.tStopRefresh)
    postTestLoop.addData('xMute1.started', xMute1.tStartRefresh)
    postTestLoop.addData('xMute1.stopped', xMute1.tStopRefresh)
    postTestLoop.addData('xSound.started', xSound.tStartRefresh)
    postTestLoop.addData('xSound.stopped', xSound.tStopRefresh)
    postTestLoop.addData('xMute2.started', xMute2.tStartRefresh)
    postTestLoop.addData('xMute2.stopped', xMute2.tStopRefresh)
    postTestAudio3.stop()  # ensure sound has stopped at end of routine
    postTestLoop.addData('postTestAudio3.started', postTestAudio3.tStartRefresh)
    postTestLoop.addData('postTestAudio3.stopped', postTestAudio3.tStopRefresh)
    postTestLoop.addData('jMute1.started', jMute1.tStartRefresh)
    postTestLoop.addData('jMute1.stopped', jMute1.tStopRefresh)
    postTestLoop.addData('jSound.started', jSound.tStartRefresh)
    postTestLoop.addData('jSound.stopped', jSound.tStopRefresh)
    postTestLoop.addData('jMute2.started', jMute2.tStartRefresh)
    postTestLoop.addData('jMute2.stopped', jMute2.tStopRefresh)
    postTestLoop.addData('textInstrPostTest.started', textInstrPostTest.tStartRefresh)
    postTestLoop.addData('textInstrPostTest.stopped', textInstrPostTest.tStopRefresh)
    postTestLoop.addData('fText.started', fText.tStartRefresh)
    postTestLoop.addData('fText.stopped', fText.tStopRefresh)
    postTestLoop.addData('xText.started', xText.tStartRefresh)
    postTestLoop.addData('xText.stopped', xText.tStopRefresh)
    postTestLoop.addData('jText.started', jText.tStartRefresh)
    postTestLoop.addData('jText.stopped', jText.tStopRefresh)
    # the Routine "posttest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'postTestLoop'


# ------Prepare to start Routine "thankuser"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
quit.keys = []
quit.rt = []
_quit_allKeys = []
# keep track of which components have finished
thankuserComponents = [text, quit]
for thisComponent in thankuserComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thankuserClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thankuser"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thankuserClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thankuserClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # *quit* updates
    waitOnFlip = False
    if quit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        quit.frameNStart = frameN  # exact frame index
        quit.tStart = t  # local t and not account for scr refresh
        quit.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(quit, 'tStartRefresh')  # time at next scr refresh
        quit.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(quit.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(quit.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if quit.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > quit.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            quit.tStop = t  # not accounting for scr refresh
            quit.frameNStop = frameN  # exact frame index
            win.timeOnFlip(quit, 'tStopRefresh')  # time at next scr refresh
            quit.status = FINISHED
    if quit.status == STARTED and not waitOnFlip:
        theseKeys = quit.getKeys(keyList=None, waitRelease=False)
        _quit_allKeys.extend(theseKeys)
        if len(_quit_allKeys):
            quit.keys = _quit_allKeys[-1].name  # just the last key pressed
            quit.rt = _quit_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thankuserComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thankuser"-------
for thisComponent in thankuserComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if quit.keys in ['', [], None]:  # No response was made
    quit.keys = None
thisExp.addData('quit.keys',quit.keys)
if quit.keys != None:  # we had a response
    thisExp.addData('quit.rt', quit.rt)
thisExp.addData('quit.started', quit.tStartRefresh)
thisExp.addData('quit.stopped', quit.tStopRefresh)
thisExp.nextEntry()

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
