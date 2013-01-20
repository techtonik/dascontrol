#!/usr/bin/env python
"""
# [x] Recorder
# [x] Recognizer
# [x] Matcher
# [x] Executor

python recorder.py sample.flac
python recognizer-google.py sample.flac
python matcher.py
python executor.py action.txt

"""

# --- the code below to executes the stuff above in a cross-platform way

import sys
import subprocess

for cmd in __doc__.split('\n'):
  command = ''
  if cmd.startswith('#') or cmd.strip() == '':
    continue

  if cmd.startswith('python'):
    command = [sys.executable] + cmd.strip().split()[1:]

  #print(command)

  # [ ] Windows tested, not the best solution, probably
  # ignore Ctrl-C signal, which is then handled by the child process
  import signal
  signal.signal(signal.SIGINT, signal.SIG_IGN)

  process = subprocess.Popen(command, shell=True)
  try:
      out, err = process.communicate()
  except KeyboardInterrupt:
      pass
  if process.returncode != 0:
      sys.exit("Some error occured. Exiting.")
