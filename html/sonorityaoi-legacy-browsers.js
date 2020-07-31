﻿/******************** 
 * Sonorityaoi Test *
 ********************/

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
let expName = 'sonorityaoi';  // from the Builder filename that created this script
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
const train1blocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(train1blocksLoopBegin, train1blocksLoopScheduler);
flowScheduler.add(train1blocksLoopScheduler);
flowScheduler.add(train1blocksLoopEnd);
flowScheduler.add(instr2RoutineBegin());
flowScheduler.add(instr2RoutineEachFrame());
flowScheduler.add(instr2RoutineEnd());
const train2blocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(train2blocksLoopBegin, train2blocksLoopScheduler);
flowScheduler.add(train2blocksLoopScheduler);
flowScheduler.add(train2blocksLoopEnd);
flowScheduler.add(testTrainInstrRoutineBegin());
flowScheduler.add(testTrainInstrRoutineEachFrame());
flowScheduler.add(testTrainInstrRoutineEnd());
const test1LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(test1LoopLoopBegin, test1LoopLoopScheduler);
flowScheduler.add(test1LoopLoopScheduler);
flowScheduler.add(test1LoopLoopEnd);
flowScheduler.add(testNovel1InstrRoutineBegin());
flowScheduler.add(testNovel1InstrRoutineEachFrame());
flowScheduler.add(testNovel1InstrRoutineEnd());
const test2LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(test2LoopLoopBegin, test2LoopLoopScheduler);
flowScheduler.add(test2LoopLoopScheduler);
flowScheduler.add(test2LoopLoopEnd);
flowScheduler.add(testNovel2InstrRoutineBegin());
flowScheduler.add(testNovel2InstrRoutineEachFrame());
flowScheduler.add(testNovel2InstrRoutineEnd());
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
var train1Clock;
var imagetrain1;
var stimuli1train1;
var stimuli2train1;
var stimuli3train1;
var stimuli4train1;
var stimuli5train1;
var trainquestions1Clock;
var stimulitest1;
var correct;
var incorrect;
var train1Response;
var instr2Clock;
var train2warning10;
var train2warning5;
var train2warning4;
var train2warning3;
var train2warning2;
var train2warning1;
var skipTrain2Instr;
var train2Clock;
var imagetrain2;
var stimuli1train2;
var stimuli2train2;
var stimuli3train2;
var stimuli4train2;
var stimuli5train2;
var trainquestions2Clock;
var stimulitest2;
var correct2;
var incorrect2;
var train2Response;
var testTrainInstrClock;
var skipTest1Instr;
var test1warning10;
var test1warning5;
var test1warning4;
var test1warning3;
var test1warning2;
var test1warning1;
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
var testNovel1InstrClock;
var skipTest2Instr;
var test2warning10;
var test2warning5;
var test2warning4;
var test2warning3;
var test2warning2;
var test2warning1;
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
var testNovel2InstrClock;
var skipTest3Instr;
var test3warning10;
var test3warning5;
var test3warning4;
var test3warning3;
var test3warning2;
var test3warning1;
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
var postTestInstrClock;
var skipPostTestInstr;
var postTestWarning10;
var postTestWarning5;
var postTestWarning4;
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
var textInstructionsPostTest;
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
    text: 'Welcome and thank you for participating!\n\nInstructions will go here',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  advanceTrain1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "train1"
  train1Clock = new util.Clock();
  imagetrain1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imagetrain1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  stimuli1train1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimuli1train1.setVolume(1);
  stimuli2train1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimuli2train1.setVolume(1);
  stimuli3train1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimuli3train1.setVolume(1);
  stimuli4train1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimuli4train1.setVolume(1);
  stimuli5train1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stimuli5train1.setVolume(1);
  // Initialize components for Routine "trainquestions1"
  trainquestions1Clock = new util.Clock();
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
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  incorrect = new visual.ImageStim({
    win : psychoJS.window,
    name : 'incorrect', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  train1Response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instr2"
  instr2Clock = new util.Clock();
  train2warning10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'train2warning10',
    text: 'Next part will  start automatically\nin less than 10 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  train2warning5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'train2warning5',
    text: 'Next part will  start automatically\nin less than 5 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  train2warning4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'train2warning4',
    text: 'Next part will  start automatically\nin less than 4 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  train2warning3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'train2warning3',
    text: 'Next part will  start automatically\nin less than 3 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  train2warning2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'train2warning2',
    text: 'Next part will  start automatically\nin less than 2 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  train2warning1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'train2warning1',
    text: 'Next part will  start automatically\nin less than 1 minute.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  skipTrain2Instr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "train2"
  train2Clock = new util.Clock();
  imagetrain2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imagetrain2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
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
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  incorrect2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'incorrect2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  train2Response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "testTrainInstr"
  testTrainInstrClock = new util.Clock();
  skipTest1Instr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  test1warning10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test1warning10',
    text: 'Next part will  start automatically\nin less than 10 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  test1warning5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test1warning5',
    text: 'Next part will  start automatically\nin less than 5 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  test1warning4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test1warning4',
    text: 'Next part will  start automatically\nin less than 4 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  test1warning3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test1warning3',
    text: 'Next part will  start automatically\nin less than 3 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  test1warning2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test1warning2',
    text: 'Next part will  start automatically\nin less than 2 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  test1warning1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test1warning1',
    text: 'Next part will  start automatically\nin less than 1 minute.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
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
    ori : 0, pos : [0, 0.2], size : [0.4, 0.4],
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
  
  // Initialize components for Routine "testNovel1Instr"
  testNovel1InstrClock = new util.Clock();
  skipTest2Instr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  test2warning10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test2warning10',
    text: 'Next part will  start automatically\nin less than 10 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  test2warning5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test2warning5',
    text: 'Next part will  start automatically\nin less than 5 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  test2warning4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test2warning4',
    text: 'Next part will  start automatically\nin less than 4 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  test2warning3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test2warning3',
    text: 'Next part will  start automatically\nin less than 3 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  test2warning2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test2warning2',
    text: 'Next part will  start automatically\nin less than 2 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  test2warning1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test2warning1',
    text: 'Next part will  start automatically\nin less than 1 minute.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
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
    ori : 0, pos : [0, 0.2], size : [0.4, 0.4],
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
  
  // Initialize components for Routine "testNovel2Instr"
  testNovel2InstrClock = new util.Clock();
  skipTest3Instr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  test3warning10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test3warning10',
    text: 'Next part will  start automatically\nin less than 10 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  test3warning5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test3warning5',
    text: 'Next part will  start automatically\nin less than 5 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  test3warning4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test3warning4',
    text: 'Next part will  start automatically\nin less than 4 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  test3warning3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test3warning3',
    text: 'Next part will  start automatically\nin less than 3 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  test3warning2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test3warning2',
    text: 'Next part will  start automatically\nin less than 2 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  test3warning1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'test3warning1',
    text: 'Next part will  start automatically\nin less than 1 minute.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
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
    ori : 0, pos : [0, 0.2], size : [0.4, 0.4],
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
  
  // Initialize components for Routine "postTestInstr"
  postTestInstrClock = new util.Clock();
  skipPostTestInstr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  postTestWarning10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'postTestWarning10',
    text: 'Next part will  start automatically\nin less than 10 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  postTestWarning5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'postTestWarning5',
    text: 'Next part will  start automatically\nin less than 5 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  postTestWarning4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'postTestWarning4',
    text: 'Next part will  start automatically\nin less than 4 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  postTestWarning3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'postTestWarning3',
    text: 'Next part will  start automatically\nin less than 3 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  postTestWarning2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'postTestWarning2',
    text: 'Next part will  start automatically\nin less than 2 minutes.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  postTestWarning1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'postTestWarning1',
    text: 'Next part will  start automatically\nin less than 1 minute.\n\nPress any button to start now',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
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
  textInstructionsPostTest = new visual.TextStim({
    win: psychoJS.window,
    name: 'textInstructionsPostTest',
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
    text: 'Thank you for participating!\n\nPress any button to end this experiment',
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
    
    instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var train1blocks;
var currentLoop;
function train1blocksLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  train1blocks = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'aoiConditions/train1LoopCondition.xlsx',
    seed: undefined, name: 'train1blocks'
  });
  psychoJS.experiment.addLoop(train1blocks); // add the loop to the experiment
  currentLoop = train1blocks;  // we're now the current loop

  // Schedule all the trials in the trialList:
  train1blocks.forEach(function() {
    const snapshot = train1blocks.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    const blockwords1LoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(blockwords1LoopBegin, blockwords1LoopScheduler);
    thisScheduler.add(blockwords1LoopScheduler);
    thisScheduler.add(blockwords1LoopEnd);
    const blocktest1LoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(blocktest1LoopBegin, blocktest1LoopScheduler);
    thisScheduler.add(blocktest1LoopScheduler);
    thisScheduler.add(blocktest1LoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var blockwords1;
function blockwords1LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  blockwords1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: condFiles,
    seed: undefined, name: 'blockwords1'
  });
  psychoJS.experiment.addLoop(blockwords1); // add the loop to the experiment
  currentLoop = blockwords1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  blockwords1.forEach(function() {
    const snapshot = blockwords1.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(train1RoutineBegin(snapshot));
    thisScheduler.add(train1RoutineEachFrame(snapshot));
    thisScheduler.add(train1RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function blockwords1LoopEnd() {
  psychoJS.experiment.removeLoop(blockwords1);

  return Scheduler.Event.NEXT;
}


var blocktest1;
function blocktest1LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  blocktest1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: testFiles,
    seed: undefined, name: 'blocktest1'
  });
  psychoJS.experiment.addLoop(blocktest1); // add the loop to the experiment
  currentLoop = blocktest1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  blocktest1.forEach(function() {
    const snapshot = blocktest1.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trainquestions1RoutineBegin(snapshot));
    thisScheduler.add(trainquestions1RoutineEachFrame(snapshot));
    thisScheduler.add(trainquestions1RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function blocktest1LoopEnd() {
  psychoJS.experiment.removeLoop(blocktest1);

  return Scheduler.Event.NEXT;
}


function train1blocksLoopEnd() {
  psychoJS.experiment.removeLoop(train1blocks);

  return Scheduler.Event.NEXT;
}


var train2blocks;
function train2blocksLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  train2blocks = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'aoiConditions/train2LoopCondition.xlsx',
    seed: undefined, name: 'train2blocks'
  });
  psychoJS.experiment.addLoop(train2blocks); // add the loop to the experiment
  currentLoop = train2blocks;  // we're now the current loop

  // Schedule all the trials in the trialList:
  train2blocks.forEach(function() {
    const snapshot = train2blocks.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    const blockloop2LoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(blockloop2LoopBegin, blockloop2LoopScheduler);
    thisScheduler.add(blockloop2LoopScheduler);
    thisScheduler.add(blockloop2LoopEnd);
    const blocktest2LoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(blocktest2LoopBegin, blocktest2LoopScheduler);
    thisScheduler.add(blocktest2LoopScheduler);
    thisScheduler.add(blocktest2LoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var blockloop2;
function blockloop2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  blockloop2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: condFiles,
    seed: undefined, name: 'blockloop2'
  });
  psychoJS.experiment.addLoop(blockloop2); // add the loop to the experiment
  currentLoop = blockloop2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  blockloop2.forEach(function() {
    const snapshot = blockloop2.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(train2RoutineBegin(snapshot));
    thisScheduler.add(train2RoutineEachFrame(snapshot));
    thisScheduler.add(train2RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function blockloop2LoopEnd() {
  psychoJS.experiment.removeLoop(blockloop2);

  return Scheduler.Event.NEXT;
}


var blocktest2;
function blocktest2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  blocktest2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: testFiles,
    seed: undefined, name: 'blocktest2'
  });
  psychoJS.experiment.addLoop(blocktest2); // add the loop to the experiment
  currentLoop = blocktest2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  blocktest2.forEach(function() {
    const snapshot = blocktest2.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trainquestions2RoutineBegin(snapshot));
    thisScheduler.add(trainquestions2RoutineEachFrame(snapshot));
    thisScheduler.add(trainquestions2RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function blocktest2LoopEnd() {
  psychoJS.experiment.removeLoop(blocktest2);

  return Scheduler.Event.NEXT;
}


function train2blocksLoopEnd() {
  psychoJS.experiment.removeLoop(train2blocks);

  return Scheduler.Event.NEXT;
}


var test1Loop;
function test1LoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  test1Loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'aoiConditions/test1Conditions.xlsx',
    seed: undefined, name: 'test1Loop'
  });
  psychoJS.experiment.addLoop(test1Loop); // add the loop to the experiment
  currentLoop = test1Loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  test1Loop.forEach(function() {
    const snapshot = test1Loop.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(test1RoutineBegin(snapshot));
    thisScheduler.add(test1RoutineEachFrame(snapshot));
    thisScheduler.add(test1RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

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
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'aoiConditions/test2Conditions.xlsx',
    seed: undefined, name: 'test2Loop'
  });
  psychoJS.experiment.addLoop(test2Loop); // add the loop to the experiment
  currentLoop = test2Loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  test2Loop.forEach(function() {
    const snapshot = test2Loop.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(test2RoutineBegin(snapshot));
    thisScheduler.add(test2RoutineEachFrame(snapshot));
    thisScheduler.add(test2RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

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
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'aoiConditions/test3Conditions.xlsx',
    seed: undefined, name: 'test3Loop'
  });
  psychoJS.experiment.addLoop(test3Loop); // add the loop to the experiment
  currentLoop = test3Loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  test3Loop.forEach(function() {
    const snapshot = test3Loop.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(test3RoutineBegin(snapshot));
    thisScheduler.add(test3RoutineEachFrame(snapshot));
    thisScheduler.add(test3RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

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
  postTestLoop.forEach(function() {
    const snapshot = postTestLoop.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(posttestRoutineBegin(snapshot));
    thisScheduler.add(posttestRoutineEachFrame(snapshot));
    thisScheduler.add(posttestRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function postTestLoopLoopEnd() {
  psychoJS.experiment.removeLoop(postTestLoop);

  return Scheduler.Event.NEXT;
}


var train1Components;
function train1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'train1'-------
    t = 0;
    train1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    imagetrain1.setImage(imageLoc);
    stimuli1train1 = new sound.Sound({
    win: psychoJS.window,
    value: audio,
    secs: -1,
    });
    stimuli1train1.setVolume(1);
    stimuli2train1 = new sound.Sound({
    win: psychoJS.window,
    value: audio,
    secs: -1,
    });
    stimuli2train1.setVolume(1);
    stimuli3train1 = new sound.Sound({
    win: psychoJS.window,
    value: audio,
    secs: -1,
    });
    stimuli3train1.setVolume(1);
    stimuli4train1 = new sound.Sound({
    win: psychoJS.window,
    value: audio,
    secs: -1,
    });
    stimuli4train1.setVolume(1);
    stimuli5train1 = new sound.Sound({
    win: psychoJS.window,
    value: audio,
    secs: -1,
    });
    stimuli5train1.setVolume(1);
    // keep track of which components have finished
    train1Components = [];
    train1Components.push(imagetrain1);
    train1Components.push(stimuli1train1);
    train1Components.push(stimuli2train1);
    train1Components.push(stimuli3train1);
    train1Components.push(stimuli4train1);
    train1Components.push(stimuli5train1);
    
    train1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function train1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'train1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = train1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *imagetrain1* updates
    if (t >= 2 && imagetrain1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imagetrain1.tStart = t;  // (not accounting for frame time here)
      imagetrain1.frameNStart = frameN;  // exact frame index
      
      imagetrain1.setAutoDraw(true);
    }

    frameRemains = 2 + 9 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imagetrain1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imagetrain1.setAutoDraw(false);
    }
    // start/stop stimuli1train1
    if (t >= 2 && stimuli1train1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli1train1.tStart = t;  // (not accounting for frame time here)
      stimuli1train1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimuli1train1.play(); });  // screen flip
      stimuli1train1.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimuli1train1.getDuration() + stimuli1train1.tStart)     && stimuli1train1.status === PsychoJS.Status.STARTED) {
      stimuli1train1.stop();  // stop the sound (if longer than duration)
      stimuli1train1.status = PsychoJS.Status.FINISHED;
    }
    // start/stop stimuli2train1
    if (t >= 4 && stimuli2train1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli2train1.tStart = t;  // (not accounting for frame time here)
      stimuli2train1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimuli2train1.play(); });  // screen flip
      stimuli2train1.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimuli2train1.getDuration() + stimuli2train1.tStart)     && stimuli2train1.status === PsychoJS.Status.STARTED) {
      stimuli2train1.stop();  // stop the sound (if longer than duration)
      stimuli2train1.status = PsychoJS.Status.FINISHED;
    }
    // start/stop stimuli3train1
    if (t >= 6 && stimuli3train1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli3train1.tStart = t;  // (not accounting for frame time here)
      stimuli3train1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimuli3train1.play(); });  // screen flip
      stimuli3train1.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimuli3train1.getDuration() + stimuli3train1.tStart)     && stimuli3train1.status === PsychoJS.Status.STARTED) {
      stimuli3train1.stop();  // stop the sound (if longer than duration)
      stimuli3train1.status = PsychoJS.Status.FINISHED;
    }
    // start/stop stimuli4train1
    if (t >= 8 && stimuli4train1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli4train1.tStart = t;  // (not accounting for frame time here)
      stimuli4train1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimuli4train1.play(); });  // screen flip
      stimuli4train1.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimuli4train1.getDuration() + stimuli4train1.tStart)     && stimuli4train1.status === PsychoJS.Status.STARTED) {
      stimuli4train1.stop();  // stop the sound (if longer than duration)
      stimuli4train1.status = PsychoJS.Status.FINISHED;
    }
    // start/stop stimuli5train1
    if (t >= 10 && stimuli5train1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimuli5train1.tStart = t;  // (not accounting for frame time here)
      stimuli5train1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stimuli5train1.play(); });  // screen flip
      stimuli5train1.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stimuli5train1.getDuration() + stimuli5train1.tStart)     && stimuli5train1.status === PsychoJS.Status.STARTED) {
      stimuli5train1.stop();  // stop the sound (if longer than duration)
      stimuli5train1.status = PsychoJS.Status.FINISHED;
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
    train1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    train1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    stimuli1train1.stop();  // ensure sound has stopped at end of routine
    stimuli2train1.stop();  // ensure sound has stopped at end of routine
    stimuli3train1.stop();  // ensure sound has stopped at end of routine
    stimuli4train1.stop();  // ensure sound has stopped at end of routine
    stimuli5train1.stop();  // ensure sound has stopped at end of routine
    // the Routine "train1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _train1Response_allKeys;
var trainquestions1Components;
function trainquestions1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trainquestions1'-------
    t = 0;
    trainquestions1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    stimulitest1 = new sound.Sound({
    win: psychoJS.window,
    value: audioTrue,
    secs: -1,
    });
    stimulitest1.setVolume(1);
    correct.setPos([truePos, 0]);
    correct.setImage(imageTrue);
    incorrect.setPos([falsePos, 0]);
    incorrect.setImage(imageFalse);
    train1Response.keys = undefined;
    train1Response.rt = undefined;
    _train1Response_allKeys = [];
    // keep track of which components have finished
    trainquestions1Components = [];
    trainquestions1Components.push(stimulitest1);
    trainquestions1Components.push(correct);
    trainquestions1Components.push(incorrect);
    trainquestions1Components.push(train1Response);
    
    trainquestions1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function trainquestions1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trainquestions1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trainquestions1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop stimulitest1
    if (t >= 0 && stimulitest1.status === PsychoJS.Status.NOT_STARTED) {
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
    if (t >= 0.0 && correct.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      correct.tStart = t;  // (not accounting for frame time here)
      correct.frameNStart = frameN;  // exact frame index
      
      correct.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (correct.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      correct.setAutoDraw(false);
    }
    
    // *incorrect* updates
    if (t >= 0.0 && incorrect.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      incorrect.tStart = t;  // (not accounting for frame time here)
      incorrect.frameNStart = frameN;  // exact frame index
      
      incorrect.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (incorrect.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      incorrect.setAutoDraw(false);
    }
    
    // *train1Response* updates
    if (t >= 1 && train1Response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train1Response.tStart = t;  // (not accounting for frame time here)
      train1Response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { train1Response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { train1Response.start(); }); // start on screen flip
    }

    frameRemains = 1 + 6.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trainquestions1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trainquestions1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trainquestions1'-------
    trainquestions1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    stimulitest1.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('train1Response.keys', train1Response.keys);
    if (typeof train1Response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('train1Response.rt', train1Response.rt);
        routineTimer.reset();
        }
    
    train1Response.stop();
    // the Routine "trainquestions1" was not non-slip safe, so reset the non-slip timer
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
    routineTimer.add(600.000000);
    // update component parameters for each repeat
    skipTrain2Instr.keys = undefined;
    skipTrain2Instr.rt = undefined;
    _skipTrain2Instr_allKeys = [];
    // keep track of which components have finished
    instr2Components = [];
    instr2Components.push(train2warning10);
    instr2Components.push(train2warning5);
    instr2Components.push(train2warning4);
    instr2Components.push(train2warning3);
    instr2Components.push(train2warning2);
    instr2Components.push(train2warning1);
    instr2Components.push(skipTrain2Instr);
    
    instr2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    
    // *train2warning10* updates
    if (t >= 0.0 && train2warning10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train2warning10.tStart = t;  // (not accounting for frame time here)
      train2warning10.frameNStart = frameN;  // exact frame index
      
      train2warning10.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train2warning10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train2warning10.setAutoDraw(false);
    }
    
    // *train2warning5* updates
    if (t >= 300 && train2warning5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train2warning5.tStart = t;  // (not accounting for frame time here)
      train2warning5.frameNStart = frameN;  // exact frame index
      
      train2warning5.setAutoDraw(true);
    }

    frameRemains = 300 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train2warning5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train2warning5.setAutoDraw(false);
    }
    
    // *train2warning4* updates
    if (t >= 360 && train2warning4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train2warning4.tStart = t;  // (not accounting for frame time here)
      train2warning4.frameNStart = frameN;  // exact frame index
      
      train2warning4.setAutoDraw(true);
    }

    frameRemains = 360 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train2warning4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train2warning4.setAutoDraw(false);
    }
    
    // *train2warning3* updates
    if (t >= 420 && train2warning3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train2warning3.tStart = t;  // (not accounting for frame time here)
      train2warning3.frameNStart = frameN;  // exact frame index
      
      train2warning3.setAutoDraw(true);
    }

    frameRemains = 420 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train2warning3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train2warning3.setAutoDraw(false);
    }
    
    // *train2warning2* updates
    if (t >= 480 && train2warning2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train2warning2.tStart = t;  // (not accounting for frame time here)
      train2warning2.frameNStart = frameN;  // exact frame index
      
      train2warning2.setAutoDraw(true);
    }

    frameRemains = 480 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (train2warning2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train2warning2.setAutoDraw(false);
    }
    
    // *train2warning1* updates
    if (t >= 540 && train2warning1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train2warning1.tStart = t;  // (not accounting for frame time here)
      train2warning1.frameNStart = frameN;  // exact frame index
      
      train2warning1.setAutoDraw(true);
    }

    frameRemains = 540 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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

    frameRemains = 0.0 + 600 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    instr2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    instr2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('skipTrain2Instr.keys', skipTrain2Instr.keys);
    if (typeof skipTrain2Instr.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('skipTrain2Instr.rt', skipTrain2Instr.rt);
        routineTimer.reset();
        }
    
    skipTrain2Instr.stop();
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
    
    train2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    train2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    train2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    correct2.setPos([truePos, 0]);
    correct2.setImage(imageTrue);
    incorrect2.setPos([falsePos, 0]);
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
    
    trainquestions2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    if (t >= 0.0 && stimulitest2.status === PsychoJS.Status.NOT_STARTED) {
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
    if (t >= 0.0 && correct2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      correct2.tStart = t;  // (not accounting for frame time here)
      correct2.frameNStart = frameN;  // exact frame index
      
      correct2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (correct2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      correct2.setAutoDraw(false);
    }
    
    // *incorrect2* updates
    if (t >= 0.0 && incorrect2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      incorrect2.tStart = t;  // (not accounting for frame time here)
      incorrect2.frameNStart = frameN;  // exact frame index
      
      incorrect2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (incorrect2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      incorrect2.setAutoDraw(false);
    }
    
    // *train2Response* updates
    if (t >= 1 && train2Response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train2Response.tStart = t;  // (not accounting for frame time here)
      train2Response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { train2Response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { train2Response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { train2Response.clearEvents(); });
    }

    frameRemains = 1 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trainquestions2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    trainquestions2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
var testTrainInstrComponents;
function testTrainInstrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'testTrainInstr'-------
    t = 0;
    testTrainInstrClock.reset(); // clock
    frameN = -1;
    routineTimer.add(600.000000);
    // update component parameters for each repeat
    skipTest1Instr.keys = undefined;
    skipTest1Instr.rt = undefined;
    _skipTest1Instr_allKeys = [];
    // keep track of which components have finished
    testTrainInstrComponents = [];
    testTrainInstrComponents.push(skipTest1Instr);
    testTrainInstrComponents.push(test1warning10);
    testTrainInstrComponents.push(test1warning5);
    testTrainInstrComponents.push(test1warning4);
    testTrainInstrComponents.push(test1warning3);
    testTrainInstrComponents.push(test1warning2);
    testTrainInstrComponents.push(test1warning1);
    
    testTrainInstrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function testTrainInstrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'testTrainInstr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = testTrainInstrClock.getTime();
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

    frameRemains = 0.0 + 600 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    
    
    // *test1warning10* updates
    if (t >= 0.0 && test1warning10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1warning10.tStart = t;  // (not accounting for frame time here)
      test1warning10.frameNStart = frameN;  // exact frame index
      
      test1warning10.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1warning10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1warning10.setAutoDraw(false);
    }
    
    // *test1warning5* updates
    if (t >= 300 && test1warning5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1warning5.tStart = t;  // (not accounting for frame time here)
      test1warning5.frameNStart = frameN;  // exact frame index
      
      test1warning5.setAutoDraw(true);
    }

    frameRemains = 300 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1warning5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1warning5.setAutoDraw(false);
    }
    
    // *test1warning4* updates
    if (t >= 360 && test1warning4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1warning4.tStart = t;  // (not accounting for frame time here)
      test1warning4.frameNStart = frameN;  // exact frame index
      
      test1warning4.setAutoDraw(true);
    }

    frameRemains = 360 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1warning4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1warning4.setAutoDraw(false);
    }
    
    // *test1warning3* updates
    if (t >= 420 && test1warning3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1warning3.tStart = t;  // (not accounting for frame time here)
      test1warning3.frameNStart = frameN;  // exact frame index
      
      test1warning3.setAutoDraw(true);
    }

    frameRemains = 420 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1warning3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1warning3.setAutoDraw(false);
    }
    
    // *test1warning2* updates
    if (t >= 480 && test1warning2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1warning2.tStart = t;  // (not accounting for frame time here)
      test1warning2.frameNStart = frameN;  // exact frame index
      
      test1warning2.setAutoDraw(true);
    }

    frameRemains = 480 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1warning2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1warning2.setAutoDraw(false);
    }
    
    // *test1warning1* updates
    if (t >= 540 && test1warning1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1warning1.tStart = t;  // (not accounting for frame time here)
      test1warning1.frameNStart = frameN;  // exact frame index
      
      test1warning1.setAutoDraw(true);
    }

    frameRemains = 540 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    testTrainInstrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function testTrainInstrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'testTrainInstr'-------
    testTrainInstrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('skipTest1Instr.keys', skipTest1Instr.keys);
    if (typeof skipTest1Instr.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('skipTest1Instr.rt', skipTest1Instr.rt);
        routineTimer.reset();
        }
    
    skipTest1Instr.stop();
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
    
    test1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    if (t >= 0 && test1Audio1.status === PsychoJS.Status.NOT_STARTED) {
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
    if (t >= 0.0 && test1Audio1Sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Audio1Sound.tStart = t;  // (not accounting for frame time here)
      test1Audio1Sound.frameNStart = frameN;  // exact frame index
      
      test1Audio1Sound.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Audio1Sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Audio1Sound.setAutoDraw(false);
    }
    
    // *test1Audio1Mute* updates
    if (t >= 1 && test1Audio1Mute.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Audio1Mute.tStart = t;  // (not accounting for frame time here)
      test1Audio1Mute.frameNStart = frameN;  // exact frame index
      
      test1Audio1Mute.setAutoDraw(true);
    }

    frameRemains = 1 + 9 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Audio1Mute.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Audio1Mute.setAutoDraw(false);
    }
    // start/stop test1Audio2
    if (t >= 1 && test1Audio2.status === PsychoJS.Status.NOT_STARTED) {
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
    if (t >= 0.0 && test1Audio2Mute1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Audio2Mute1.tStart = t;  // (not accounting for frame time here)
      test1Audio2Mute1.frameNStart = frameN;  // exact frame index
      
      test1Audio2Mute1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Audio2Mute1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Audio2Mute1.setAutoDraw(false);
    }
    
    // *test1Audio2Sound* updates
    if (t >= 1 && test1Audio2Sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Audio2Sound.tStart = t;  // (not accounting for frame time here)
      test1Audio2Sound.frameNStart = frameN;  // exact frame index
      
      test1Audio2Sound.setAutoDraw(true);
    }

    frameRemains = 1 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Audio2Sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Audio2Sound.setAutoDraw(false);
    }
    
    // *test1Audio2Mute2* updates
    if (t >= 2 && test1Audio2Mute2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Audio2Mute2.tStart = t;  // (not accounting for frame time here)
      test1Audio2Mute2.frameNStart = frameN;  // exact frame index
      
      test1Audio2Mute2.setAutoDraw(true);
    }

    frameRemains = 2 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Audio2Mute2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Audio2Mute2.setAutoDraw(false);
    }
    
    // *test1Response* updates
    if (t >= 2 && test1Response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Response.tStart = t;  // (not accounting for frame time here)
      test1Response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { test1Response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { test1Response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { test1Response.clearEvents(); });
    }

    frameRemains = 2 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Image.setAutoDraw(false);
    }
    
    // *test1F* updates
    if (t >= 0.0 && test1F.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1F.tStart = t;  // (not accounting for frame time here)
      test1F.frameNStart = frameN;  // exact frame index
      
      test1F.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1F.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1F.setAutoDraw(false);
    }
    
    // *test1J* updates
    if (t >= 0.0 && test1J.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1J.tStart = t;  // (not accounting for frame time here)
      test1J.frameNStart = frameN;  // exact frame index
      
      test1J.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1J.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1J.setAutoDraw(false);
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
    test1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    test1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
var testNovel1InstrComponents;
function testNovel1InstrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'testNovel1Instr'-------
    t = 0;
    testNovel1InstrClock.reset(); // clock
    frameN = -1;
    routineTimer.add(600.000000);
    // update component parameters for each repeat
    skipTest2Instr.keys = undefined;
    skipTest2Instr.rt = undefined;
    _skipTest2Instr_allKeys = [];
    // keep track of which components have finished
    testNovel1InstrComponents = [];
    testNovel1InstrComponents.push(skipTest2Instr);
    testNovel1InstrComponents.push(test2warning10);
    testNovel1InstrComponents.push(test2warning5);
    testNovel1InstrComponents.push(test2warning4);
    testNovel1InstrComponents.push(test2warning3);
    testNovel1InstrComponents.push(test2warning2);
    testNovel1InstrComponents.push(test2warning1);
    
    testNovel1InstrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function testNovel1InstrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'testNovel1Instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = testNovel1InstrClock.getTime();
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

    frameRemains = 0.0 + 600 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    
    
    // *test2warning10* updates
    if (t >= 0.0 && test2warning10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2warning10.tStart = t;  // (not accounting for frame time here)
      test2warning10.frameNStart = frameN;  // exact frame index
      
      test2warning10.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2warning10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2warning10.setAutoDraw(false);
    }
    
    // *test2warning5* updates
    if (t >= 300 && test2warning5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2warning5.tStart = t;  // (not accounting for frame time here)
      test2warning5.frameNStart = frameN;  // exact frame index
      
      test2warning5.setAutoDraw(true);
    }

    frameRemains = 300 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2warning5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2warning5.setAutoDraw(false);
    }
    
    // *test2warning4* updates
    if (t >= 360 && test2warning4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2warning4.tStart = t;  // (not accounting for frame time here)
      test2warning4.frameNStart = frameN;  // exact frame index
      
      test2warning4.setAutoDraw(true);
    }

    frameRemains = 360 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2warning4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2warning4.setAutoDraw(false);
    }
    
    // *test2warning3* updates
    if (t >= 420 && test2warning3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2warning3.tStart = t;  // (not accounting for frame time here)
      test2warning3.frameNStart = frameN;  // exact frame index
      
      test2warning3.setAutoDraw(true);
    }

    frameRemains = 420 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2warning3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2warning3.setAutoDraw(false);
    }
    
    // *test2warning2* updates
    if (t >= 480 && test2warning2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2warning2.tStart = t;  // (not accounting for frame time here)
      test2warning2.frameNStart = frameN;  // exact frame index
      
      test2warning2.setAutoDraw(true);
    }

    frameRemains = 480 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2warning2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2warning2.setAutoDraw(false);
    }
    
    // *test2warning1* updates
    if (t >= 540 && test2warning1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2warning1.tStart = t;  // (not accounting for frame time here)
      test2warning1.frameNStart = frameN;  // exact frame index
      
      test2warning1.setAutoDraw(true);
    }

    frameRemains = 540 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    testNovel1InstrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function testNovel1InstrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'testNovel1Instr'-------
    testNovel1InstrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('skipTest2Instr.keys', skipTest2Instr.keys);
    if (typeof skipTest2Instr.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('skipTest2Instr.rt', skipTest2Instr.rt);
        routineTimer.reset();
        }
    
    skipTest2Instr.stop();
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
    
    test2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    if (t >= 0.0 && test2Audio1.status === PsychoJS.Status.NOT_STARTED) {
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
    if (t >= 0.0 && test2Audio1Sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2Audio1Sound.tStart = t;  // (not accounting for frame time here)
      test2Audio1Sound.frameNStart = frameN;  // exact frame index
      
      test2Audio1Sound.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2Audio1Sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2Audio1Sound.setAutoDraw(false);
    }
    
    // *test1Audio2Mute* updates
    if (t >= 1 && test1Audio2Mute.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test1Audio2Mute.tStart = t;  // (not accounting for frame time here)
      test1Audio2Mute.frameNStart = frameN;  // exact frame index
      
      test1Audio2Mute.setAutoDraw(true);
    }

    frameRemains = 1 + 9 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test1Audio2Mute.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test1Audio2Mute.setAutoDraw(false);
    }
    // start/stop test2Audio2
    if (t >= 1 && test2Audio2.status === PsychoJS.Status.NOT_STARTED) {
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
    if (t >= 0.0 && test2Audio2Mute1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2Audio2Mute1.tStart = t;  // (not accounting for frame time here)
      test2Audio2Mute1.frameNStart = frameN;  // exact frame index
      
      test2Audio2Mute1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2Audio2Mute1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2Audio2Mute1.setAutoDraw(false);
    }
    
    // *test2Audio2Sound* updates
    if (t >= 1 && test2Audio2Sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2Audio2Sound.tStart = t;  // (not accounting for frame time here)
      test2Audio2Sound.frameNStart = frameN;  // exact frame index
      
      test2Audio2Sound.setAutoDraw(true);
    }

    frameRemains = 1 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2Audio2Sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2Audio2Sound.setAutoDraw(false);
    }
    
    // *test2Audio2Mute2* updates
    if (t >= 2 && test2Audio2Mute2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2Audio2Mute2.tStart = t;  // (not accounting for frame time here)
      test2Audio2Mute2.frameNStart = frameN;  // exact frame index
      
      test2Audio2Mute2.setAutoDraw(true);
    }

    frameRemains = 2 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2Audio2Mute2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2Audio2Mute2.setAutoDraw(false);
    }
    
    // *test2Response* updates
    if (t >= 2 && test2Response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2Response.tStart = t;  // (not accounting for frame time here)
      test2Response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { test2Response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { test2Response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { test2Response.clearEvents(); });
    }

    frameRemains = 2 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2Image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2Image.setAutoDraw(false);
    }
    
    // *test2F* updates
    if (t >= 0.0 && test2F.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2F.tStart = t;  // (not accounting for frame time here)
      test2F.frameNStart = frameN;  // exact frame index
      
      test2F.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2F.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2F.setAutoDraw(false);
    }
    
    // *test2J* updates
    if (t >= 0.0 && test2J.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test2J.tStart = t;  // (not accounting for frame time here)
      test2J.frameNStart = frameN;  // exact frame index
      
      test2J.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test2J.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test2J.setAutoDraw(false);
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
    test2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    test2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
var testNovel2InstrComponents;
function testNovel2InstrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'testNovel2Instr'-------
    t = 0;
    testNovel2InstrClock.reset(); // clock
    frameN = -1;
    routineTimer.add(600.000000);
    // update component parameters for each repeat
    skipTest3Instr.keys = undefined;
    skipTest3Instr.rt = undefined;
    _skipTest3Instr_allKeys = [];
    // keep track of which components have finished
    testNovel2InstrComponents = [];
    testNovel2InstrComponents.push(skipTest3Instr);
    testNovel2InstrComponents.push(test3warning10);
    testNovel2InstrComponents.push(test3warning5);
    testNovel2InstrComponents.push(test3warning4);
    testNovel2InstrComponents.push(test3warning3);
    testNovel2InstrComponents.push(test3warning2);
    testNovel2InstrComponents.push(test3warning1);
    
    testNovel2InstrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function testNovel2InstrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'testNovel2Instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = testNovel2InstrClock.getTime();
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

    frameRemains = 0.0 + 600 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    
    
    // *test3warning10* updates
    if (t >= 0.0 && test3warning10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3warning10.tStart = t;  // (not accounting for frame time here)
      test3warning10.frameNStart = frameN;  // exact frame index
      
      test3warning10.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3warning10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3warning10.setAutoDraw(false);
    }
    
    // *test3warning5* updates
    if (t >= 300 && test3warning5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3warning5.tStart = t;  // (not accounting for frame time here)
      test3warning5.frameNStart = frameN;  // exact frame index
      
      test3warning5.setAutoDraw(true);
    }

    frameRemains = 300 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3warning5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3warning5.setAutoDraw(false);
    }
    
    // *test3warning4* updates
    if (t >= 360 && test3warning4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3warning4.tStart = t;  // (not accounting for frame time here)
      test3warning4.frameNStart = frameN;  // exact frame index
      
      test3warning4.setAutoDraw(true);
    }

    frameRemains = 360 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3warning4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3warning4.setAutoDraw(false);
    }
    
    // *test3warning3* updates
    if (t >= 420 && test3warning3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3warning3.tStart = t;  // (not accounting for frame time here)
      test3warning3.frameNStart = frameN;  // exact frame index
      
      test3warning3.setAutoDraw(true);
    }

    frameRemains = 420 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3warning3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3warning3.setAutoDraw(false);
    }
    
    // *test3warning2* updates
    if (t >= 480 && test3warning2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3warning2.tStart = t;  // (not accounting for frame time here)
      test3warning2.frameNStart = frameN;  // exact frame index
      
      test3warning2.setAutoDraw(true);
    }

    frameRemains = 480 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3warning2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3warning2.setAutoDraw(false);
    }
    
    // *test3warning1* updates
    if (t >= 540 && test3warning1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3warning1.tStart = t;  // (not accounting for frame time here)
      test3warning1.frameNStart = frameN;  // exact frame index
      
      test3warning1.setAutoDraw(true);
    }

    frameRemains = 540 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    testNovel2InstrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function testNovel2InstrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'testNovel2Instr'-------
    testNovel2InstrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('skipTest3Instr.keys', skipTest3Instr.keys);
    if (typeof skipTest3Instr.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('skipTest3Instr.rt', skipTest3Instr.rt);
        routineTimer.reset();
        }
    
    skipTest3Instr.stop();
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
    
    test3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    if (t >= 0.0 && test3Audio1.status === PsychoJS.Status.NOT_STARTED) {
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
    if (t >= 0.0 && test3Audio1Sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Audio1Sound.tStart = t;  // (not accounting for frame time here)
      test3Audio1Sound.frameNStart = frameN;  // exact frame index
      
      test3Audio1Sound.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3Audio1Sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3Audio1Sound.setAutoDraw(false);
    }
    
    // *test3Audio1Mute* updates
    if (t >= 1 && test3Audio1Mute.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Audio1Mute.tStart = t;  // (not accounting for frame time here)
      test3Audio1Mute.frameNStart = frameN;  // exact frame index
      
      test3Audio1Mute.setAutoDraw(true);
    }

    frameRemains = 1 + 9 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3Audio1Mute.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3Audio1Mute.setAutoDraw(false);
    }
    // start/stop test3Audio2
    if (t >= 1 && test3Audio2.status === PsychoJS.Status.NOT_STARTED) {
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
    if (t >= 0.0 && test3Audio2Mute1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Audio2Mute1.tStart = t;  // (not accounting for frame time here)
      test3Audio2Mute1.frameNStart = frameN;  // exact frame index
      
      test3Audio2Mute1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3Audio2Mute1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3Audio2Mute1.setAutoDraw(false);
    }
    
    // *test3Audio2Sound* updates
    if (t >= 1 && test3Audio2Sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Audio2Sound.tStart = t;  // (not accounting for frame time here)
      test3Audio2Sound.frameNStart = frameN;  // exact frame index
      
      test3Audio2Sound.setAutoDraw(true);
    }

    frameRemains = 1 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3Audio2Sound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3Audio2Sound.setAutoDraw(false);
    }
    
    // *test3Audio2Mute2* updates
    if (t >= 2 && test3Audio2Mute2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Audio2Mute2.tStart = t;  // (not accounting for frame time here)
      test3Audio2Mute2.frameNStart = frameN;  // exact frame index
      
      test3Audio2Mute2.setAutoDraw(true);
    }

    frameRemains = 2 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3Audio2Mute2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3Audio2Mute2.setAutoDraw(false);
    }
    
    // *test3Response* updates
    if (t >= 2 && test3Response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3Response.tStart = t;  // (not accounting for frame time here)
      test3Response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { test3Response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { test3Response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { test3Response.clearEvents(); });
    }

    frameRemains = 2 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3Image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3Image.setAutoDraw(false);
    }
    
    // *test3F* updates
    if (t >= 0.0 && test3F.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3F.tStart = t;  // (not accounting for frame time here)
      test3F.frameNStart = frameN;  // exact frame index
      
      test3F.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3F.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3F.setAutoDraw(false);
    }
    
    // *test3J* updates
    if (t >= 0.0 && test3J.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      test3J.tStart = t;  // (not accounting for frame time here)
      test3J.frameNStart = frameN;  // exact frame index
      
      test3J.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (test3J.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      test3J.setAutoDraw(false);
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
    test3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    test3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    routineTimer.add(600.000000);
    // update component parameters for each repeat
    skipPostTestInstr.keys = undefined;
    skipPostTestInstr.rt = undefined;
    _skipPostTestInstr_allKeys = [];
    // keep track of which components have finished
    postTestInstrComponents = [];
    postTestInstrComponents.push(skipPostTestInstr);
    postTestInstrComponents.push(postTestWarning10);
    postTestInstrComponents.push(postTestWarning5);
    postTestInstrComponents.push(postTestWarning4);
    postTestInstrComponents.push(postTestWarning3);
    postTestInstrComponents.push(postTestWarning2);
    postTestInstrComponents.push(postTestWarning1);
    
    postTestInstrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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

    frameRemains = 0.0 + 600 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    
    
    // *postTestWarning10* updates
    if (t >= 0.0 && postTestWarning10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postTestWarning10.tStart = t;  // (not accounting for frame time here)
      postTestWarning10.frameNStart = frameN;  // exact frame index
      
      postTestWarning10.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (postTestWarning10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      postTestWarning10.setAutoDraw(false);
    }
    
    // *postTestWarning5* updates
    if (t >= 300 && postTestWarning5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postTestWarning5.tStart = t;  // (not accounting for frame time here)
      postTestWarning5.frameNStart = frameN;  // exact frame index
      
      postTestWarning5.setAutoDraw(true);
    }

    frameRemains = 300 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (postTestWarning5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      postTestWarning5.setAutoDraw(false);
    }
    
    // *postTestWarning4* updates
    if (t >= 360 && postTestWarning4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postTestWarning4.tStart = t;  // (not accounting for frame time here)
      postTestWarning4.frameNStart = frameN;  // exact frame index
      
      postTestWarning4.setAutoDraw(true);
    }

    frameRemains = 360 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (postTestWarning4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      postTestWarning4.setAutoDraw(false);
    }
    
    // *postTestWarning3* updates
    if (t >= 420 && postTestWarning3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postTestWarning3.tStart = t;  // (not accounting for frame time here)
      postTestWarning3.frameNStart = frameN;  // exact frame index
      
      postTestWarning3.setAutoDraw(true);
    }

    frameRemains = 420 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (postTestWarning3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      postTestWarning3.setAutoDraw(false);
    }
    
    // *postTestWarning2* updates
    if (t >= 480 && postTestWarning2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postTestWarning2.tStart = t;  // (not accounting for frame time here)
      postTestWarning2.frameNStart = frameN;  // exact frame index
      
      postTestWarning2.setAutoDraw(true);
    }

    frameRemains = 480 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (postTestWarning2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      postTestWarning2.setAutoDraw(false);
    }
    
    // *postTestWarning1* updates
    if (t >= 540 && postTestWarning1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postTestWarning1.tStart = t;  // (not accounting for frame time here)
      postTestWarning1.frameNStart = frameN;  // exact frame index
      
      postTestWarning1.setAutoDraw(true);
    }

    frameRemains = 540 + 60 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    postTestInstrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    postTestInstrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    value: audioB,
    secs: -1,
    });
    postTestAudio2.setVolume(1);
    postTestAudio3 = new sound.Sound({
    win: psychoJS.window,
    value: audioC,
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
    posttestComponents.push(textInstructionsPostTest);
    posttestComponents.push(fText);
    posttestComponents.push(xText);
    posttestComponents.push(jText);
    
    posttestComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    if (t >= 3 && postTestResponse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postTestResponse.tStart = t;  // (not accounting for frame time here)
      postTestResponse.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { postTestResponse.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { postTestResponse.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { postTestResponse.clearEvents(); });
    }

    frameRemains = 3 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    if (t >= 0.0 && postTestAudio1.status === PsychoJS.Status.NOT_STARTED) {
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
    if (t >= 0.0 && fSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fSound.tStart = t;  // (not accounting for frame time here)
      fSound.frameNStart = frameN;  // exact frame index
      
      fSound.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fSound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fSound.setAutoDraw(false);
    }
    
    // *fMute* updates
    if (t >= 1 && fMute.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fMute.tStart = t;  // (not accounting for frame time here)
      fMute.frameNStart = frameN;  // exact frame index
      
      fMute.setAutoDraw(true);
    }

    frameRemains = 1 + 9 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fMute.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fMute.setAutoDraw(false);
    }
    // start/stop postTestAudio2
    if (t >= 1 && postTestAudio2.status === PsychoJS.Status.NOT_STARTED) {
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
    if (t >= 0.0 && xMute1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      xMute1.tStart = t;  // (not accounting for frame time here)
      xMute1.frameNStart = frameN;  // exact frame index
      
      xMute1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (xMute1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      xMute1.setAutoDraw(false);
    }
    
    // *xSound* updates
    if (t >= 1 && xSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      xSound.tStart = t;  // (not accounting for frame time here)
      xSound.frameNStart = frameN;  // exact frame index
      
      xSound.setAutoDraw(true);
    }

    frameRemains = 1 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (xSound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      xSound.setAutoDraw(false);
    }
    
    // *xMute2* updates
    if (t >= 2 && xMute2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      xMute2.tStart = t;  // (not accounting for frame time here)
      xMute2.frameNStart = frameN;  // exact frame index
      
      xMute2.setAutoDraw(true);
    }

    frameRemains = 2 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (xMute2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      xMute2.setAutoDraw(false);
    }
    // start/stop postTestAudio3
    if (t >= 2 && postTestAudio3.status === PsychoJS.Status.NOT_STARTED) {
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
    if (t >= 0.0 && jMute1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      jMute1.tStart = t;  // (not accounting for frame time here)
      jMute1.frameNStart = frameN;  // exact frame index
      
      jMute1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (jMute1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      jMute1.setAutoDraw(false);
    }
    
    // *jSound* updates
    if (t >= 2 && jSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      jSound.tStart = t;  // (not accounting for frame time here)
      jSound.frameNStart = frameN;  // exact frame index
      
      jSound.setAutoDraw(true);
    }

    frameRemains = 2 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (jSound.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      jSound.setAutoDraw(false);
    }
    
    // *jMute2* updates
    if (t >= 3 && jMute2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      jMute2.tStart = t;  // (not accounting for frame time here)
      jMute2.frameNStart = frameN;  // exact frame index
      
      jMute2.setAutoDraw(true);
    }

    frameRemains = 3 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (jMute2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      jMute2.setAutoDraw(false);
    }
    
    // *textInstructionsPostTest* updates
    if (t >= 0.0 && textInstructionsPostTest.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textInstructionsPostTest.tStart = t;  // (not accounting for frame time here)
      textInstructionsPostTest.frameNStart = frameN;  // exact frame index
      
      textInstructionsPostTest.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textInstructionsPostTest.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textInstructionsPostTest.setAutoDraw(false);
    }
    
    // *fText* updates
    if (t >= 0.0 && fText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fText.tStart = t;  // (not accounting for frame time here)
      fText.frameNStart = frameN;  // exact frame index
      
      fText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    posttestComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    posttestComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    thankuserComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    thankuserComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    thankuserComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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