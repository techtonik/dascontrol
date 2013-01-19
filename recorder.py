#!/usr/bin/env python
"""
Record sound from mic to sample.flac

FLAC is only needed if Google Recognition Engine is used.
"""

# hacking to use Python libraries from lib/ dir
import os
import sys

ROOT = os.path.abspath(os.path.dirname(__file__))
BIN = os.path.join(ROOT, 'bin')
LIB = os.path.join(ROOT, 'lib')
sys.path += [LIB]

from shrun import runret, runout, which


# --- Variant 1: Use sox to record to FLAC file
if len(sys.argv) < 2:
    # default is useful for debugging
    outfile = "sample.flac"
else:
    outfile = sys.argv[1]

# add local bin/ to PATH
os.environ['PATH'] += os.pathsep + BIN
sox = which("sox")
print("Recording.. Press Ctrl-C to stop.")
limit = 60
# [ ] sound end is stripped, because Ctrl-C kills sox too early,
#     try to control the process asynchronously (process.terminate())
#res = runout('"%s" -d -q --rate 16000 -t flac %s trim 0 %s' % (sox, outfile, limit))
res = runout('"%s" -d -q --rate 16000 -t flac %s' % (sox, outfile))
if res.ret not in (0, None):  # None returned on KeyboardInterrupt
    print(res.out)
    print(res.err)
    print(res.ret)
    print("Error running sox. Please check if sox is installed")
    print("or get it from http://sox.sourceforge.net/ and place")
    print("into bin directory of the current dir.")
    sys.exit(1)

print("Sample saved to " + outfile)

# --- Variant 2: Trying to record and encode to FLAC in pure Python

# This implementation proved itself unusable, because we need
# to install compiled binaries for PyAudio and bitarray for
# pure Python FLAC encoder.
#

"""
import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
"""