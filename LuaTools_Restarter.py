import subprocess
import os

# Path to the target executable
target_exe = os.path.join(os.getcwd(), "LuaTools.exe")

# Launch it
subprocess.Popen([target_exe], shell=True)
