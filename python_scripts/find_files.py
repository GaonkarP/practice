import os
import sys
import subprocess
import shutil
import argparse


NUMBEROFFILES = 0

def get_args(arguments):
    desc = 'Find and Copy source files'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--extension','-e', required=True, help='file extension to be searched and copied, could be list seperated by ","')
    parser.add_argument('--inputfolder','-i', required=True, help='Flist location')
    parser.add_argument('--outputfolder','-o', required=True, help='Out put folder location')
    parser.add_argument('--blacklist','-b', required=False, help='Out put folder location')
    return parser.parse_args(arguments)


class p:
    def __init__(self, repository_rootdir, destinationfolder):

        #paths only relative to repository_rootdir (root directory of repo)
        self.repository_rootdir = repository_rootdir
        self.source_code_for_OSS = os.path.join(destinationfolder, "Source_files")
        self.OSS_flux_error_logfile = os.path.join(destinationfolder, "OSS_flux_error.txt")
        self.destinationfolder = destinationfolder
        self.my_api_key_arg = None

# ---------------------------------------------
#  Description:
# copying the files to the destination location
# Input parameter: config, relfilename
# Return: Nothing
# ----------------------------------------------
def copyfiles(source, destination):
    global NUMBEROFFILES
    NUMBEROFFILES = NUMBEROFFILES + 1
    # relfilename = relfilename.strip('\n')
    # source = os.path.join(c.repository_rootdir, relfilename)
    # destination = os.path.join(c.source_code_for_OSS, relfilename)
    # shutil.copyfile(source, destination)
    try:
        shutil.copyfile(source, destination)
    except IOError as io_err:
        try:
            os.makedirs(os.path.dirname(destination), exist_ok=True)
        except Exception as exc:
            print(f"Exception is {exc}")

        try:
            shutil.copyfile(source, destination)
        except FileNotFoundError as file_err:
            print(f"Mentioned file is not found please take care--> {file_err}")
            # with open(c.OSS_flux_error_logfile, "r") as f_err:
            #     temp_lines = f_err.readlines()
            # temp_lines.append(relfilename)
            # temp_lines.append("\n")
            # with open(c.OSS_flux_error_logfile, "w") as f_err:
            #     f_err.writelines(temp_lines)


# ---------------------------------------
# Description:
# finding flist file in the given path
# Input parameters: name, file path
# Return: return the files
# ---------------------------------------
def find_all_files(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result


# ---------------------------------------
# Description:
# finding files wiht given extension in the given path
# Input parameters: extension list, file path
# Return: return the files
# ---------------------------------------
def find_all_files_w_extension(extension, source, destination, blacklist=None):
    print(f"blacklist folders--> {blacklist}")
    # sys.exit()
    for root, dirs, files in os.walk(source):
        # if ((blacklist is None) or (root.endswith(blacklist) is False)):
        #     if (root.endswith(blacklist)):
        #         print(root)
        #         print(root.endswith(blacklist) is False)
        #         sys.exit()
        for file in files:
            if file.endswith(tuple(extension)):
                dest_rel_path = root.replace(source, destination)
                copyfiles( (os.path.join(root, file)), (os.path.join(dest_rel_path, file)) )

def main():
    global NUMBEROFFILES
    args = get_args(sys.argv[1:])
    cwd = os.getcwd()
    print(f"Tool to find and copy files with given extensioin from a folder")
    file_extension = args.extension.split(",")
    if args.blacklist is not None:
        blacklist = tuple(args.blacklist.split(","))
    else:
        blacklist = args.blacklist

    find_all_files_w_extension(file_extension, args.inputfolder, args.outputfolder, blacklist)

    print(f"Total number of files with extension {file_extension} are --> {NUMBEROFFILES}")

if __name__ == "__main__":
    sys.exit(main())