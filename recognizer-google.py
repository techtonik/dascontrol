#!/usr/bin/env python
"""
Recognize sample.flac using Google API

FLAC 16000 is the only format that Google Recognition Engine accepts.


This is a replacement for the following Linux command:
# curl --data-binary @sample.flac --header "Content-type: audio/x-flac; rate=16000" "https://www.google.com/speech-api/v1/recognize?lang=ru-RU&client=chromium" 2>/dev/null\
# | tee /dev/tty|jshon -e hypotheses -e 0 -e utterance -u > sample.txt
"""

INFILE = 'sample.flac'
OUTFILE = 'sample.txt'

# --- hacking to use Python libraries from lib/ dir

import os
import sys

ROOT = os.path.abspath(os.path.dirname(__file__))
BIN = os.path.join(ROOT, 'bin')
LIB = os.path.join(ROOT, 'lib')
sys.path += [LIB]

import requests
import json

# --- make request to Google API
if len(sys.argv) < 2:
  # default is useful for debugging
  infile = INFILE
else:
  infile = sys.argv[1]


with open(infile, 'rb') as flac:
  r = requests.post('https://www.google.com/speech-api/v1/recognize?lang=ru-RU&client=chromium',
        data=flac, headers={'Content-type': 'audio/x-flac; rate=16000'})
if r.status_code == 400:
  # [ ] event to rerun record/recognition cycle process
  print("Recognition failed.")
  sys.exit(-1)
elif r.status_code != 200:
  print(r.status_code)
  print("Error accessing Google Voice Recognition API")
  #print(r.text.encode('utf-8'))
  sys.exit(r.status_code)

#print(r.text.encode('utf-8'))
resp = json.loads(r.text)
first_match = resp[u'hypotheses'][0][u'utterance']
#print(first_match.encode('utf-8'))

with open(OUTFILE, 'wb') as out:
  out.write(first_match.encode('utf-8'))

print("Recognized text is saved to %s" % OUTFILE)
