import sys
import os

#find script location
if getattr(sys, "frozen", False):
    # check application or script file
    # if app, pyinstaller extends sys module by a flag frozen=True and sets the app path into variable _MEIPASS
    current_dir = os.path.dirname(sys.executable)
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))
