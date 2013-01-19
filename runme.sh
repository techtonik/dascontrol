#!/bin/sh

# [x] Recorder
# [x] Recognizer
# [ ] Matcher
# [ ] Executor

# Recorder
rec -q sample.ogg

# Recognizer
sox sample.ogg -q --rate 16000 -t flac - 2>/dev/null| curl --data-binary @- --header 'Content-type: audio/x-flac; rate=16000' 'https://www.google.com/speech-api/v1/recognize?lang=ru-RU&client=chromium' 2>/dev/null | tee /dev/tty|jshon -e hypotheses -e 0 -e utterance -u > sample.txt

# [ ] Matcher
cp sample.txt action.txt

# [ ] Executor
cat action.txt
