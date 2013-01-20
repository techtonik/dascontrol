#!/usr/bin/env python
# -*- coding: utf-8 -*-

INFILE = 'sample.txt'
OUTFILE = 'action.txt'

rules_trivial = {
  "сделай громче":  "sound.volume.inc",
  "сделай тише":    "sound.volume.dec",
  "запусти музыку": "music.start"
}


import sys

if len(sys.argv) < 2:
  # default is useful for debugging
  infile = INFILE
else:
  infile = sys.argv[1]

text = open(infile, 'rb').read()

for key in rules_trivial:
  if key == text:
    open(OUTFILE, 'wb').write(rules_trivial[key])
