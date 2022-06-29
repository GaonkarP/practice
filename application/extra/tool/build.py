import os
import sys
import shutil
import subprocess
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "python_scripts")))
# import helper

class buildwrapper:

    def __init__(self):
        self.rootfolder = os.path.join(os.path.dirname(__file__), "..", "..", "..")
        self.buildfolder = os.path.join(os.path.dirname(__file__), "..", "..", "..", "build")
        

def helper_executeCommand(cmd, optionMessage = ""):
    optionalSpace = ""
    if not optionMessage =="":
        optionalSpace = " "

    print(f"{optionMessage}" + optionalSpace + f"Command -->{cmd}")
    exitPattern = subprocess.check_call(cmd)
    print(f"{optionMessage}" + optionalSpace + f"Exit Code -->{exitPattern}")

def get_args(arguments):
    desc = 'build tool chain wrapper'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--target','-t', required=False, type=str.lower, help='compiler target option')
    
    return parser.parse_args(arguments)


def fromelfOnExecutable(c):
    filepath = os.path.join(c.buildfolder, "a.out")
    # fromelf --text -c a.out
    # fromelf --text -z a.out
    cmd = "fromelf --text -c " + filepath + " >> Disassemble.map"
    helper_executeCommand(cmd)

    cmd = "fromelf --text -z " + filepath + " >> Examine_code.txt"
    helper_executeCommand(cmd)


def simpleBuilder(c, filename):
    # armclang --target=aarch64-arm-none-eabi hello.c
    filepath = os.path.join(os.path.dirname(__file__), "..", "..", "src", filename)
    cmd = "armclang --target=aarch64-arm-none-eabi " + filepath

    helper_executeCommand(cmd)
    fromelfOnExecutable(c)

def compileFiles(c, filename):
    filepath = os.path.join(os.path.dirname(__file__), "..", "..", "src", filename)
    cmd = "armclang -c --target=aarch64-arm-none-eabi " + filepath

    helper_executeCommand(cmd)
    
def linkFiles(c, filename):
    filepath = os.path.join(os.path.dirname(__file__), "..", "..", "src", filename)
    cmd = "armclang -c --target=aarch64-arm-none-eabi " + filepath

    helper_executeCommand(cmd)
    fromelfOnExecutable(c, "a.out")



def main():
    print("Hello, In Build tool chain")

    c = buildwrapper()
    #argument parser
    args = get_args(sys.argv[1:])
    print(args)

    cwd = os.getcwd()
    if not os.path.exists(c.buildfolder):
        os.mkdir(c.buildfolder)
    os.chdir(c.buildfolder)
    print(os.getcwd())
    simpleBuilder(c, "hello.c")
    # compileFiles(c)
   
    os.chdir(cwd)
    print(os.getcwd())

if __name__ == "__main__":
    sys.exit(main())