﻿/******************* 
 * Condition1 Test *
 *******************/

import { PsychoJS } from './lib/core-2020.1.js';
import * as core from './lib/core-2020.1.js';
import { TrialHandler } from './lib/data-2020.1.js';
import { Scheduler } from './lib/util-2020.1.js';
import * as util from './lib/util-2020.1.js';
import * as visual from './lib/visual-2020.1.js';
import * as sound from './lib/sound-2020.1.js';

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'condition1';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instrRoutineBegin());
flowScheduler.add(instrRoutineEachFrame());
flowScheduler.add(instrRoutineEnd());
const alltrain1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(alltrain1LoopBegin, alltrain1LoopScheduler);
flowScheduler.add(alltrain1LoopScheduler);
flowScheduler.add(alltrain1LoopEnd);
flowScheduler.add(instr2RoutineBegin());
flowScheduler.add(instr2RoutineEachFrame());
flowScheduler.add(instr2RoutineEnd());
const alltrain2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(alltrain2LoopBegin, alltrain2LoopScheduler);
flowScheduler.add(alltrain2LoopScheduler);
flowScheduler.add(alltrain2LoopEnd);
flowScheduler.add(test1waitRoutineBegin());
flowScheduler.add(test1waitRoutineEachFrame());
flowScheduler.add(test1waitRoutineEnd());
flowScheduler.add(test1instrRoutineBegin());
flowScheduler.add(test1instrRoutineEachFrame());
flowScheduler.add(test1instrRoutineEnd());
const test1LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(test1LoopLoopBegin, test1LoopLoopScheduler);
flowScheduler.add(test1LoopLoopScheduler);
flowScheduler.add(test1LoopLoopEnd);
flowScheduler.add(test2waitRoutineBegin());
flowScheduler.add(test2waitRoutineEachFrame());
flowScheduler.add(test2waitRoutineEnd());
flowScheduler.add(test2instrRoutineBegin());
flowScheduler.add(test2instrRoutineEachFrame());
flowScheduler.add(test2instrRoutineEnd());
const test2LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(test2LoopLoopBegin, test2LoopLoopScheduler);
flowScheduler.add(test2LoopLoopScheduler);
flowScheduler.add(test2LoopLoopEnd);
flowScheduler.add(test3waitRoutineBegin());
flowScheduler.add(test3waitRoutineEachFrame());
flowScheduler.add(test3waitRoutineEnd());
flowScheduler.add(test3instrRoutineBegin());
flowScheduler.add(test3instrRoutineEachFrame());
flowScheduler.add(test3instrRoutineEnd());
const test3LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(test3LoopLoopBegin, test3LoopLoopScheduler);
flowScheduler.add(test3LoopLoopScheduler);
flowScheduler.add(test3LoopLoopEnd);
flowScheduler.add(postTestInstrRoutineBegin());
flowScheduler.add(postTestInstrRoutineEachFrame());
flowScheduler.add(postTestInstrRoutineEnd());
const postTestLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(postTestLoopLoopBegin, postTestLoopLoopScheduler);
flowScheduler.add(postTestLoopLoopScheduler);
flowScheduler.add(postTestLoopLoopEnd);
flowScheduler.add(thankuserRoutineBegin());
flowScheduler.add(thankuserRoutineEachFrame());
flowScheduler.add(thankuserRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instrClock;
var instructions;
var advanceTrain1;
var train1InstrClock;
var train1Type;
var skipTrain1Type;
var train1Clock;
var imagetrain1p1;
var stimuli1train1p1;
var stimuli2train1p1;
var stimuli3train1p1;
var stimuli4train1p1;
var stimuli5train1p1;
var listenTrain1p1;
var train1QuestInstrClock;
var train1QuestText;
var train1QuestAdvance;
var train1questionsClock;
var stimulitest1;
var correct;
var incorrect;
var train1Response;
var chooseImageTrain1;
var train1F;
var train1J;
var instr2Clock;
var train2warning3;
var train2warning2;
var train2warning1;
var skipTrain2Instr;
var train2InstrClock;
var train2Type;
var skipTrain2Type;
var train2Clock;
var imagetrain2;
var stimuli1train2;
var stimuli2train2;
var stimuli3train2;
var stimuli4train2;
var stimuli5train2;
var listenTrain2;
var train2QuestInstrClock;
var train2QuestText;
var train2QuestAdvance;
var trainquestions2Clock;
var stimulitest2;
var correct2;
var incorrect2;
var train2Response;
var chooseImageTrain2;
var train2F;
var train2J;
var test1waitClock;
var skipTest1Instr;
var test1warning3;
var test1warning2;
var test1warning1;
var test1instrClock;
var test1Text;
var key_resp;
var test1Clock;
var test1Audio1;
var test1Audio1Sound;
var test1Audio1Mute;
var test1Audio2;
var test1Audio2Mute1;
var test1Audio2Sound;
var test1Audio2Mute2;
var test1Response;
var test1Image;
var test1F;
var test1J;
var test1Instr;
var test2waitClock;
var skipTest2Instr;
var test2warning3;
var test2warning2;
var test2warning1;
var test2instrClock;
var test2Text;
var key_resp_2;
var test2Clock;
var test2Audio1;
var test2Audio1Sound;
var test1Audio2Mute;
var test2Audio2;
var test2Audio2Mute1;
var test2Audio2Sound;
var test2Audio2Mute2;
var test2Response;
var test2Image;
var test2F;
var test2J;
var test2Instr;
var test3waitClock;
var skipTest3Instr;
var test3warning3;
var test3warning2;
var test3warning1;
var test3instrClock;
var test3Text;
var key_resp_3;
var test3Clock;
var test3Audio1;
var test3Audio1Sound;
var test3Audio1Mute;
var test3Audio2;
var test3Audio2Mute1;
var test3Audio2Sound;
var test3Audio2Mute2;
var test3Response;
var test3Image;
var test3F;
var test3J;
var test3Instr;
var postTestInstrClock;
var skipPostTestInstr;
var postTestWarning3;
var postTestWarning2;
var postTestWarning1;
var posttestClock;
var postTestResponse;
var postTestAudio1;
var fSound;
var fMute;
var postTestAudio2;
var xMute1;
var xSound;
var xMute2;
var postTestAudio3;
var jMute1;
var jSound;
var jMute2;
var textInstrPostTest;
var fText;
var xText;
var jText;
var thankuserClock;
var text;
var quit;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions',
    text: 'This is an experiment about learning words of a foreign language. You will hear the pronunciation of each word five times, accompanied by a picture of the word. After hearing a few words, you will answer some picture matching questions: you will hear the pronunciation of one word you have learned, and choose the corresponding picture out of two. There will be two training sessions where you familiarize yourself with the language, three test sessions where you hear words you have learned and novel words, and one post test session. Participation is completely voluntary, and you can quit the experiment at any point.\n\nPress any key to advance.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  advanceTrain1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "train1Instr"
  train1InstrClock = new util.Clock();
  train1Type = new visual.TextStim({
    win: psychoJS.window,
    name: 'train1Type',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  skipTrain1Type = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "train1"
  train1Clock = new util.Clock();
  imagetrain1p1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imagetrain1p1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, (- 0.1)], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  stimuli1train1p1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimuli1train1p1.setVolume(1);
  stimuli2train1p1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimuli2train1p1.setVolume(1);
  stimuli3train1p1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimuli3train1p1.setVolume(1);
  stimuli4train1p1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimuli4train1p1.setVolume(1);
  stimuli5train1p1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimuli5train1p1.setVolume(1);
  listenTrain1p1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'listenTrain1p1',
    text: 'Listen to the words:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "train1QuestInstr"
  train1QuestInstrClock = new util.Clock();
  train1QuestText = new visual.TextStim({
    win: psychoJS.window,
    name: 'train1QuestText',
    text: 'Choose the correct image corresponding to the word you just heard.\n\nPress any key to advance',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  train1QuestAdvance = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "train1questions"
  train1questionsClock = new util.Clock();
  stimulitest1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimulitest1.setVolume(1);
  correct = new visual.ImageStim({
    win : psychoJS.window,
    name : 'correct', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  incorrect = new visual.ImageStim({
    win : psychoJS.window,
    name : 'incorrect', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  train1Response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  chooseImageTrain1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'chooseImageTrain1',
    text: 'Choose the correct image (F or J) corresponding to the word you just heard.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  train1F = new visual.TextStim({
    win: psychoJS.window,
    name: 'train1F',
    text: 'F',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  train1J = new visual.TextStim({
    win: psychoJS.window,
    name: 'train1J',
    text: 'J',
    font: 'Arial',
    units: undefined, 
    pos: [0.5, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "instr2"
  instr2Clock = new util.Clock();
  train2warning3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'train2warning3',
    text: 'Next part will start automatically\nin less than 3 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  train2warning2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'train2warning2',
    text: 'Next part will start automatically\nin less than 2 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  train2warning1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'train2warning1',
    text: 'Next part will start automatically\nin less than 1 minute.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  skipTrain2Instr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "train2Instr"
  train2InstrClock = new util.Clock();
  train2Type = new visual.TextStim({
    win: psychoJS.window,
    name: 'train2Type',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  skipTrain2Type = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "train2"
  train2Clock = new util.Clock();
  imagetrain2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imagetrain2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, (- 0.1)], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  stimuli1train2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimuli1train2.setVolume(1);
  stimuli2train2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimuli2train2.setVolume(1);
  stimuli3train2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimuli3train2.setVolume(1);
  stimuli4train2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimuli4train2.setVolume(1);
  stimuli5train2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimuli5train2.setVolume(1);
  listenTrain2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'listenTrain2',
    text: 'Listen to the words:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "train2QuestInstr"
  train2QuestInstrClock = new util.Clock();
  train2QuestText = new visual.TextStim({
    win: psychoJS.window,
    name: 'train2QuestText',
    text: 'Choose the correct image corresponding to the word you just heard.\n\nPress any key to advance',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  train2QuestAdvance = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trainquestions2"
  trainquestions2Clock = new util.Clock();
  stimulitest2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimulitest2.setVolume(1);
  correct2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'correct2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  incorrect2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'incorrect2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  train2Response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  chooseImageTrain2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'chooseImageTrain2',
    text: 'Choose the correct image (F or J) corresponding to the word you just heard.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  train2F = new visual.TextStim({
    win: psychoJS.window,
    name: 'train2F',
    text: 'F',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  train2J = new visual.TextStim({
    win: psychoJS.window,
    name: 'train2J',
    text: 'J',
    font: 'Arial',
    units: undefined, 
    pos: [0.5, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "test1wait"
  test1waitClock = new util.Clock();
  skipTest1Instr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  test1warning3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test1warning3',
    text: 'Next part will start automatically\nin less than 3 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  test1warning2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test1warning2',
    text: 'Next part will start automatically\nin less than 2 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  test1warning1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test1warning1',
    text: 'Next part will start automatically\nin less than 1 minute.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "test1instr"
  test1instrClock = new util.Clock();
  test1Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'test1Text',
    text: 'You will now hear two pronunciations of the words you have already heard. Select the correct pronunciation to the best of your ability.\n\nPress any key to start now.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "test1"
  test1Clock = new util.Clock();
  test1Audio1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  test1Audio1.setVolume(1);
  test1Audio1Sound = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test1Audio1Sound', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.3), (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  test1Audio1Mute = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test1Audio1Mute', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.3), (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  test1Audio2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  test1Audio2.setVolume(1);
  test1Audio2Mute1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test1Audio2Mute1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.3, (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  test1Audio2Sound = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test1Audio2Sound', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.3, (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  test1Audio2Mute2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test1Audio2Mute2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.3, (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  test1Response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  test1Image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test1Image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.1], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  test1F = new visual.TextStim({
    win: psychoJS.window,
    name: 'test1F',
    text: 'F',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), (- 0.1)], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  test1J = new visual.TextStim({
    win: psychoJS.window,
    name: 'test1J',
    text: 'J',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, (- 0.1)], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -10.0 
  });
  
  test1Instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'test1Instr',
    text: 'Choose the audio that has the correct pronunciation (F or J)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -11.0 
  });
  
  // Initialize components for Routine "test2wait"
  test2waitClock = new util.Clock();
  skipTest2Instr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  test2warning3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test2warning3',
    text: 'Next part will start automatically\nin less than 3 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  test2warning2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test2warning2',
    text: 'Next part will start automatically\nin less than 2 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  test2warning1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test2warning1',
    text: 'Next part will start automatically\nin less than 1 minute.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "test2instr"
  test2instrClock = new util.Clock();
  test2Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'test2Text',
    text: 'You will now hear two pronunciations of a word you have not heard. Select the one that you think might be the correct pronunciation.\n\nPress any key to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "test2"
  test2Clock = new util.Clock();
  test2Audio1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  test2Audio1.setVolume(1);
  test2Audio1Sound = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test2Audio1Sound', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.3), (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  test1Audio2Mute = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test1Audio2Mute', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.3), (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  test2Audio2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  test2Audio2.setVolume(1);
  test2Audio2Mute1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test2Audio2Mute1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.3, (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  test2Audio2Sound = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test2Audio2Sound', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.3, (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  test2Audio2Mute2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test2Audio2Mute2', units : undefined, 
    image : 'mute.png', mask : undefined,
    ori : 0, pos : [0.3, (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  test2Response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  test2Image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test2Image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.1], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  test2F = new visual.TextStim({
    win: psychoJS.window,
    name: 'test2F',
    text: 'F',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), (- 0.1)], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  test2J = new visual.TextStim({
    win: psychoJS.window,
    name: 'test2J',
    text: 'J',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, (- 0.1)], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -10.0 
  });
  
  test2Instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'test2Instr',
    text: 'Choose the audio that has the correct pronunciation (F or J)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -11.0 
  });
  
  // Initialize components for Routine "test3wait"
  test3waitClock = new util.Clock();
  skipTest3Instr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  test3warning3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test3warning3',
    text: 'Next part will start automatically\nin less than 3 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  test3warning2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test3warning2',
    text: 'Next part will start automatically\nin less than 2 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  test3warning1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test3warning1',
    text: 'Next part will start automatically\nin less than 1 minute.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "test3instr"
  test3instrClock = new util.Clock();
  test3Text = new visual.TextStim({
    win: psychoJS.window,
    name: 'test3Text',
    text: 'You will now hear two pronunciations of the words you just heard. Select the one that you think might be the correct pronunciation.\n\nPress any key to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "test3"
  test3Clock = new util.Clock();
  test3Audio1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  test3Audio1.setVolume(1);
  test3Audio1Sound = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test3Audio1Sound', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.3), (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  test3Audio1Mute = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test3Audio1Mute', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.3), (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  test3Audio2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  test3Audio2.setVolume(1);
  test3Audio2Mute1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test3Audio2Mute1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.3, (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  test3Audio2Sound = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test3Audio2Sound', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.3, (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  test3Audio2Mute2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test3Audio2Mute2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.3, (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  test3Response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  test3Image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'test3Image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.1], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  test3F = new visual.TextStim({
    win: psychoJS.window,
    name: 'test3F',
    text: 'F',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), (- 0.1)], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  test3J = new visual.TextStim({
    win: psychoJS.window,
    name: 'test3J',
    text: 'J',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, (- 0.1)], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -10.0 
  });
  
  test3Instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'test3Instr',
    text: 'Choose the audio that has the correct pronunciation (F or J)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -11.0 
  });
  
  // Initialize components for Routine "postTestInstr"
  postTestInstrClock = new util.Clock();
  skipPostTestInstr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  postTestWarning3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'postTestWarning3',
    text: 'Next part will start automatically\nin less than 3 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  postTestWarning2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'postTestWarning2',
    text: 'Next part will start automatically\nin less than 2 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  postTestWarning1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'postTestWarning1',
    text: 'Next part will start automatically\nin less than 1 minute.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "posttest"
  posttestClock = new util.Clock();
  postTestResponse = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  postTestAudio1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  postTestAudio1.setVolume(1);
  fSound = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fSound', units : undefined, 
    image : 'sound.png', mask : undefined,
    ori : 0, pos : [(- 0.5), (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  fMute = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fMute', units : undefined, 
    image : 'mute.png', mask : undefined,
    ori : 0, pos : [(- 0.5), (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  postTestAudio2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  postTestAudio2.setVolume(1);
  xMute1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'xMute1', units : undefined, 
    image : 'mute.png', mask : undefined,
    ori : 0, pos : [0, (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  xSound = new visual.ImageStim({
    win : psychoJS.window,
    name : 'xSound', units : undefined, 
    image : 'sound.png', mask : undefined,
    ori : 0, pos : [0, (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  xMute2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'xMute2', units : undefined, 
    image : 'mute.png', mask : undefined,
    ori : 0, pos : [0, (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  postTestAudio3 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  postTestAudio3.setVolume(1);
  jMute1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'jMute1', units : undefined, 
    image : 'mute.png', mask : undefined,
    ori : 0, pos : [0.5, (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -9.0 
  });
  jSound = new visual.ImageStim({
    win : psychoJS.window,
    name : 'jSound', units : undefined, 
    image : 'sound.png', mask : undefined,
    ori : 0, pos : [0.5, (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -10.0 
  });
  jMute2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'jMute2', units : undefined, 
    image : 'mute.png', mask : undefined,
    ori : 0, pos : [0.5, (- 0.3)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -11.0 
  });
  textInstrPostTest = new visual.TextStim({
    win: psychoJS.window,
    name: 'textInstrPostTest',
    text: 'Does the middle audio (X) match in stress with F or J? (Press F or J)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -12.0 
  });
  
  fText = new visual.TextStim({
    win: psychoJS.window,
    name: 'fText',
    text: 'F',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -13.0 
  });
  
  xText = new visual.TextStim({
    win: psychoJS.window,
    name: 'xText',
    text: 'X',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -14.0 
  });
  
  jText = new visual.TextStim({
    win: psychoJS.window,
    name: 'jText',
    text: 'J',
    font: 'Arial',
    units: undefined, 
    pos: [0.5, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -15.0 
  });
  
  // Initialize components for Routine "thankuser"
  thankuserClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Thank you for participating!\n\nPress any key to end this experiment',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  quit = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _advanceTrain1_allKeys;
var instrComponents;
function instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr'-------
    t = 0;
    instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    advanceTrain1.keys = undefined;
    advanceTrain1.rt = undefined;
    _advanceTrain1_allKeys = [];
    // keep track of which components have finished
    instrComponents = [];
    instrComponents.push(instructions);
    instrComponents.push(advanceTrain1);
    
    for (const thisComponent of instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions* updates
    if (t >= 0.0 && instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions.tStart = t;  // (not accounting for frame time here)
      instructions.frameNStart = frameN;  // exact frame index
      
      instructions.setAutoDraw(true);
    }

    
    // *advanceTrain1* updates
    if (t >= 0.0 && advanceTrain1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      advanceTrain1.tStart = t;  // (not accounting for frame time here)
      advanceTrain1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { advanceTrain1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { advanceTrain1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { advanceTrain1.clearEvents(); });
    }

    if (advanceTrain1.status === PsychoJS.Status.STARTED) {
      let theseKeys = advanceTrain1.getKeys({keyList: [], waitRelease: false});
      _advanceTrain1_allKeys = _advanceTrain1_allKeys.concat(theseKeys);
      if (_advanceTrain1_allKeys.length > 0) {
        advanceTrain1.keys = _advanceTrain1_allKeys[_advanceTrain1_allKeys.length - 1].name;  // just the last key pressed
        advanceTrain1.rt = _advanceTrain1_allKeys[_advanceTrain1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr'-------
    for (const thisComponent of instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var alltrain1;
var currentLoop;
function alltrain1LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  alltrain1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'aoiConditions/train1Conditions.xlsx',
    seed: undefined, name: 'alltrain1'
  });
  psychoJS.experiment.addLoop(alltrain1); // add the loop to the experiment
  currentLoop = alltrain1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisAlltrain1 of alltrain1) {
    const snapshot = alltrain1.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(train1InstrRoutineBegin(snapshot));
    thisScheduler.add(train1InstrRoutineEachFrame(snapshot));
    thisScheduler.add(train1InstrRoutineEnd(snapshot));
    const trial1phasesLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trial1phasesLoopBegin, trial1phasesLoopScheduler);
    thisScheduler.add(trial1phasesLoopScheduler);
    thisScheduler.add(trial1phasesLoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var trial1phases;
function trial1phasesLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trial1phases = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: condFile,
    seed: undefined, name: 'trial1phases'
  });
  psychoJS.experiment.addLoop(trial1phases); // add the loop to the experiment
  currentLoop = trial1phases;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial1phase of trial1phases) {
    const snapshot = trial1phases.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    const train1WordsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(train1WordsLoopBegin, train1WordsLoopScheduler);
    thisScheduler.add(train1WordsLoopScheduler);
    thisScheduler.add(train1WordsLoopEnd);
    thisScheduler.add(train1QuestInstrRoutineBegin(snapshot));
    thisScheduler.add(train1QuestInstrRoutineEachFrame(snapshot));
    thisScheduler.add(train1QuestInstrRoutineEnd(snapshot));
    const train1QuestionsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(train1QuestionsLoopBegin, train1QuestionsLoopScheduler);
    thisScheduler.add(train1QuestionsLoopScheduler);
    thisScheduler.add(train1QuestionsLoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var train1Words;
function train1WordsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  train1Words = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 0, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: condFiles,
    seed: undefined, name: 'train1Words'
  });
  psychoJS.experiment.addLoop(train1Words); // add the loop to the experiment
  currentLoop = train1Words;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrain1Word of train1Words) {
    const snapshot = train1Words.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(train1RoutineBegin(snapshot));
    thisScheduler.add(train1RoutineEachFrame(snapshot));
    thisScheduler.add(train1RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function train1WordsLoopEnd() {
  psychoJS.experiment.removeLoop(train1Words);

  return Scheduler.Event.NEXT;
}


var train1Questions;
function train1QuestionsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  train1Questions = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 0, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: testFiles,
    seed: undefined, name: 'train1Questions'
  });
  psychoJS.experiment.addLoop(train1Questions); // add the loop to the experiment
  currentLoop = train1Questions;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrain1Question of train1Questions) {
    const snapshot = train1Questions.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(train1questionsRoutineBegin(snapshot));
    thisScheduler.add(train1questionsRoutineEachFrame(snapshot));
    thisScheduler.add(train1questionsRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function train1QuestionsLoopEnd() {
  psychoJS.experiment.removeLoop(train1Questions);

  return Scheduler.Event.NEXT;
}


function trial1phasesLoopEnd() {
  psychoJS.experiment.removeLoop(trial1phases);

  return Scheduler.Event.NEXT;
}


function alltrain1LoopEnd() {
  psychoJS.experiment.removeLoop(alltrain1);

  return Scheduler.Event.NEXT;
}


var alltrain2;
function alltrain2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  alltrain2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'aoiConditions/train2Conditions.xlsx',
    seed: undefined, name: 'alltrain2'
  });
  psychoJS.experiment.addLoop(alltrain2); // add the loop to the experiment
  currentLoop = alltrain2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisAlltrain2 of alltrain2) {
    const snapshot = alltrain2.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(train2InstrRoutineBegin(snapshot));
    thisScheduler.add(train2InstrRoutineEachFrame(snapshot));
    thisScheduler.add(train2InstrRoutineEnd(snapshot));
    const trial2phasesLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trial2phasesLoopBegin, trial2phasesLoopScheduler);
    thisScheduler.add(trial2phasesLoopScheduler);
    thisScheduler.add(trial2phasesLoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var trial2phases;
function trial2phasesLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trial2phases = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: condFile,
    seed: undefined, name: 'trial2phases'
  });
  psychoJS.experiment.addLoop(trial2phases); // add the loop to the experiment
  currentLoop = trial2phases;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial2phase of trial2phases) {
    const snapshot = trial2phases.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    const train2WordsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(train2WordsLoopBegin, train2WordsLoopScheduler);
    thisScheduler.add(train2WordsLoopScheduler);
    thisScheduler.add(train2WordsLoopEnd);
    thisScheduler.add(train2QuestInstrRoutineBegin(snapshot));
    thisScheduler.add(train2QuestInstrRoutineEachFrame(snapshot));
    thisScheduler.add(train2QuestInstrRoutineEnd(snapshot));
    const train2QuestionsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(train2QuestionsLoopBegin, train2QuestionsLoopScheduler);
    thisScheduler.add(train2QuestionsLoopScheduler);
    thisScheduler.add(train2QuestionsLoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var train2Words;
function train2WordsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  train2Words = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 0, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: condFiles,
    seed: undefined, name: 'train2Words'
  });
  psychoJS.experiment.addLoop(train2Words); // add the loop to the experiment
  currentLoop = train2Words;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrain2Word of train2Words) {
    const snapshot = train2Words.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(train2RoutineBegin(snapshot));
    thisScheduler.add(train2RoutineEachFrame(snapshot));
    thisScheduler.add(train2RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function train2WordsLoopEnd() {
  psychoJS.experiment.removeLoop(train2Words);

  return Scheduler.Event.NEXT;
}


var train2Questions;
function train2QuestionsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  train2Questions = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 0, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: testFiles,
    seed: undefined, name: 'train2Questions'
  });
  psychoJS.experiment.addLoop(train2Questions); // add the loop to the experiment
  currentLoop = train2Questions;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrain2Question of train2Questions) {
    const snapshot = train2Questions.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trainquestions2RoutineBegin(snapshot));
    thisScheduler.add(trainquestions2RoutineEachFrame(snapshot));
    thisScheduler.add(trainquestions2RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function train2QuestionsLoopEnd() {
  psychoJS.experiment.removeLoop(train2Questions);

  return Scheduler.Event.NEXT;
}


function trial2phasesLoopEnd() {
  psychoJS.experiment.removeLoop(trial2phases);

  return Scheduler.Event.NEXT;
}


function alltrain2LoopEnd() {
  psychoJS.experiment.removeLoop(alltrain2);

  return Scheduler.Event.NEXT;
}


var test1Loop;
function test1LoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  test1Loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 0, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'aoiConditions/test1Conditions.xlsx',
    seed: undefined, name: 'test1Loop'
  });
  psychoJS.experiment.addLoop(test1Loop); // add the loop to the experiment
  currentLoop = test1Loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTest1Loop of test1Loop) {
    const snapshot = test1Loop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(test1RoutineBegin(snapshot));
    thisScheduler.add(test1RoutineEachFrame(snapshot));
    thisScheduler.add(test1RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function test1LoopLoopEnd() {
  psychoJS.experiment.removeLoop(test1Loop);

  return Scheduler.Event.NEXT;
}


var test2Loop;
function test2LoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  test2Loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 0, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'aoiConditions/test2Conditions.xlsx',
    seed: undefined, name: 'test2Loop'
  });
  psychoJS.experiment.addLoop(test2Loop); // add the loop to the experiment
  currentLoop = test2Loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTest2Loop of test2Loop) {
    const snapshot = test2Loop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(test2RoutineBegin(snapshot));
    thisScheduler.add(test2RoutineEachFrame(snapshot));
    thisScheduler.add(test2RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function test2LoopLoopEnd() {
  psychoJS.experiment.removeLoop(test2Loop);

  return Scheduler.Event.NEXT;
}


var test3Loop;
function test3LoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  test3Loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 0, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'aoiConditions/test3Conditions.xlsx',
    seed: undefined, name: 'test3Loop'
  });
  psychoJS.experiment.addLoop(test3Loop); // add the loop to the experiment
  currentLoop = test3Loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTest3Loop of test3Loop) {
    const snapshot = test3Loop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(test3RoutineBegin(snapshot));
    thisScheduler.add(test3RoutineEachFrame(snapshot));
    thisScheduler.add(test3RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function test3LoopLoopEnd() {
  psychoJS.experiment.removeLoop(test3Loop);

  return Scheduler.Event.NEXT;
}


var postTestLoop;
function postTestLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  postTestLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'postTestConditions.xlsx',
    seed: undefined, name: 'postTestLoop'
  });
  psychoJS.experiment.addLoop(postTestLoop); // add the loop to the experiment
  currentLoop = postTestLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPostTestLoop of postTestLoop) {
    const snapshot = postTestLoop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(posttestRoutineBegin(snapshot));
    thisScheduler.add(posttestRoutineEachFrame(snapshot));
    thisScheduler.add(posttestRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function postTestLoopLoopEnd() {
  psychoJS.experiment.removeLoop(postTestLoop);

  return Scheduler.Event.NEXT;
}


var _skipTrain1Type_allKeys;
var train1InstrComponents;
function train1InstrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'train1Instr'-------
    t = 0;
    train1InstrClock.reset(); // clock
    frameN = -1;
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    train1Type.setText((('You will be hearing ' + numWords) + ' words in a row, each for five times. Please try to remember these words’ pronunciations and their corresponding meaning shown in the pictures. \nPress any key to advance.'));
    skipTrain1Type.keys = undefined;
    skipTrain1Type.rt = undefined;
    _skipTrain1Type_allKeys = [];
    // keep track of which components have finished
    train1InstrComponents = [];
    train1InstrComponents.push(train1Type);
    train1InstrComponents.push(skipTrain1Type);
    
    for (const thisComponent of train1InstrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function train1InstrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'train1Instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = train1InstrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *train1Type* updates
    if (t >= 0.0 && train1Type.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train1Type.tStart = t;  // (not accounting for frame time here)
      train1Type.frameNStart = frameN;  // exact frame index
      
      train1Type.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train1Type.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train1Type.setAutoDraw(false);
    }
    
    // *skipTrain1Type* updates
    if (t >= 0.0 && skipTrain1Type.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      skipTrain1Type.tStart = t;  // (not accounting for frame time here)
      skipTrain1Type.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { skipTrain1Type.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { skipTrain1Type.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { skipTrain1Type.clearEvents(); });
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (skipTrain1Type.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      skipTrain1Type.status = PsychoJS.Status.FINISHED;
  }

    if (skipTrain1Type.status === PsychoJS.Status.STARTED) {
      let theseKeys = skipTrain1Type.getKeys({keyList: [], waitRelease: false});
      _skipTrain1Type_allKeys = _skipTrain1Type_allKeys.concat(theseKeys);
      if (_skipTrain1Type_allKeys.length > 0) {
        skipTrain1Type.keys = _skipTrain1Type_allKeys[_skipTrain1Type_allKeys.length - 1].name;  // just the last key pressed
        skipTrain1Type.rt = _skipTrain1Type_allKeys[_skipTrain1Type_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of train1InstrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function train1InstrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'train1Instr'-------
    for (const thisComponent of train1InstrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('skipTrain1Type.keys', skipTrain1Type.keys);
    if (typeof skipTrain1Type.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('skipTrain1Type.rt', skipTrain1Type.rt);
        routineTimer.reset();
        }
    
    skipTrain1Type.stop();
    return Scheduler.Event.NEXT;
  };
}


var train1Components;
function train1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'train1'-------
    t = 0;
    train1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    imagetrain1p1.setImage(imageLoc);
    stimuli1train1p1 = new sound.Sound({
    win: psychoJS.window,
    value: audio,
    secs: -1,
    });
    stimuli1train1p1.setVolume(1);
    stimuli2train1p1 = new sound.Sound({
    win: psychoJS.window,
    value: audio,
    secs: -1,
    });
    stimuli2train1p1.setVolume(1);
    stimuli3train1p1 = new sound.Sound({
    win: psychoJS.window,
    value: audio,
    secs: -1,
    });
    stimuli3train1p1.setVolume(1);
    stimuli4train1p1 = new sound.Sound({
    win: psychoJS.window,
    value: audio,
    secs: -1,
    });
    stimuli4train1p1.setVolume(1);
    stimuli5train1p1 = new sound.Sound({
    win: psychoJS.window,
    value: audio,
    secs: -1,
    });
    stimuli5train1p1.setVolume(1);
    // keep track of which components have finished
    train1Components = [];
    train1Components.push(imagetrain1p1);
    train1Components.push(stimuli1train1p1);
    train1Components.push(stimuli2train1p1);
    train1Components.push(stimuli3train1p1);
    train1Components.push(stimuli4train1p1);
    train1Components.push(stimuli5train1p1);
    train1Components.push(listenTrain1p1);
    
    for (const thisComponent of train1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function train1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'train1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = train1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *imagetrain1p1* updates
    if (t >= 2 && imagetrain1p1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imagetrain1p1.tStart = t;  // (not accounting for frame time here)
      imagetrain1p1.frameNStart = frameN;  // exact frame index
      
      imagetrain1p1.setAutoDraw(true);
    }

    frameRemains = 2 + 9 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imagetrain1p1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imagetrain1p1.setAutoDraw(false);
    }
    // start/stop stimuli1train1p1
    if (t >= 2 && stimuli1train1p1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli1train1p1.tStart = t;  // (not accounting for frame time here)
      stimuli1train1p1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimuli1train1p1.play(); });  // screen flip
      stimuli1train1p1.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimuli1train1p1.getDuration() + stimuli1train1p1.tStart)     && stimuli1train1p1.status === PsychoJS.Status.STARTED) {
      stimuli1train1p1.stop();  // stop the sound (if longer than duration)
      stimuli1train1p1.status = PsychoJS.Status.FINISHED;
    }
    // start/stop stimuli2train1p1
    if (t >= 4 && stimuli2train1p1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli2train1p1.tStart = t;  // (not accounting for frame time here)
      stimuli2train1p1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimuli2train1p1.play(); });  // screen flip
      stimuli2train1p1.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimuli2train1p1.getDuration() + stimuli2train1p1.tStart)     && stimuli2train1p1.status === PsychoJS.Status.STARTED) {
      stimuli2train1p1.stop();  // stop the sound (if longer than duration)
      stimuli2train1p1.status = PsychoJS.Status.FINISHED;
    }
    // start/stop stimuli3train1p1
    if (t >= 6 && stimuli3train1p1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli3train1p1.tStart = t;  // (not accounting for frame time here)
      stimuli3train1p1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimuli3train1p1.play(); });  // screen flip
      stimuli3train1p1.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimuli3train1p1.getDuration() + stimuli3train1p1.tStart)     && stimuli3train1p1.status === PsychoJS.Status.STARTED) {
      stimuli3train1p1.stop();  // stop the sound (if longer than duration)
      stimuli3train1p1.status = PsychoJS.Status.FINISHED;
    }
    // start/stop stimuli4train1p1
    if (t >= 8 && stimuli4train1p1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli4train1p1.tStart = t;  // (not accounting for frame time here)
      stimuli4train1p1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimuli4train1p1.play(); });  // screen flip
      stimuli4train1p1.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimuli4train1p1.getDuration() + stimuli4train1p1.tStart)     && stimuli4train1p1.status === PsychoJS.Status.STARTED) {
      stimuli4train1p1.stop();  // stop the sound (if longer than duration)
      stimuli4train1p1.status = PsychoJS.Status.FINISHED;
    }
    // start/stop stimuli5train1p1
    if (t >= 10 && stimuli5train1p1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli5train1p1.tStart = t;  // (not accounting for frame time here)
      stimuli5train1p1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimuli5train1p1.play(); });  // screen flip
      stimuli5train1p1.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimuli5train1p1.getDuration() + stimuli5train1p1.tStart)     && stimuli5train1p1.status === PsychoJS.Status.STARTED) {
      stimuli5train1p1.stop();  // stop the sound (if longer than duration)
      stimuli5train1p1.status = PsychoJS.Status.FINISHED;
    }
    
    // *listenTrain1p1* updates
    if (t >= 0.0 && listenTrain1p1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      listenTrain1p1.tStart = t;  // (not accounting for frame time here)
      listenTrain1p1.frameNStart = frameN;  // exact frame index
      
      listenTrain1p1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 11 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (listenTrain1p1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      listenTrain1p1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of train1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function train1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'train1'-------
    for (const thisComponent of train1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    stimuli1train1p1.stop();  // ensure sound has stopped at end of routine
    stimuli2train1p1.stop();  // ensure sound has stopped at end of routine
    stimuli3train1p1.stop();  // ensure sound has stopped at end of routine
    stimuli4train1p1.stop();  // ensure sound has stopped at end of routine
    stimuli5train1p1.stop();  // ensure sound has stopped at end of routine
    // the Routine "train1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _train1QuestAdvance_allKeys;
var train1QuestInstrComponents;
function train1QuestInstrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'train1QuestInstr'-------
    t = 0;
    train1QuestInstrClock.reset(); // clock
    frameN = -1;
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    train1QuestAdvance.keys = undefined;
    train1QuestAdvance.rt = undefined;
    _train1QuestAdvance_allKeys = [];
    // keep track of which components have finished
    train1QuestInstrComponents = [];
    train1QuestInstrComponents.push(train1QuestText);
    train1QuestInstrComponents.push(train1QuestAdvance);
    
    for (const thisComponent of train1QuestInstrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function train1QuestInstrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'train1QuestInstr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = train1QuestInstrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *train1QuestText* updates
    if (t >= 0.0 && train1QuestText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train1QuestText.tStart = t;  // (not accounting for frame time here)
      train1QuestText.frameNStart = frameN;  // exact frame index
      
      train1QuestText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train1QuestText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train1QuestText.setAutoDraw(false);
    }
    
    // *train1QuestAdvance* updates
    if (t >= 0.0 && train1QuestAdvance.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train1QuestAdvance.tStart = t;  // (not accounting for frame time here)
      train1QuestAdvance.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { train1QuestAdvance.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { train1QuestAdvance.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { train1QuestAdvance.clearEvents(); });
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train1QuestAdvance.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train1QuestAdvance.status = PsychoJS.Status.FINISHED;
  }

    if (train1QuestAdvance.status === PsychoJS.Status.STARTED) {
      let theseKeys = train1QuestAdvance.getKeys({keyList: [], waitRelease: false});
      _train1QuestAdvance_allKeys = _train1QuestAdvance_allKeys.concat(theseKeys);
      if (_train1QuestAdvance_allKeys.length > 0) {
        train1QuestAdvance.keys = _train1QuestAdvance_allKeys[_train1QuestAdvance_allKeys.length - 1].name;  // just the last key pressed
        train1QuestAdvance.rt = _train1QuestAdvance_allKeys[_train1QuestAdvance_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of train1QuestInstrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function train1QuestInstrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'train1QuestInstr'-------
    for (const thisComponent of train1QuestInstrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('train1QuestAdvance.keys', train1QuestAdvance.keys);
    if (typeof train1QuestAdvance.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('train1QuestAdvance.rt', train1QuestAdvance.rt);
        routineTimer.reset();
        }
    
    train1QuestAdvance.stop();
    return Scheduler.Event.NEXT;
  };
}


var _train1Response_allKeys;
var train1questionsComponents;
function train1questionsRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'train1questions'-------
    t = 0;
    train1questionsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    stimulitest1 = new sound.Sound({
    win: psychoJS.window,
    value: audioTrue,
    secs: -1,
    });
    stimulitest1.setVolume(1);
    correct.setPos([truePos, (- 0.3)]);
    correct.setImage(imageTrue);
    incorrect.setPos([falsePos, (- 0.3)]);
    incorrect.setImage(imageFalse);
    train1Response.keys = undefined;
    train1Response.rt = undefined;
    _train1Response_allKeys = [];
    // keep track of which components have finished
    train1questionsComponents = [];
    train1questionsComponents.push(stimulitest1);
    train1questionsComponents.push(correct);
    train1questionsComponents.push(incorrect);
    train1questionsComponents.push(train1Response);
    train1questionsComponents.push(chooseImageTrain1);
    train1questionsComponents.push(train1F);
    train1questionsComponents.push(train1J);
    
    for (const thisComponent of train1questionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function train1questionsRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'train1questions'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = train1questionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop stimulitest1
    if (t >= 0.5 && stimulitest1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimulitest1.tStart = t;  // (not accounting for frame time here)
      stimulitest1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimulitest1.play(); });  // screen flip
      stimulitest1.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimulitest1.getDuration() + stimulitest1.tStart)     && stimulitest1.status === PsychoJS.Status.STARTED) {
      stimulitest1.stop();  // stop the sound (if longer than duration)
      stimulitest1.status = PsychoJS.Status.FINISHED;
    }
    
    // *correct* updates
    if (t >= 0.5 && correct.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      correct.tStart = t;  // (not accounting for frame time here)
      correct.frameNStart = frameN;  // exact frame index
      
      correct.setAutoDraw(true);
    }

    frameRemains = 0.5 + 9.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (correct.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      correct.setAutoDraw(false);
    }
    
    // *incorrect* updates
    if (t >= 0.5 && incorrect.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      incorrect.tStart = t;  // (not accounting for frame time here)
      incorrect.frameNStart = frameN;  // exact frame index
      
      incorrect.setAutoDraw(true);
    }

    frameRemains = 0.5 + 9.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (incorrect.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      incorrect.setAutoDraw(false);
    }
    
    // *train1Response* updates
    if (t >= 1.5 && train1Response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train1Response.tStart = t;  // (not accounting for frame time here)
      train1Response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { train1Response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { train1Response.start(); }); // start on screen flip
    }

    frameRemains = 1.5 + 8.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train1Response.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train1Response.status = PsychoJS.Status.FINISHED;
  }

    if (train1Response.status === PsychoJS.Status.STARTED) {
      let theseKeys = train1Response.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _train1Response_allKeys = _train1Response_allKeys.concat(theseKeys);
      if (_train1Response_allKeys.length > 0) {
        train1Response.keys = _train1Response_allKeys[_train1Response_allKeys.length - 1].name;  // just the last key pressed
        train1Response.rt = _train1Response_allKeys[_train1Response_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *chooseImageTrain1* updates
    if (t >= 0 && chooseImageTrain1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      chooseImageTrain1.tStart = t;  // (not accounting for frame time here)
      chooseImageTrain1.frameNStart = frameN;  // exact frame index
      
      chooseImageTrain1.setAutoDraw(true);
    }

    frameRemains = 0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (chooseImageTrain1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      chooseImageTrain1.setAutoDraw(false);
    }
    
    // *train1F* updates
    if (t >= 1.5 && train1F.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train1F.tStart = t;  // (not accounting for frame time here)
      train1F.frameNStart = frameN;  // exact frame index
      
      train1F.setAutoDraw(true);
    }

    frameRemains = 1.5 + 8.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train1F.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train1F.setAutoDraw(false);
    }
    
    // *train1J* updates
    if (t >= 1.5 && train1J.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train1J.tStart = t;  // (not accounting for frame time here)
      train1J.frameNStart = frameN;  // exact frame index
      
      train1J.setAutoDraw(true);
    }

    frameRemains = 1.5 + 8.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train1J.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train1J.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of train1questionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function train1questionsRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'train1questions'-------
    for (const thisComponent of train1questionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    stimulitest1.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('train1Response.keys', train1Response.keys);
    if (typeof train1Response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('train1Response.rt', train1Response.rt);
        routineTimer.reset();
        }
    
    train1Response.stop();
    // the Routine "train1questions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _skipTrain2Instr_allKeys;
var instr2Components;
function instr2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr2'-------
    t = 0;
    instr2Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(180.000000);
    // update component parameters for each repeat
    skipTrain2Instr.keys = undefined;
    skipTrain2Instr.rt = undefined;
    _skipTrain2Instr_allKeys = [];
    // keep track of which components have finished
    instr2Components = [];
    instr2Components.push(train2warning3);
    instr2Components.push(train2warning2);
    instr2Components.push(train2warning1);
    instr2Components.push(skipTrain2Instr);
    
    for (const thisComponent of instr2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instr2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *train2warning3* updates
    if (t >= 0 && train2warning3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train2warning3.tStart = t;  // (not accounting for frame time here)
      train2warning3.frameNStart = frameN;  // exact frame index
      
      train2warning3.setAutoDraw(true);
    }

    frameRemains = 0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train2warning3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train2warning3.setAutoDraw(false);
    }
    
    // *train2warning2* updates
    if (t >= 60 && train2warning2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train2warning2.tStart = t;  // (not accounting for frame time here)
      train2warning2.frameNStart = frameN;  // exact frame index
      
      train2warning2.setAutoDraw(true);
    }

    frameRemains = 60 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train2warning2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train2warning2.setAutoDraw(false);
    }
    
    // *train2warning1* updates
    if (t >= 120 && train2warning1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train2warning1.tStart = t;  // (not accounting for frame time here)
      train2warning1.frameNStart = frameN;  // exact frame index
      
      train2warning1.setAutoDraw(true);
    }

    frameRemains = 120 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train2warning1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train2warning1.setAutoDraw(false);
    }
    
    // *skipTrain2Instr* updates
    if (t >= 0.0 && skipTrain2Instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      skipTrain2Instr.tStart = t;  // (not accounting for frame time here)
      skipTrain2Instr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { skipTrain2Instr.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { skipTrain2Instr.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { skipTrain2Instr.clearEvents(); });
    }

    frameRemains = 0.0 + 180 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (skipTrain2Instr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      skipTrain2Instr.status = PsychoJS.Status.FINISHED;
  }

    if (skipTrain2Instr.status === PsychoJS.Status.STARTED) {
      let theseKeys = skipTrain2Instr.getKeys({keyList: [], waitRelease: false});
      _skipTrain2Instr_allKeys = _skipTrain2Instr_allKeys.concat(theseKeys);
      if (_skipTrain2Instr_allKeys.length > 0) {
        skipTrain2Instr.keys = _skipTrain2Instr_allKeys[_skipTrain2Instr_allKeys.length - 1].name;  // just the last key pressed
        skipTrain2Instr.rt = _skipTrain2Instr_allKeys[_skipTrain2Instr_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instr2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr2'-------
    for (const thisComponent of instr2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('skipTrain2Instr.keys', skipTrain2Instr.keys);
    if (typeof skipTrain2Instr.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('skipTrain2Instr.rt', skipTrain2Instr.rt);
        routineTimer.reset();
        }
    
    skipTrain2Instr.stop();
    return Scheduler.Event.NEXT;
  };
}


var _skipTrain2Type_allKeys;
var train2InstrComponents;
function train2InstrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'train2Instr'-------
    t = 0;
    train2InstrClock.reset(); // clock
    frameN = -1;
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    train2Type.setText((('You will be hearing ' + numWords) + ' words in a row, each for five times. Please try to remember these words’ pronunciations and their corresponding meaning shown in the pictures. \nPress any key to advance.'));
    skipTrain2Type.keys = undefined;
    skipTrain2Type.rt = undefined;
    _skipTrain2Type_allKeys = [];
    // keep track of which components have finished
    train2InstrComponents = [];
    train2InstrComponents.push(train2Type);
    train2InstrComponents.push(skipTrain2Type);
    
    for (const thisComponent of train2InstrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function train2InstrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'train2Instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = train2InstrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *train2Type* updates
    if (t >= 0.0 && train2Type.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train2Type.tStart = t;  // (not accounting for frame time here)
      train2Type.frameNStart = frameN;  // exact frame index
      
      train2Type.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train2Type.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train2Type.setAutoDraw(false);
    }
    
    // *skipTrain2Type* updates
    if (t >= 0.0 && skipTrain2Type.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      skipTrain2Type.tStart = t;  // (not accounting for frame time here)
      skipTrain2Type.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { skipTrain2Type.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { skipTrain2Type.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { skipTrain2Type.clearEvents(); });
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (skipTrain2Type.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      skipTrain2Type.status = PsychoJS.Status.FINISHED;
  }

    if (skipTrain2Type.status === PsychoJS.Status.STARTED) {
      let theseKeys = skipTrain2Type.getKeys({keyList: [], waitRelease: false});
      _skipTrain2Type_allKeys = _skipTrain2Type_allKeys.concat(theseKeys);
      if (_skipTrain2Type_allKeys.length > 0) {
        skipTrain2Type.keys = _skipTrain2Type_allKeys[_skipTrain2Type_allKeys.length - 1].name;  // just the last key pressed
        skipTrain2Type.rt = _skipTrain2Type_allKeys[_skipTrain2Type_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of train2InstrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function train2InstrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'train2Instr'-------
    for (const thisComponent of train2InstrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('skipTrain2Type.keys', skipTrain2Type.keys);
    if (typeof skipTrain2Type.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('skipTrain2Type.rt', skipTrain2Type.rt);
        routineTimer.reset();
        }
    
    skipTrain2Type.stop();
    return Scheduler.Event.NEXT;
  };
}


var train2Components;
function train2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'train2'-------
    t = 0;
    train2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    imagetrain2.setImage(imageLoc);
    stimuli1train2 = new sound.Sound({
    win: psychoJS.window,
    value: audio,
    secs: -1,
    });
    stimuli1train2.setVolume(1);
    stimuli2train2 = new sound.Sound({
    win: psychoJS.window,
    value: audio,
    secs: -1,
    });
    stimuli2train2.setVolume(1);
    stimuli3train2 = new sound.Sound({
    win: psychoJS.window,
    value: audio,
    secs: -1,
    });
    stimuli3train2.setVolume(1);
    stimuli4train2 = new sound.Sound({
    win: psychoJS.window,
    value: audio,
    secs: -1,
    });
    stimuli4train2.setVolume(1);
    stimuli5train2 = new sound.Sound({
    win: psychoJS.window,
    value: audio,
    secs: -1,
    });
    stimuli5train2.setVolume(1);
    // keep track of which components have finished
    train2Components = [];
    train2Components.push(imagetrain2);
    train2Components.push(stimuli1train2);
    train2Components.push(stimuli2train2);
    train2Components.push(stimuli3train2);
    train2Components.push(stimuli4train2);
    train2Components.push(stimuli5train2);
    train2Components.push(listenTrain2);
    
    for (const thisComponent of train2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function train2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'train2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = train2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *imagetrain2* updates
    if (t >= 2 && imagetrain2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imagetrain2.tStart = t;  // (not accounting for frame time here)
      imagetrain2.frameNStart = frameN;  // exact frame index
      
      imagetrain2.setAutoDraw(true);
    }

    frameRemains = 2 + 9 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imagetrain2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imagetrain2.setAutoDraw(false);
    }
    // start/stop stimuli1train2
    if (t >= 2 && stimuli1train2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli1train2.tStart = t;  // (not accounting for frame time here)
      stimuli1train2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimuli1train2.play(); });  // screen flip
      stimuli1train2.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimuli1train2.getDuration() + stimuli1train2.tStart)     && stimuli1train2.status === PsychoJS.Status.STARTED) {
      stimuli1train2.stop();  // stop the sound (if longer than duration)
      stimuli1train2.status = PsychoJS.Status.FINISHED;
    }
    // start/stop stimuli2train2
    if (t >= 4 && stimuli2train2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli2train2.tStart = t;  // (not accounting for frame time here)
      stimuli2train2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimuli2train2.play(); });  // screen flip
      stimuli2train2.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimuli2train2.getDuration() + stimuli2train2.tStart)     && stimuli2train2.status === PsychoJS.Status.STARTED) {
      stimuli2train2.stop();  // stop the sound (if longer than duration)
      stimuli2train2.status = PsychoJS.Status.FINISHED;
    }
    // start/stop stimuli3train2
    if (t >= 6 && stimuli3train2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli3train2.tStart = t;  // (not accounting for frame time here)
      stimuli3train2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimuli3train2.play(); });  // screen flip
      stimuli3train2.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimuli3train2.getDuration() + stimuli3train2.tStart)     && stimuli3train2.status === PsychoJS.Status.STARTED) {
      stimuli3train2.stop();  // stop the sound (if longer than duration)
      stimuli3train2.status = PsychoJS.Status.FINISHED;
    }
    // start/stop stimuli4train2
    if (t >= 8 && stimuli4train2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli4train2.tStart = t;  // (not accounting for frame time here)
      stimuli4train2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimuli4train2.play(); });  // screen flip
      stimuli4train2.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimuli4train2.getDuration() + stimuli4train2.tStart)     && stimuli4train2.status === PsychoJS.Status.STARTED) {
      stimuli4train2.stop();  // stop the sound (if longer than duration)
      stimuli4train2.status = PsychoJS.Status.FINISHED;
    }
    // start/stop stimuli5train2
    if (t >= 10 && stimuli5train2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli5train2.tStart = t;  // (not accounting for frame time here)
      stimuli5train2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimuli5train2.play(); });  // screen flip
      stimuli5train2.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimuli5train2.getDuration() + stimuli5train2.tStart)     && stimuli5train2.status === PsychoJS.Status.STARTED) {
      stimuli5train2.stop();  // stop the sound (if longer than duration)
      stimuli5train2.status = PsychoJS.Status.FINISHED;
    }
    
    // *listenTrain2* updates
    if (t >= 0.0 && listenTrain2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      listenTrain2.tStart = t;  // (not accounting for frame time here)
      listenTrain2.frameNStart = frameN;  // exact frame index
      
      listenTrain2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 11 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (listenTrain2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      listenTrain2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of train2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function train2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'train2'-------
    for (const thisComponent of train2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    stimuli1train2.stop();  // ensure sound has stopped at end of routine
    stimuli2train2.stop();  // ensure sound has stopped at end of routine
    stimuli3train2.stop();  // ensure sound has stopped at end of routine
    stimuli4train2.stop();  // ensure sound has stopped at end of routine
    stimuli5train2.stop();  // ensure sound has stopped at end of routine
    // the Routine "train2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _train2QuestAdvance_allKeys;
var train2QuestInstrComponents;
function train2QuestInstrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'train2QuestInstr'-------
    t = 0;
    train2QuestInstrClock.reset(); // clock
    frameN = -1;
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    train2QuestAdvance.keys = undefined;
    train2QuestAdvance.rt = undefined;
    _train2QuestAdvance_allKeys = [];
    // keep track of which components have finished
    train2QuestInstrComponents = [];
    train2QuestInstrComponents.push(train2QuestText);
    train2QuestInstrComponents.push(train2QuestAdvance);
    
    for (const thisComponent of train2QuestInstrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function train2QuestInstrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'train2QuestInstr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = train2QuestInstrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *train2QuestText* updates
    if (t >= 0.0 && train2QuestText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train2QuestText.tStart = t;  // (not accounting for frame time here)
      train2QuestText.frameNStart = frameN;  // exact frame index
      
      train2QuestText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train2QuestText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train2QuestText.setAutoDraw(false);
    }
    
    // *train2QuestAdvance* updates
    if (t >= 0.0 && train2QuestAdvance.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train2QuestAdvance.tStart = t;  // (not accounting for frame time here)
      train2QuestAdvance.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { train2QuestAdvance.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { train2QuestAdvance.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { train2QuestAdvance.clearEvents(); });
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train2QuestAdvance.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train2QuestAdvance.status = PsychoJS.Status.FINISHED;
  }

    if (train2QuestAdvance.status === PsychoJS.Status.STARTED) {
      let theseKeys = train2QuestAdvance.getKeys({keyList: [], waitRelease: false});
      _train2QuestAdvance_allKeys = _train2QuestAdvance_allKeys.concat(theseKeys);
      if (_train2QuestAdvance_allKeys.length > 0) {
        train2QuestAdvance.keys = _train2QuestAdvance_allKeys[_train2QuestAdvance_allKeys.length - 1].name;  // just the last key pressed
        train2QuestAdvance.rt = _train2QuestAdvance_allKeys[_train2QuestAdvance_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of train2QuestInstrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function train2QuestInstrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'train2QuestInstr'-------
    for (const thisComponent of train2QuestInstrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('train2QuestAdvance.keys', train2QuestAdvance.keys);
    if (typeof train2QuestAdvance.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('train2QuestAdvance.rt', train2QuestAdvance.rt);
        routineTimer.reset();
        }
    
    train2QuestAdvance.stop();
    return Scheduler.Event.NEXT;
  };
}


var _train2Response_allKeys;
var trainquestions2Components;
function trainquestions2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trainquestions2'-------
    t = 0;
    trainquestions2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    stimulitest2 = new sound.Sound({
    win: psychoJS.window,
    value: audioTrue,
    secs: -1,
    });
    stimulitest2.setVolume(1);
    correct2.setPos([truePos, (- 0.3)]);
    correct2.setImage(imageTrue);
    incorrect2.setPos([falsePos, (- 0.3)]);
    incorrect2.setImage(imageFalse);
    train2Response.keys = undefined;
    train2Response.rt = undefined;
    _train2Response_allKeys = [];
    // keep track of which components have finished
    trainquestions2Components = [];
    trainquestions2Components.push(stimulitest2);
    trainquestions2Components.push(correct2);
    trainquestions2Components.push(incorrect2);
    trainquestions2Components.push(train2Response);
    trainquestions2Components.push(chooseImageTrain2);
    trainquestions2Components.push(train2F);
    trainquestions2Components.push(train2J);
    
    for (const thisComponent of trainquestions2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function trainquestions2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trainquestions2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trainquestions2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop stimulitest2
    if (t >= 0.5 && stimulitest2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimulitest2.tStart = t;  // (not accounting for frame time here)
      stimulitest2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimulitest2.play(); });  // screen flip
      stimulitest2.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimulitest2.getDuration() + stimulitest2.tStart)     && stimulitest2.status === PsychoJS.Status.STARTED) {
      stimulitest2.stop();  // stop the sound (if longer than duration)
      stimulitest2.status = PsychoJS.Status.FINISHED;
    }
    
    // *correct2* updates
    if (t >= 0.5 && correct2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      correct2.tStart = t;  // (not accounting for frame time here)
      correct2.frameNStart = frameN;  // exact frame index
      
      correct2.setAutoDraw(true);
    }

    frameRemains = 0.5 + 9.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (correct2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      correct2.setAutoDraw(false);
    }
    
    // *incorrect2* updates
    if (t >= 0.5 && incorrect2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      incorrect2.tStart = t;  // (not accounting for frame time here)
      incorrect2.frameNStart = frameN;  // exact frame index
      
      incorrect2.setAutoDraw(true);
    }

    frameRemains = 0.5 + 9.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (incorrect2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      incorrect2.setAutoDraw(false);
    }
    
    // *train2Response* updates
    if (t >= 1.5 && train2Response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train2Response.tStart = t;  // (not accounting for frame time here)
      train2Response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { train2Response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { train2Response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { train2Response.clearEvents(); });
    }

    frameRemains = 1.5 + 8.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train2Response.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train2Response.status = PsychoJS.Status.FINISHED;
  }

    if (train2Response.status === PsychoJS.Status.STARTED) {
      let theseKeys = train2Response.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _train2Response_allKeys = _train2Response_allKeys.concat(theseKeys);
      if (_train2Response_allKeys.length > 0) {
        train2Response.keys = _train2Response_allKeys[_train2Response_allKeys.length - 1].name;  // just the last key pressed
        train2Response.rt = _train2Response_allKeys[_train2Response_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *chooseImageTrain2* updates
    if (t >= 0 && chooseImageTrain2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      chooseImageTrain2.tStart = t;  // (not accounting for frame time here)
      chooseImageTrain2.frameNStart = frameN;  // exact frame index
      
      chooseImageTrain2.setAutoDraw(true);
    }

    frameRemains = 0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (chooseImageTrain2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      chooseImageTrain2.setAutoDraw(false);
    }
    
    // *train2F* updates
    if (t >= 1.5 && train2F.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train2F.tStart = t;  // (not accounting for frame time here)
      train2F.frameNStart = frameN;  // exact frame index
      
      train2F.setAutoDraw(true);
    }

    frameRemains = 1.5 + 8.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train2F.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train2F.setAutoDraw(false);
    }
    
    // *train2J* updates
    if (t >= 1.5 && train2J.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train2J.tStart = t;  // (not accounting for frame time here)
      train2J.frameNStart = frameN;  // exact frame index
      
      train2J.setAutoDraw(true);
    }

    frameRemains = 1.5 + 8.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train2J.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train2J.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trainquestions2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trainquestions2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trainquestions2'-------
    for (const thisComponent of trainquestions2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    stimulitest2.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('train2Response.keys', train2Response.keys);
    if (typeof train2Response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('train2Response.rt', train2Response.rt);
        routineTimer.reset();
        }
    
    train2Response.stop();
    // the Routine "trainquestions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _skipTest1Instr_allKeys;
var test1waitComponents;
function test1waitRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'test1wait'-------
    t = 0;
    test1waitClock.reset(); // clock
    frameN = -1;
    routineTimer.add(180.000000);
    // update component parameters for each repeat
    skipTest1Instr.keys = undefined;
    skipTest1Instr.rt = undefined;
    _skipTest1Instr_allKeys = [];
    // keep track of which components have finished
    test1waitComponents = [];
    test1waitComponents.push(skipTest1Instr);
    test1waitComponents.push(test1warning3);
    test1waitComponents.push(test1warning2);
    test1waitComponents.push(test1warning1);
    
    for (const thisComponent of test1waitComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function test1waitRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'test1wait'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = test1waitClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *skipTest1Instr* updates
    if (t >= 0.0 && skipTest1Instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      skipTest1Instr.tStart = t;  // (not accounting for frame time here)
      skipTest1Instr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { skipTest1Instr.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { skipTest1Instr.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { skipTest1Instr.clearEvents(); });
    }

    frameRemains = 0.0 + 180 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (skipTest1Instr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      skipTest1Instr.status = PsychoJS.Status.FINISHED;
  }

    if (skipTest1Instr.status === PsychoJS.Status.STARTED) {
      let theseKeys = skipTest1Instr.getKeys({keyList: [], waitRelease: false});
      _skipTest1Instr_allKeys = _skipTest1Instr_allKeys.concat(theseKeys);
      if (_skipTest1Instr_allKeys.length > 0) {
        skipTest1Instr.keys = _skipTest1Instr_allKeys[_skipTest1Instr_allKeys.length - 1].name;  // just the last key pressed
        skipTest1Instr.rt = _skipTest1Instr_allKeys[_skipTest1Instr_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *test1warning3* updates
    if (t >= 0 && test1warning3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1warning3.tStart = t;  // (not accounting for frame time here)
      test1warning3.frameNStart = frameN;  // exact frame index
      
      test1warning3.setAutoDraw(true);
    }

    frameRemains = 0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1warning3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1warning3.setAutoDraw(false);
    }
    
    // *test1warning2* updates
    if (t >= 60 && test1warning2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1warning2.tStart = t;  // (not accounting for frame time here)
      test1warning2.frameNStart = frameN;  // exact frame index
      
      test1warning2.setAutoDraw(true);
    }

    frameRemains = 60 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1warning2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1warning2.setAutoDraw(false);
    }
    
    // *test1warning1* updates
    if (t >= 120 && test1warning1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1warning1.tStart = t;  // (not accounting for frame time here)
      test1warning1.frameNStart = frameN;  // exact frame index
      
      test1warning1.setAutoDraw(true);
    }

    frameRemains = 120 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1warning1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1warning1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test1waitComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function test1waitRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'test1wait'-------
    for (const thisComponent of test1waitComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('skipTest1Instr.keys', skipTest1Instr.keys);
    if (typeof skipTest1Instr.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('skipTest1Instr.rt', skipTest1Instr.rt);
        routineTimer.reset();
        }
    
    skipTest1Instr.stop();
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var test1instrComponents;
function test1instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'test1instr'-------
    t = 0;
    test1instrClock.reset(); // clock
    frameN = -1;
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    test1instrComponents = [];
    test1instrComponents.push(test1Text);
    test1instrComponents.push(key_resp);
    
    for (const thisComponent of test1instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function test1instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'test1instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = test1instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *test1Text* updates
    if (t >= 0.0 && test1Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Text.tStart = t;  // (not accounting for frame time here)
      test1Text.frameNStart = frameN;  // exact frame index
      
      test1Text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Text.setAutoDraw(false);
    }
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: [], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test1instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function test1instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'test1instr'-------
    for (const thisComponent of test1instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    return Scheduler.Event.NEXT;
  };
}


var _test1Response_allKeys;
var test1Components;
function test1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'test1'-------
    t = 0;
    test1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    test1Audio1 = new sound.Sound({
    win: psychoJS.window,
    value: firstAudio,
    secs: -1,
    });
    test1Audio1.setVolume(1);
    test1Audio1Sound.setImage('sound.png');
    test1Audio1Mute.setImage('mute.png');
    test1Audio2 = new sound.Sound({
    win: psychoJS.window,
    value: secondAudio,
    secs: -1,
    });
    test1Audio2.setVolume(1);
    test1Audio2Mute1.setImage('mute.png');
    test1Audio2Sound.setImage('sound.png');
    test1Audio2Mute2.setImage('mute.png');
    test1Response.keys = undefined;
    test1Response.rt = undefined;
    _test1Response_allKeys = [];
    test1Image.setImage(imageLoc);
    // keep track of which components have finished
    test1Components = [];
    test1Components.push(test1Audio1);
    test1Components.push(test1Audio1Sound);
    test1Components.push(test1Audio1Mute);
    test1Components.push(test1Audio2);
    test1Components.push(test1Audio2Mute1);
    test1Components.push(test1Audio2Sound);
    test1Components.push(test1Audio2Mute2);
    test1Components.push(test1Response);
    test1Components.push(test1Image);
    test1Components.push(test1F);
    test1Components.push(test1J);
    test1Components.push(test1Instr);
    
    for (const thisComponent of test1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function test1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'test1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = test1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop test1Audio1
    if (t >= 0.5 && test1Audio1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Audio1.tStart = t;  // (not accounting for frame time here)
      test1Audio1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ test1Audio1.play(); });  // screen flip
      test1Audio1.status = PsychoJS.Status.STARTED;
    }
    if (t >= (test1Audio1.getDuration() + test1Audio1.tStart)     && test1Audio1.status === PsychoJS.Status.STARTED) {
      test1Audio1.stop();  // stop the sound (if longer than duration)
      test1Audio1.status = PsychoJS.Status.FINISHED;
    }
    
    // *test1Audio1Sound* updates
    if (t >= 0.5 && test1Audio1Sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Audio1Sound.tStart = t;  // (not accounting for frame time here)
      test1Audio1Sound.frameNStart = frameN;  // exact frame index
      
      test1Audio1Sound.setAutoDraw(true);
    }

    frameRemains = 0.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Audio1Sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Audio1Sound.setAutoDraw(false);
    }
    
    // *test1Audio1Mute* updates
    if (t >= 1.5 && test1Audio1Mute.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Audio1Mute.tStart = t;  // (not accounting for frame time here)
      test1Audio1Mute.frameNStart = frameN;  // exact frame index
      
      test1Audio1Mute.setAutoDraw(true);
    }

    frameRemains = 1.5 + 18.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Audio1Mute.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Audio1Mute.setAutoDraw(false);
    }
    // start/stop test1Audio2
    if (t >= 2.5 && test1Audio2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Audio2.tStart = t;  // (not accounting for frame time here)
      test1Audio2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ test1Audio2.play(); });  // screen flip
      test1Audio2.status = PsychoJS.Status.STARTED;
    }
    if (t >= (test1Audio2.getDuration() + test1Audio2.tStart)     && test1Audio2.status === PsychoJS.Status.STARTED) {
      test1Audio2.stop();  // stop the sound (if longer than duration)
      test1Audio2.status = PsychoJS.Status.FINISHED;
    }
    
    // *test1Audio2Mute1* updates
    if (t >= 0.5 && test1Audio2Mute1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Audio2Mute1.tStart = t;  // (not accounting for frame time here)
      test1Audio2Mute1.frameNStart = frameN;  // exact frame index
      
      test1Audio2Mute1.setAutoDraw(true);
    }

    frameRemains = 0.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Audio2Mute1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Audio2Mute1.setAutoDraw(false);
    }
    
    // *test1Audio2Sound* updates
    if (t >= 2.5 && test1Audio2Sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Audio2Sound.tStart = t;  // (not accounting for frame time here)
      test1Audio2Sound.frameNStart = frameN;  // exact frame index
      
      test1Audio2Sound.setAutoDraw(true);
    }

    frameRemains = 2.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Audio2Sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Audio2Sound.setAutoDraw(false);
    }
    
    // *test1Audio2Mute2* updates
    if (t >= 3.5 && test1Audio2Mute2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Audio2Mute2.tStart = t;  // (not accounting for frame time here)
      test1Audio2Mute2.frameNStart = frameN;  // exact frame index
      
      test1Audio2Mute2.setAutoDraw(true);
    }

    frameRemains = 3.5 + 16.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Audio2Mute2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Audio2Mute2.setAutoDraw(false);
    }
    
    // *test1Response* updates
    if (t >= 3.5 && test1Response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Response.tStart = t;  // (not accounting for frame time here)
      test1Response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { test1Response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { test1Response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { test1Response.clearEvents(); });
    }

    frameRemains = 3.5 + 16.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Response.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Response.status = PsychoJS.Status.FINISHED;
  }

    if (test1Response.status === PsychoJS.Status.STARTED) {
      let theseKeys = test1Response.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _test1Response_allKeys = _test1Response_allKeys.concat(theseKeys);
      if (_test1Response_allKeys.length > 0) {
        test1Response.keys = _test1Response_allKeys[_test1Response_allKeys.length - 1].name;  // just the last key pressed
        test1Response.rt = _test1Response_allKeys[_test1Response_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *test1Image* updates
    if (t >= 0.0 && test1Image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Image.tStart = t;  // (not accounting for frame time here)
      test1Image.frameNStart = frameN;  // exact frame index
      
      test1Image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Image.setAutoDraw(false);
    }
    
    // *test1F* updates
    if (t >= 3.5 && test1F.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1F.tStart = t;  // (not accounting for frame time here)
      test1F.frameNStart = frameN;  // exact frame index
      
      test1F.setAutoDraw(true);
    }

    frameRemains = 3.5 + 16.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1F.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1F.setAutoDraw(false);
    }
    
    // *test1J* updates
    if (t >= 3.5 && test1J.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1J.tStart = t;  // (not accounting for frame time here)
      test1J.frameNStart = frameN;  // exact frame index
      
      test1J.setAutoDraw(true);
    }

    frameRemains = 3.5 + 16.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1J.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1J.setAutoDraw(false);
    }
    
    // *test1Instr* updates
    if (t >= 0.0 && test1Instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Instr.tStart = t;  // (not accounting for frame time here)
      test1Instr.frameNStart = frameN;  // exact frame index
      
      test1Instr.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Instr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Instr.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function test1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'test1'-------
    for (const thisComponent of test1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    test1Audio1.stop();  // ensure sound has stopped at end of routine
    test1Audio2.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('test1Response.keys', test1Response.keys);
    if (typeof test1Response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('test1Response.rt', test1Response.rt);
        routineTimer.reset();
        }
    
    test1Response.stop();
    // the Routine "test1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _skipTest2Instr_allKeys;
var test2waitComponents;
function test2waitRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'test2wait'-------
    t = 0;
    test2waitClock.reset(); // clock
    frameN = -1;
    routineTimer.add(180.000000);
    // update component parameters for each repeat
    skipTest2Instr.keys = undefined;
    skipTest2Instr.rt = undefined;
    _skipTest2Instr_allKeys = [];
    // keep track of which components have finished
    test2waitComponents = [];
    test2waitComponents.push(skipTest2Instr);
    test2waitComponents.push(test2warning3);
    test2waitComponents.push(test2warning2);
    test2waitComponents.push(test2warning1);
    
    for (const thisComponent of test2waitComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function test2waitRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'test2wait'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = test2waitClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *skipTest2Instr* updates
    if (t >= 0.0 && skipTest2Instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      skipTest2Instr.tStart = t;  // (not accounting for frame time here)
      skipTest2Instr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { skipTest2Instr.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { skipTest2Instr.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { skipTest2Instr.clearEvents(); });
    }

    frameRemains = 0.0 + 180 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (skipTest2Instr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      skipTest2Instr.status = PsychoJS.Status.FINISHED;
  }

    if (skipTest2Instr.status === PsychoJS.Status.STARTED) {
      let theseKeys = skipTest2Instr.getKeys({keyList: [], waitRelease: false});
      _skipTest2Instr_allKeys = _skipTest2Instr_allKeys.concat(theseKeys);
      if (_skipTest2Instr_allKeys.length > 0) {
        skipTest2Instr.keys = _skipTest2Instr_allKeys[_skipTest2Instr_allKeys.length - 1].name;  // just the last key pressed
        skipTest2Instr.rt = _skipTest2Instr_allKeys[_skipTest2Instr_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *test2warning3* updates
    if (t >= 0 && test2warning3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2warning3.tStart = t;  // (not accounting for frame time here)
      test2warning3.frameNStart = frameN;  // exact frame index
      
      test2warning3.setAutoDraw(true);
    }

    frameRemains = 0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2warning3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2warning3.setAutoDraw(false);
    }
    
    // *test2warning2* updates
    if (t >= 60 && test2warning2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2warning2.tStart = t;  // (not accounting for frame time here)
      test2warning2.frameNStart = frameN;  // exact frame index
      
      test2warning2.setAutoDraw(true);
    }

    frameRemains = 60 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2warning2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2warning2.setAutoDraw(false);
    }
    
    // *test2warning1* updates
    if (t >= 120 && test2warning1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2warning1.tStart = t;  // (not accounting for frame time here)
      test2warning1.frameNStart = frameN;  // exact frame index
      
      test2warning1.setAutoDraw(true);
    }

    frameRemains = 120 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2warning1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2warning1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test2waitComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function test2waitRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'test2wait'-------
    for (const thisComponent of test2waitComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('skipTest2Instr.keys', skipTest2Instr.keys);
    if (typeof skipTest2Instr.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('skipTest2Instr.rt', skipTest2Instr.rt);
        routineTimer.reset();
        }
    
    skipTest2Instr.stop();
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var test2instrComponents;
function test2instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'test2instr'-------
    t = 0;
    test2instrClock.reset(); // clock
    frameN = -1;
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    test2instrComponents = [];
    test2instrComponents.push(test2Text);
    test2instrComponents.push(key_resp_2);
    
    for (const thisComponent of test2instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function test2instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'test2instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = test2instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *test2Text* updates
    if (t >= 0.0 && test2Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2Text.tStart = t;  // (not accounting for frame time here)
      test2Text.frameNStart = frameN;  // exact frame index
      
      test2Text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2Text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2Text.setAutoDraw(false);
    }
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_2.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: [], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test2instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function test2instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'test2instr'-------
    for (const thisComponent of test2instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    return Scheduler.Event.NEXT;
  };
}


var _test2Response_allKeys;
var test2Components;
function test2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'test2'-------
    t = 0;
    test2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    test2Audio1 = new sound.Sound({
    win: psychoJS.window,
    value: firstAudio,
    secs: -1,
    });
    test2Audio1.setVolume(1);
    test2Audio1Sound.setImage('sound.png');
    test1Audio2Mute.setImage('mute.png');
    test2Audio2 = new sound.Sound({
    win: psychoJS.window,
    value: secondAudio,
    secs: -1,
    });
    test2Audio2.setVolume(1);
    test2Audio2Mute1.setImage('mute.png');
    test2Audio2Sound.setImage('sound.png');
    test2Response.keys = undefined;
    test2Response.rt = undefined;
    _test2Response_allKeys = [];
    test2Image.setImage(imageLoc);
    // keep track of which components have finished
    test2Components = [];
    test2Components.push(test2Audio1);
    test2Components.push(test2Audio1Sound);
    test2Components.push(test1Audio2Mute);
    test2Components.push(test2Audio2);
    test2Components.push(test2Audio2Mute1);
    test2Components.push(test2Audio2Sound);
    test2Components.push(test2Audio2Mute2);
    test2Components.push(test2Response);
    test2Components.push(test2Image);
    test2Components.push(test2F);
    test2Components.push(test2J);
    test2Components.push(test2Instr);
    
    for (const thisComponent of test2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function test2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'test2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = test2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop test2Audio1
    if (t >= 0.5 && test2Audio1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2Audio1.tStart = t;  // (not accounting for frame time here)
      test2Audio1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ test2Audio1.play(); });  // screen flip
      test2Audio1.status = PsychoJS.Status.STARTED;
    }
    if (t >= (test2Audio1.getDuration() + test2Audio1.tStart)     && test2Audio1.status === PsychoJS.Status.STARTED) {
      test2Audio1.stop();  // stop the sound (if longer than duration)
      test2Audio1.status = PsychoJS.Status.FINISHED;
    }
    
    // *test2Audio1Sound* updates
    if (t >= 0.5 && test2Audio1Sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2Audio1Sound.tStart = t;  // (not accounting for frame time here)
      test2Audio1Sound.frameNStart = frameN;  // exact frame index
      
      test2Audio1Sound.setAutoDraw(true);
    }

    frameRemains = 0.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2Audio1Sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2Audio1Sound.setAutoDraw(false);
    }
    
    // *test1Audio2Mute* updates
    if (t >= 1.5 && test1Audio2Mute.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Audio2Mute.tStart = t;  // (not accounting for frame time here)
      test1Audio2Mute.frameNStart = frameN;  // exact frame index
      
      test1Audio2Mute.setAutoDraw(true);
    }

    frameRemains = 1.5 + 18.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Audio2Mute.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Audio2Mute.setAutoDraw(false);
    }
    // start/stop test2Audio2
    if (t >= 2.5 && test2Audio2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2Audio2.tStart = t;  // (not accounting for frame time here)
      test2Audio2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ test2Audio2.play(); });  // screen flip
      test2Audio2.status = PsychoJS.Status.STARTED;
    }
    if (t >= (test2Audio2.getDuration() + test2Audio2.tStart)     && test2Audio2.status === PsychoJS.Status.STARTED) {
      test2Audio2.stop();  // stop the sound (if longer than duration)
      test2Audio2.status = PsychoJS.Status.FINISHED;
    }
    
    // *test2Audio2Mute1* updates
    if (t >= 0.5 && test2Audio2Mute1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2Audio2Mute1.tStart = t;  // (not accounting for frame time here)
      test2Audio2Mute1.frameNStart = frameN;  // exact frame index
      
      test2Audio2Mute1.setAutoDraw(true);
    }

    frameRemains = 0.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2Audio2Mute1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2Audio2Mute1.setAutoDraw(false);
    }
    
    // *test2Audio2Sound* updates
    if (t >= 2.5 && test2Audio2Sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2Audio2Sound.tStart = t;  // (not accounting for frame time here)
      test2Audio2Sound.frameNStart = frameN;  // exact frame index
      
      test2Audio2Sound.setAutoDraw(true);
    }

    frameRemains = 2.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2Audio2Sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2Audio2Sound.setAutoDraw(false);
    }
    
    // *test2Audio2Mute2* updates
    if (t >= 3.5 && test2Audio2Mute2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2Audio2Mute2.tStart = t;  // (not accounting for frame time here)
      test2Audio2Mute2.frameNStart = frameN;  // exact frame index
      
      test2Audio2Mute2.setAutoDraw(true);
    }

    frameRemains = 3.5 + 16.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2Audio2Mute2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2Audio2Mute2.setAutoDraw(false);
    }
    
    // *test2Response* updates
    if (t >= 3.5 && test2Response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2Response.tStart = t;  // (not accounting for frame time here)
      test2Response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { test2Response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { test2Response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { test2Response.clearEvents(); });
    }

    frameRemains = 3.5 + 16.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2Response.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2Response.status = PsychoJS.Status.FINISHED;
  }

    if (test2Response.status === PsychoJS.Status.STARTED) {
      let theseKeys = test2Response.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _test2Response_allKeys = _test2Response_allKeys.concat(theseKeys);
      if (_test2Response_allKeys.length > 0) {
        test2Response.keys = _test2Response_allKeys[_test2Response_allKeys.length - 1].name;  // just the last key pressed
        test2Response.rt = _test2Response_allKeys[_test2Response_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *test2Image* updates
    if (t >= 0.0 && test2Image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2Image.tStart = t;  // (not accounting for frame time here)
      test2Image.frameNStart = frameN;  // exact frame index
      
      test2Image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2Image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2Image.setAutoDraw(false);
    }
    
    // *test2F* updates
    if (t >= 3.5 && test2F.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2F.tStart = t;  // (not accounting for frame time here)
      test2F.frameNStart = frameN;  // exact frame index
      
      test2F.setAutoDraw(true);
    }

    frameRemains = 3.5 + 16.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2F.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2F.setAutoDraw(false);
    }
    
    // *test2J* updates
    if (t >= 3.5 && test2J.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2J.tStart = t;  // (not accounting for frame time here)
      test2J.frameNStart = frameN;  // exact frame index
      
      test2J.setAutoDraw(true);
    }

    frameRemains = 3.5 + 16.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2J.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2J.setAutoDraw(false);
    }
    
    // *test2Instr* updates
    if (t >= 0.0 && test2Instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2Instr.tStart = t;  // (not accounting for frame time here)
      test2Instr.frameNStart = frameN;  // exact frame index
      
      test2Instr.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2Instr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2Instr.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function test2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'test2'-------
    for (const thisComponent of test2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    test2Audio1.stop();  // ensure sound has stopped at end of routine
    test2Audio2.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('test2Response.keys', test2Response.keys);
    if (typeof test2Response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('test2Response.rt', test2Response.rt);
        routineTimer.reset();
        }
    
    test2Response.stop();
    // the Routine "test2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _skipTest3Instr_allKeys;
var test3waitComponents;
function test3waitRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'test3wait'-------
    t = 0;
    test3waitClock.reset(); // clock
    frameN = -1;
    routineTimer.add(180.000000);
    // update component parameters for each repeat
    skipTest3Instr.keys = undefined;
    skipTest3Instr.rt = undefined;
    _skipTest3Instr_allKeys = [];
    // keep track of which components have finished
    test3waitComponents = [];
    test3waitComponents.push(skipTest3Instr);
    test3waitComponents.push(test3warning3);
    test3waitComponents.push(test3warning2);
    test3waitComponents.push(test3warning1);
    
    for (const thisComponent of test3waitComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function test3waitRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'test3wait'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = test3waitClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *skipTest3Instr* updates
    if (t >= 0.0 && skipTest3Instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      skipTest3Instr.tStart = t;  // (not accounting for frame time here)
      skipTest3Instr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { skipTest3Instr.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { skipTest3Instr.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { skipTest3Instr.clearEvents(); });
    }

    frameRemains = 0.0 + 180 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (skipTest3Instr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      skipTest3Instr.status = PsychoJS.Status.FINISHED;
  }

    if (skipTest3Instr.status === PsychoJS.Status.STARTED) {
      let theseKeys = skipTest3Instr.getKeys({keyList: [], waitRelease: false});
      _skipTest3Instr_allKeys = _skipTest3Instr_allKeys.concat(theseKeys);
      if (_skipTest3Instr_allKeys.length > 0) {
        skipTest3Instr.keys = _skipTest3Instr_allKeys[_skipTest3Instr_allKeys.length - 1].name;  // just the last key pressed
        skipTest3Instr.rt = _skipTest3Instr_allKeys[_skipTest3Instr_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *test3warning3* updates
    if (t >= 0 && test3warning3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3warning3.tStart = t;  // (not accounting for frame time here)
      test3warning3.frameNStart = frameN;  // exact frame index
      
      test3warning3.setAutoDraw(true);
    }

    frameRemains = 0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3warning3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3warning3.setAutoDraw(false);
    }
    
    // *test3warning2* updates
    if (t >= 60 && test3warning2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3warning2.tStart = t;  // (not accounting for frame time here)
      test3warning2.frameNStart = frameN;  // exact frame index
      
      test3warning2.setAutoDraw(true);
    }

    frameRemains = 60 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3warning2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3warning2.setAutoDraw(false);
    }
    
    // *test3warning1* updates
    if (t >= 120 && test3warning1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3warning1.tStart = t;  // (not accounting for frame time here)
      test3warning1.frameNStart = frameN;  // exact frame index
      
      test3warning1.setAutoDraw(true);
    }

    frameRemains = 120 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3warning1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3warning1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test3waitComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function test3waitRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'test3wait'-------
    for (const thisComponent of test3waitComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('skipTest3Instr.keys', skipTest3Instr.keys);
    if (typeof skipTest3Instr.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('skipTest3Instr.rt', skipTest3Instr.rt);
        routineTimer.reset();
        }
    
    skipTest3Instr.stop();
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var test3instrComponents;
function test3instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'test3instr'-------
    t = 0;
    test3instrClock.reset(); // clock
    frameN = -1;
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    test3instrComponents = [];
    test3instrComponents.push(test3Text);
    test3instrComponents.push(key_resp_3);
    
    for (const thisComponent of test3instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function test3instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'test3instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = test3instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *test3Text* updates
    if (t >= 0.0 && test3Text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Text.tStart = t;  // (not accounting for frame time here)
      test3Text.frameNStart = frameN;  // exact frame index
      
      test3Text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3Text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3Text.setAutoDraw(false);
    }
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_3.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: [], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test3instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function test3instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'test3instr'-------
    for (const thisComponent of test3instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    return Scheduler.Event.NEXT;
  };
}


var _test3Response_allKeys;
var test3Components;
function test3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'test3'-------
    t = 0;
    test3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    test3Audio1 = new sound.Sound({
    win: psychoJS.window,
    value: firstAudio,
    secs: -1,
    });
    test3Audio1.setVolume(1);
    test3Audio1Sound.setImage('sound.png');
    test3Audio1Mute.setImage('mute.png');
    test3Audio2 = new sound.Sound({
    win: psychoJS.window,
    value: secondAudio,
    secs: -1,
    });
    test3Audio2.setVolume(1);
    test3Audio2Mute1.setImage('mute.png');
    test3Audio2Sound.setImage('sound.png');
    test3Audio2Mute2.setImage('mute.png');
    test3Response.keys = undefined;
    test3Response.rt = undefined;
    _test3Response_allKeys = [];
    test3Image.setImage(imageLoc);
    // keep track of which components have finished
    test3Components = [];
    test3Components.push(test3Audio1);
    test3Components.push(test3Audio1Sound);
    test3Components.push(test3Audio1Mute);
    test3Components.push(test3Audio2);
    test3Components.push(test3Audio2Mute1);
    test3Components.push(test3Audio2Sound);
    test3Components.push(test3Audio2Mute2);
    test3Components.push(test3Response);
    test3Components.push(test3Image);
    test3Components.push(test3F);
    test3Components.push(test3J);
    test3Components.push(test3Instr);
    
    for (const thisComponent of test3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function test3RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'test3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = test3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop test3Audio1
    if (t >= 0.5 && test3Audio1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Audio1.tStart = t;  // (not accounting for frame time here)
      test3Audio1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ test3Audio1.play(); });  // screen flip
      test3Audio1.status = PsychoJS.Status.STARTED;
    }
    if (t >= (test3Audio1.getDuration() + test3Audio1.tStart)     && test3Audio1.status === PsychoJS.Status.STARTED) {
      test3Audio1.stop();  // stop the sound (if longer than duration)
      test3Audio1.status = PsychoJS.Status.FINISHED;
    }
    
    // *test3Audio1Sound* updates
    if (t >= 0.5 && test3Audio1Sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Audio1Sound.tStart = t;  // (not accounting for frame time here)
      test3Audio1Sound.frameNStart = frameN;  // exact frame index
      
      test3Audio1Sound.setAutoDraw(true);
    }

    frameRemains = 0.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3Audio1Sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3Audio1Sound.setAutoDraw(false);
    }
    
    // *test3Audio1Mute* updates
    if (t >= 1.5 && test3Audio1Mute.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Audio1Mute.tStart = t;  // (not accounting for frame time here)
      test3Audio1Mute.frameNStart = frameN;  // exact frame index
      
      test3Audio1Mute.setAutoDraw(true);
    }

    frameRemains = 1.5 + 18.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3Audio1Mute.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3Audio1Mute.setAutoDraw(false);
    }
    // start/stop test3Audio2
    if (t >= 2.5 && test3Audio2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Audio2.tStart = t;  // (not accounting for frame time here)
      test3Audio2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ test3Audio2.play(); });  // screen flip
      test3Audio2.status = PsychoJS.Status.STARTED;
    }
    if (t >= (test3Audio2.getDuration() + test3Audio2.tStart)     && test3Audio2.status === PsychoJS.Status.STARTED) {
      test3Audio2.stop();  // stop the sound (if longer than duration)
      test3Audio2.status = PsychoJS.Status.FINISHED;
    }
    
    // *test3Audio2Mute1* updates
    if (t >= 0.5 && test3Audio2Mute1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Audio2Mute1.tStart = t;  // (not accounting for frame time here)
      test3Audio2Mute1.frameNStart = frameN;  // exact frame index
      
      test3Audio2Mute1.setAutoDraw(true);
    }

    frameRemains = 0.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3Audio2Mute1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3Audio2Mute1.setAutoDraw(false);
    }
    
    // *test3Audio2Sound* updates
    if (t >= 2.5 && test3Audio2Sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Audio2Sound.tStart = t;  // (not accounting for frame time here)
      test3Audio2Sound.frameNStart = frameN;  // exact frame index
      
      test3Audio2Sound.setAutoDraw(true);
    }

    frameRemains = 2.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3Audio2Sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3Audio2Sound.setAutoDraw(false);
    }
    
    // *test3Audio2Mute2* updates
    if (t >= 3.5 && test3Audio2Mute2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Audio2Mute2.tStart = t;  // (not accounting for frame time here)
      test3Audio2Mute2.frameNStart = frameN;  // exact frame index
      
      test3Audio2Mute2.setAutoDraw(true);
    }

    frameRemains = 3.5 + 16.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3Audio2Mute2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3Audio2Mute2.setAutoDraw(false);
    }
    
    // *test3Response* updates
    if (t >= 3.5 && test3Response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Response.tStart = t;  // (not accounting for frame time here)
      test3Response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { test3Response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { test3Response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { test3Response.clearEvents(); });
    }

    frameRemains = 3.5 + 16.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3Response.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3Response.status = PsychoJS.Status.FINISHED;
  }

    if (test3Response.status === PsychoJS.Status.STARTED) {
      let theseKeys = test3Response.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _test3Response_allKeys = _test3Response_allKeys.concat(theseKeys);
      if (_test3Response_allKeys.length > 0) {
        test3Response.keys = _test3Response_allKeys[_test3Response_allKeys.length - 1].name;  // just the last key pressed
        test3Response.rt = _test3Response_allKeys[_test3Response_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *test3Image* updates
    if (t >= 0.0 && test3Image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Image.tStart = t;  // (not accounting for frame time here)
      test3Image.frameNStart = frameN;  // exact frame index
      
      test3Image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3Image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3Image.setAutoDraw(false);
    }
    
    // *test3F* updates
    if (t >= 3.5 && test3F.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3F.tStart = t;  // (not accounting for frame time here)
      test3F.frameNStart = frameN;  // exact frame index
      
      test3F.setAutoDraw(true);
    }

    frameRemains = 3.5 + 16.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3F.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3F.setAutoDraw(false);
    }
    
    // *test3J* updates
    if (t >= 3.5 && test3J.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3J.tStart = t;  // (not accounting for frame time here)
      test3J.frameNStart = frameN;  // exact frame index
      
      test3J.setAutoDraw(true);
    }

    frameRemains = 3.5 + 16.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3J.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3J.setAutoDraw(false);
    }
    
    // *test3Instr* updates
    if (t >= 0.0 && test3Instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Instr.tStart = t;  // (not accounting for frame time here)
      test3Instr.frameNStart = frameN;  // exact frame index
      
      test3Instr.setAutoDraw(true);
    }

    frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3Instr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3Instr.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function test3RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'test3'-------
    for (const thisComponent of test3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    test3Audio1.stop();  // ensure sound has stopped at end of routine
    test3Audio2.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('test3Response.keys', test3Response.keys);
    if (typeof test3Response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('test3Response.rt', test3Response.rt);
        routineTimer.reset();
        }
    
    test3Response.stop();
    // the Routine "test3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _skipPostTestInstr_allKeys;
var postTestInstrComponents;
function postTestInstrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'postTestInstr'-------
    t = 0;
    postTestInstrClock.reset(); // clock
    frameN = -1;
    routineTimer.add(180.000000);
    // update component parameters for each repeat
    skipPostTestInstr.keys = undefined;
    skipPostTestInstr.rt = undefined;
    _skipPostTestInstr_allKeys = [];
    // keep track of which components have finished
    postTestInstrComponents = [];
    postTestInstrComponents.push(skipPostTestInstr);
    postTestInstrComponents.push(postTestWarning3);
    postTestInstrComponents.push(postTestWarning2);
    postTestInstrComponents.push(postTestWarning1);
    
    for (const thisComponent of postTestInstrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function postTestInstrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'postTestInstr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = postTestInstrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *skipPostTestInstr* updates
    if (t >= 0.0 && skipPostTestInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      skipPostTestInstr.tStart = t;  // (not accounting for frame time here)
      skipPostTestInstr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { skipPostTestInstr.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { skipPostTestInstr.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { skipPostTestInstr.clearEvents(); });
    }

    frameRemains = 0.0 + 180 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (skipPostTestInstr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      skipPostTestInstr.status = PsychoJS.Status.FINISHED;
  }

    if (skipPostTestInstr.status === PsychoJS.Status.STARTED) {
      let theseKeys = skipPostTestInstr.getKeys({keyList: [], waitRelease: false});
      _skipPostTestInstr_allKeys = _skipPostTestInstr_allKeys.concat(theseKeys);
      if (_skipPostTestInstr_allKeys.length > 0) {
        skipPostTestInstr.keys = _skipPostTestInstr_allKeys[_skipPostTestInstr_allKeys.length - 1].name;  // just the last key pressed
        skipPostTestInstr.rt = _skipPostTestInstr_allKeys[_skipPostTestInstr_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *postTestWarning3* updates
    if (t >= 0 && postTestWarning3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postTestWarning3.tStart = t;  // (not accounting for frame time here)
      postTestWarning3.frameNStart = frameN;  // exact frame index
      
      postTestWarning3.setAutoDraw(true);
    }

    frameRemains = 0 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (postTestWarning3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      postTestWarning3.setAutoDraw(false);
    }
    
    // *postTestWarning2* updates
    if (t >= 60 && postTestWarning2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postTestWarning2.tStart = t;  // (not accounting for frame time here)
      postTestWarning2.frameNStart = frameN;  // exact frame index
      
      postTestWarning2.setAutoDraw(true);
    }

    frameRemains = 60 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (postTestWarning2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      postTestWarning2.setAutoDraw(false);
    }
    
    // *postTestWarning1* updates
    if (t >= 120 && postTestWarning1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postTestWarning1.tStart = t;  // (not accounting for frame time here)
      postTestWarning1.frameNStart = frameN;  // exact frame index
      
      postTestWarning1.setAutoDraw(true);
    }

    frameRemains = 120 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (postTestWarning1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      postTestWarning1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of postTestInstrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function postTestInstrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'postTestInstr'-------
    for (const thisComponent of postTestInstrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('skipPostTestInstr.keys', skipPostTestInstr.keys);
    if (typeof skipPostTestInstr.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('skipPostTestInstr.rt', skipPostTestInstr.rt);
        routineTimer.reset();
        }
    
    skipPostTestInstr.stop();
    return Scheduler.Event.NEXT;
  };
}


var _postTestResponse_allKeys;
var posttestComponents;
function posttestRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'posttest'-------
    t = 0;
    posttestClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    postTestResponse.keys = undefined;
    postTestResponse.rt = undefined;
    _postTestResponse_allKeys = [];
    postTestAudio1 = new sound.Sound({
    win: psychoJS.window,
    value: audioA,
    secs: -1,
    });
    postTestAudio1.setVolume(1);
    postTestAudio2 = new sound.Sound({
    win: psychoJS.window,
    value: audioX,
    secs: -1,
    });
    postTestAudio2.setVolume(1);
    postTestAudio3 = new sound.Sound({
    win: psychoJS.window,
    value: audioB,
    secs: -1,
    });
    postTestAudio3.setVolume(1);
    // keep track of which components have finished
    posttestComponents = [];
    posttestComponents.push(postTestResponse);
    posttestComponents.push(postTestAudio1);
    posttestComponents.push(fSound);
    posttestComponents.push(fMute);
    posttestComponents.push(postTestAudio2);
    posttestComponents.push(xMute1);
    posttestComponents.push(xSound);
    posttestComponents.push(xMute2);
    posttestComponents.push(postTestAudio3);
    posttestComponents.push(jMute1);
    posttestComponents.push(jSound);
    posttestComponents.push(jMute2);
    posttestComponents.push(textInstrPostTest);
    posttestComponents.push(fText);
    posttestComponents.push(xText);
    posttestComponents.push(jText);
    
    for (const thisComponent of posttestComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function posttestRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'posttest'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = posttestClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *postTestResponse* updates
    if (t >= 4.5 && postTestResponse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postTestResponse.tStart = t;  // (not accounting for frame time here)
      postTestResponse.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { postTestResponse.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { postTestResponse.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { postTestResponse.clearEvents(); });
    }

    frameRemains = 4.5 + 6.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (postTestResponse.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      postTestResponse.status = PsychoJS.Status.FINISHED;
  }

    if (postTestResponse.status === PsychoJS.Status.STARTED) {
      let theseKeys = postTestResponse.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _postTestResponse_allKeys = _postTestResponse_allKeys.concat(theseKeys);
      if (_postTestResponse_allKeys.length > 0) {
        postTestResponse.keys = _postTestResponse_allKeys[_postTestResponse_allKeys.length - 1].name;  // just the last key pressed
        postTestResponse.rt = _postTestResponse_allKeys[_postTestResponse_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // start/stop postTestAudio1
    if (t >= 0.5 && postTestAudio1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postTestAudio1.tStart = t;  // (not accounting for frame time here)
      postTestAudio1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ postTestAudio1.play(); });  // screen flip
      postTestAudio1.status = PsychoJS.Status.STARTED;
    }
    if (t >= (postTestAudio1.getDuration() + postTestAudio1.tStart)     && postTestAudio1.status === PsychoJS.Status.STARTED) {
      postTestAudio1.stop();  // stop the sound (if longer than duration)
      postTestAudio1.status = PsychoJS.Status.FINISHED;
    }
    
    // *fSound* updates
    if (t >= 0.5 && fSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fSound.tStart = t;  // (not accounting for frame time here)
      fSound.frameNStart = frameN;  // exact frame index
      
      fSound.setAutoDraw(true);
    }

    frameRemains = 0.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fSound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fSound.setAutoDraw(false);
    }
    
    // *fMute* updates
    if (t >= 1.5 && fMute.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fMute.tStart = t;  // (not accounting for frame time here)
      fMute.frameNStart = frameN;  // exact frame index
      
      fMute.setAutoDraw(true);
    }

    frameRemains = 1.5 + 9.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fMute.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fMute.setAutoDraw(false);
    }
    // start/stop postTestAudio2
    if (t >= 2 && postTestAudio2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postTestAudio2.tStart = t;  // (not accounting for frame time here)
      postTestAudio2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ postTestAudio2.play(); });  // screen flip
      postTestAudio2.status = PsychoJS.Status.STARTED;
    }
    if (t >= (postTestAudio2.getDuration() + postTestAudio2.tStart)     && postTestAudio2.status === PsychoJS.Status.STARTED) {
      postTestAudio2.stop();  // stop the sound (if longer than duration)
      postTestAudio2.status = PsychoJS.Status.FINISHED;
    }
    
    // *xMute1* updates
    if (t >= 0.5 && xMute1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      xMute1.tStart = t;  // (not accounting for frame time here)
      xMute1.frameNStart = frameN;  // exact frame index
      
      xMute1.setAutoDraw(true);
    }

    frameRemains = 0.5 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (xMute1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      xMute1.setAutoDraw(false);
    }
    
    // *xSound* updates
    if (t >= 2 && xSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      xSound.tStart = t;  // (not accounting for frame time here)
      xSound.frameNStart = frameN;  // exact frame index
      
      xSound.setAutoDraw(true);
    }

    frameRemains = 2 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (xSound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      xSound.setAutoDraw(false);
    }
    
    // *xMute2* updates
    if (t >= 3 && xMute2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      xMute2.tStart = t;  // (not accounting for frame time here)
      xMute2.frameNStart = frameN;  // exact frame index
      
      xMute2.setAutoDraw(true);
    }

    frameRemains = 3 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (xMute2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      xMute2.setAutoDraw(false);
    }
    // start/stop postTestAudio3
    if (t >= 3.5 && postTestAudio3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postTestAudio3.tStart = t;  // (not accounting for frame time here)
      postTestAudio3.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ postTestAudio3.play(); });  // screen flip
      postTestAudio3.status = PsychoJS.Status.STARTED;
    }
    if (t >= (postTestAudio3.getDuration() + postTestAudio3.tStart)     && postTestAudio3.status === PsychoJS.Status.STARTED) {
      postTestAudio3.stop();  // stop the sound (if longer than duration)
      postTestAudio3.status = PsychoJS.Status.FINISHED;
    }
    
    // *jMute1* updates
    if (t >= 0.5 && jMute1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      jMute1.tStart = t;  // (not accounting for frame time here)
      jMute1.frameNStart = frameN;  // exact frame index
      
      jMute1.setAutoDraw(true);
    }

    frameRemains = 0.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (jMute1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      jMute1.setAutoDraw(false);
    }
    
    // *jSound* updates
    if (t >= 3.5 && jSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      jSound.tStart = t;  // (not accounting for frame time here)
      jSound.frameNStart = frameN;  // exact frame index
      
      jSound.setAutoDraw(true);
    }

    frameRemains = 3.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (jSound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      jSound.setAutoDraw(false);
    }
    
    // *jMute2* updates
    if (t >= 4.5 && jMute2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      jMute2.tStart = t;  // (not accounting for frame time here)
      jMute2.frameNStart = frameN;  // exact frame index
      
      jMute2.setAutoDraw(true);
    }

    frameRemains = 4.5 + 6.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (jMute2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      jMute2.setAutoDraw(false);
    }
    
    // *textInstrPostTest* updates
    if (t >= 0.0 && textInstrPostTest.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textInstrPostTest.tStart = t;  // (not accounting for frame time here)
      textInstrPostTest.frameNStart = frameN;  // exact frame index
      
      textInstrPostTest.setAutoDraw(true);
    }

    frameRemains = 0.0 + 11 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textInstrPostTest.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textInstrPostTest.setAutoDraw(false);
    }
    
    // *fText* updates
    if (t >= 0.0 && fText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fText.tStart = t;  // (not accounting for frame time here)
      fText.frameNStart = frameN;  // exact frame index
      
      fText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 11 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fText.setAutoDraw(false);
    }
    
    // *xText* updates
    if (t >= 0.0 && xText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      xText.tStart = t;  // (not accounting for frame time here)
      xText.frameNStart = frameN;  // exact frame index
      
      xText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 11 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (xText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      xText.setAutoDraw(false);
    }
    
    // *jText* updates
    if (t >= 0.0 && jText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      jText.tStart = t;  // (not accounting for frame time here)
      jText.frameNStart = frameN;  // exact frame index
      
      jText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 11 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (jText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      jText.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of posttestComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function posttestRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'posttest'-------
    for (const thisComponent of posttestComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('postTestResponse.keys', postTestResponse.keys);
    if (typeof postTestResponse.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('postTestResponse.rt', postTestResponse.rt);
        routineTimer.reset();
        }
    
    postTestResponse.stop();
    postTestAudio1.stop();  // ensure sound has stopped at end of routine
    postTestAudio2.stop();  // ensure sound has stopped at end of routine
    postTestAudio3.stop();  // ensure sound has stopped at end of routine
    // the Routine "posttest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _quit_allKeys;
var thankuserComponents;
function thankuserRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'thankuser'-------
    t = 0;
    thankuserClock.reset(); // clock
    frameN = -1;
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    quit.keys = undefined;
    quit.rt = undefined;
    _quit_allKeys = [];
    // keep track of which components have finished
    thankuserComponents = [];
    thankuserComponents.push(text);
    thankuserComponents.push(quit);
    
    for (const thisComponent of thankuserComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function thankuserRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'thankuser'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = thankuserClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    
    // *quit* updates
    if (t >= 0.0 && quit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      quit.tStart = t;  // (not accounting for frame time here)
      quit.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { quit.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { quit.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { quit.clearEvents(); });
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (quit.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      quit.status = PsychoJS.Status.FINISHED;
  }

    if (quit.status === PsychoJS.Status.STARTED) {
      let theseKeys = quit.getKeys({keyList: [], waitRelease: false});
      _quit_allKeys = _quit_allKeys.concat(theseKeys);
      if (_quit_allKeys.length > 0) {
        quit.keys = _quit_allKeys[_quit_allKeys.length - 1].name;  // just the last key pressed
        quit.rt = _quit_allKeys[_quit_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of thankuserComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function thankuserRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'thankuser'-------
    for (const thisComponent of thankuserComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('quit.keys', quit.keys);
    if (typeof quit.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('quit.rt', quit.rt);
        routineTimer.reset();
        }
    
    quit.stop();
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
