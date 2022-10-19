import sys
import os
import logging


VERSION = '1.3.3'

#find script location
if getattr(sys, "frozen", False):
    # check application or script file
    # if app, pyinstaller extends sys module by a flag frozen=True and sets the app path into variable _MEIPASS
    current_dir = os.path.dirname(sys.executable)
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"current dir-->{current_dir}")
class p:
    def __init__(self):
        #paths related to root directory only
        self.test_string = "IN priveate class"
    
def configLogger(logfile='Logfile.log'):
    # create logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(logfile, mode="w")
    fh.setLevel(logging.INFO)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
def command_executor(cmd):
    cmd_output = subprocess.run(
        [
            "python",
            "hckr_rnk_ref.py",
            "--infile=test.txt",
            "--varb=praveen"
        ],
        capture_output=True,
        shell=True,
        text=True)
    output_string = cmd_output.stdout
    exit_code = cmd_output.stderr
    # output_string= output_string.decode("utf-8")

def get_args():
    desc = 'argument parser'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--infile',   required='--support' not in sys.argv and '--version' not in sys.argv,
                        help='input file path')
    parser.add_argument('--varb', default="prav", required=False,
                        help='var b')
    parser.add_argument('--version', action="store_true", required=False,
                        help='script version')
    return parser.parse_args()


def get_file_args(argum):
    '''
    you can also pass general arguments may be read from file? etc
    it hould be list of arguments as a list
    works as fine as system argument
    '''
    desc = 'update the hexfile'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-a', required=True, 
                        choices=["var1", "var2"],
                        help='choice param')
    parser.add_argument('-b', required=True,
                        help='bar b')
    return parser.parse_args(argum)

def file_operation(outfile, infile):    
    with open(outfile, 'w') as writefile:
        writefile.write("checkinng file operation")
    if os.path.isfile(outfile):
        log.info(f"file created")
    if os.path.isfile(infile):
        log.info(f"file available")
    with open(infile, 'w') as readfile:
#         fread = readfile.readlines()
        fread = readfile.read()

def checkfile(filename):
    if os.path.isfile(filename):
        logger.info('file available--> ' + filename)
    else:
        logger.error(
            'file does not exists. exit execution--> ' + filename)
        sys.exit(-1)

def main():
#     args = get_args(sys.argv[1:])
    args = get_args()
    
    if args.version:
        log.info(f"VERSION - {VERSION}")
        return 0

if __name__ == "__main__":
    sys.exit(main())
