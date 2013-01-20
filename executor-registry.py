#!/usr/bin/env python
"""
Execute action specified in sample.txt

Action are hardcoded in registry list, which is filled with
object of Action type.
"""
import os
import sys

# hacking to use Python libraries from lib/ dir

ROOT = os.path.abspath(os.path.dirname(__file__))
BIN = os.path.join(ROOT, 'bin')
LIB = os.path.join(ROOT, 'lib')
sys.path += [LIB]

from shrun import runret, runout, which

class Action(object):
  """Action that executes program"""
  name = None
  command = None

  def __init__(self, name, command):
    self.name = name
    self.command = command

  def run(self):
    runret(command)

class PythonAction(object):
  def __init__(self, name, runnable):
    self.name = name
    self.run = runnable

# --- add actions

# music.start
def start_online_radio():
  import webbrowser
  webbrowser.open("http://www.4duk.ru/4duk/playerPage.action?play=true")
    
music_start = PythonAction('music.start', start_online_radio)

registry = []
registry.append(music_start)


# --- process action
# read action
if len(sys.argv) < 2:
  # default is useful for debugging
  infile = "action.txt"
else:
  infile = sys.argv[1]

action = open(infile).read().strip()
print(action)

# process hardcoded actions in this file
for act in registry:
  if act.name == action:
    act.run()
