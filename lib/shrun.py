""" https://gist.github.com/1978810
shutil.runret() and shutil.runout() functions
 
runret(command)   - run command through shell, return ret code
runout(command)   - run command through shell, return output
 
Public Domain, i.e. free for copy/paste

https://groups.google.com/d/topic/python-ideas/u42aZZnrs8A/discussion
"""
 
import subprocess

class OutErrRet(object):
  """Container object to return input, output and return code
     from runout call.
  """
  cmd = ''
  out = ''
  err = ''
  ret = 0


def runret(command):
  """ Run command through shell, return ret code """
  # [ ] silence all output
  return subprocess.call(command, shell=True)
 
def runout(command):
  """ Run command through shell, return output (stdout + stderr)
 
  [ ] cyclic buffer reader in separate thread to avoid deadlock
      if process writes too much
  """
  ret = OutErrRet()
  ret.cmd = command
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
  try:   
      ret.out, ret.err = process.communicate()
  except KeyboardInterrupt:
      pass

  ret.ret = process.returncode
  return ret


# https://gist.github.com/4368898
# Public domain code by anatoly techtonik <techtonik@gmail.com>
 
import os
import sys

def which(executable, path=None):
    """Try to find 'executable' in the directories listed in 'path' (a
    string listing directories separated by 'os.pathsep'; defaults to
    os.environ['PATH']).  Returns the complete filename or None if not
    found
    """
    if path is None:
        path = os.environ['PATH']
    paths = path.split(os.pathsep)
    extlist = ['']
    if os.name == 'os2':
        (base, ext) = os.path.splitext(executable)
        # executable files on OS/2 can have an arbitrary extension, but
        # .exe is automatically appended if no dot is present in the name
        if not ext:
            executable = executable + ".exe"
    elif sys.platform == 'win32':
        pathext = os.environ['PATHEXT'].lower().split(os.pathsep)
        (base, ext) = os.path.splitext(executable)
        if ext.lower() not in pathext:
            extlist = pathext
    for ext in extlist:
        execname = executable + ext
        if os.path.isfile(execname):
            return execname
        else:
            for p in paths:
                f = os.path.join(p, execname)
                if os.path.isfile(f):
                    return f
    else:
        return None
 
# which('sox')