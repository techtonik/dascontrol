dascontrol
==========

Computer listens people.

    > python RUNME.py


Proof of concept
================

    [x] Get voice sample
    [x] Convert sample into text (recognize)
    [x] Select command (match)
    [x] Execute command


User experience
===============

    [x] Single top level command to start the process
    [ ] Signal to start and end recording
    [ ] Show "..processing.." state while recognizing
    [ ] Show text


Components
==========

    [x] Recorder   (mic -> sample.wav)
      [ ] (lev.2) UI (press button -- record -- unpress)
    [x] Recognizer (sample.wav -> sample.txt)
    [x] Matcher    (sample.txt -> action.txt)
    [x] Executor   (action.txt -> ...)


Out of scope
=============

    [ ] Continuous voice scan
         (no technology available, no time to reseach
          current version of Sphinx CMU)


Phase One (Done)
================
Requisites:
 * Linux
 * curl
 * jshon
 * sox
 * clisp

Every component is shell script:

    [x] Console scripts


Phase Two (Done)
================
Requisites:
 * sox
 * Python

Go cross-platform

    [x] Python (Lin/Win/OS) recording
    [x] Python Google API request (requests lib)
    [x] Python Matcher
    [x] Python Action Executor


Phase Three
===========
Graphics UI
  * pyglet/pygame
  * or anything (web/kivy + websockets)

    [ ] three static screens
    [ ] state machine
    [ ] animations
