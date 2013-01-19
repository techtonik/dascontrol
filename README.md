dascontrol
==========

Computer listens people.


Proof of concept
================

[ ] Get voice sample
[ ] Convert sample into text (recognize)
[ ] Select command (match)
[ ] Execute command


User experience
===============
[ ] Single top level command to start the process
[ ] Signal to start and end recording
[ ] Show "..processing.." state while recognizing
[ ] Show text


Components
==========
[ ] (UI) Recorder (press button -- record -- unpress)
[ ] Recognizer
[ ] Matcher
[ ] Executor


Out of scope
=============
[ ] Continuous voice scan
     (no technology available, no time to reseach
      current version of Sphinx CMU)


Phase One
=========
Requisites:
 * Linux
 * curl
 * jshon
 * sox

Every component is shell script:
[x] Console scripts
[x] sox as a prerequisite


Phase Two
=========
Requisites:
 * Python
   * requests
   * PyAudio

Go cross-platform
[ ] Python (Lin/Win/OS) recording
[ ] Python Google API request (requests lib)
[ ] Python Action Executor
[ ] JSON Action Map


Phase Three
===========
Graphics UI
  * pyglet/pygame
  * or anything (web/kivy + websockets)

[ ] three static screens
[ ] state machine
[ ] animations
