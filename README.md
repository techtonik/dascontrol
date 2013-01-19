dascontrol
==========

Computer listens people.


Proof of concept
================

[x] Get voice sample
[x] Convert sample into text (recognize)
[ ] Select command (match)
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
[ ] Matcher    (sample.txt -> action.txt)
[x] Executor   (action.txt -> ...)


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


Phase Two
=========
Requisites:
 * Python
   * setuptools
   * requests
   * PyAudio
     > python -m easy_install pyaudio

Go cross-platform
[x] Python (Lin/Win/OS) recording
[ ] Python Google API request (requests lib)
[x] Python Action Executor
[ ] JSON Action Map


Phase Three
===========
Graphics UI
  * pyglet/pygame
  * or anything (web/kivy + websockets)

[ ] three static screens
[ ] state machine
[ ] animations
