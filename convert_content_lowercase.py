import os
import sys
import argparse

def get_args(arguments):
    desc = 'converts contet of file to lower case other than comments'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--ifile','-if', required=False, type=int, help='file to be converted to lowercase')
    return parser.parse_args(arguments)

def readfile(in_file):
    lines = []
    with open(in_file, "r") as f1:
        lines = f1.readlines()
        # print(lines)
        # sys.exit()
    print(len(lines))
    for i in range(len(lines)):
        if not lines[i].strip().startswith("#") or lines[i].strip().startswith("name"):
            lines[i] = str.lower(lines[i])
            # for j in range(len(lines[i])):
            #     if lines[i][j] == "@" and lines[i][j-1] == " ":

            # pass
        print(lines[i])
    
    with open(in_file, "w") as f1:
        f1.writelines(lines)

            
        # print(len(lines))   



def main():

    cwd = os.getcwd()
    print(cwd)

    args = get_args(sys.argv[1:])
    if args.ifile is None or args.ifile == "":
        in_file = os.path.join(cwd, "CODEOWNERS")
    readfile(in_file)

    print("done")



if __name__ == "__main__":
    sys.exit(main())