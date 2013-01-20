#!/usr/bin/env python
"""
Execute action specified in sample.txt

Actions are scripts in actions/ directory
"""

import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.dirname(__file__))
ACTIONDIR = os.path.join(ROOT, 'actions')

# --- process action
# read action
if len(sys.argv) < 2:
    # default is useful for debugging
    infile = "action.txt"
else:
    infile = sys.argv[1]

action = open(infile).read().strip()
print(action)

# look into actions/ dir and execute file under the given name
# detect how to execute the file by looking at its first line
action_script = os.path.join(ACTIONDIR, action)
if not os.path.exists(action_script):
    print("Unknown action '%s'" % action)
    sys.exit(-1)
else:
    python_signature = '#!/usr/bin/env python'
    signature = open(action_script).read(1024)
    command = None
    if signature.startswith(python_signature):
        command = [sys.executable] + [action_script]
    else:
        command = [action_script]
    # [ ] reuse asyncprocess
    process = subprocess.Popen(command, shell=True)
    out, err = process.communicate()
    if process.returncode != 0:
        sys.exit("Some error occured. Exiting.")
