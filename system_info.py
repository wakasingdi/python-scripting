import platform
import os
import sys

print ("Platform:", platform.system(), platform.release())
print("Machine:", platform.machine())
print("Python:", sys.version.split()[0])
print("Current dir:", os.getcwd())

import subprocess
print("uname -a:", subprocess.check_output(["uname", "-a"]).decode().strip())