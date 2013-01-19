#!/bin/sh

# [x] Recorder
# [x] Recognizer
# [ ] Matcher
# [x] Executor

# Recorder
python2 recorder.py sample.flac

# Recognizer
curl --data-binary @sample.flac -k --header "Content-type: audio/x-flac; rate=16000" "https://www.google.com/speech-api/v1/recognize?lang=ru-RU&client=chromium" | tee /dev/tty|jshon -e hypotheses -e 0 -e utterance -u > sample.txt

# [ ] Matcher
clisp matcher.lisp

# [x] Executor
python2 executor.py action.txt
