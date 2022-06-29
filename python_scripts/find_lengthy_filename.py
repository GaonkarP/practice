#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import pandas as pd
# import numpy as np

NUMBEROFFILES = 0

def get_args(arguments):
    desc = 'Finds and lists the files with lengthy name'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--length','-l', required=False, default="256", type=int, help='file name lenth more than given value is listed')
    parser.add_argument('--inputfolder','-i', required=True, help='input folder to search')
    return parser.parse_args(arguments)


# ---------------------------------------
# Description:
# finding flist file in the given path
# Input parameters: name, file path
# Return: return the files
# ---------------------------------------
def find_all_files(length, path):
    global NUMBEROFFILES    
    lines = []
    num_of_lengthy_files = 0
    lines.append("Filename,Component,Relative_path,length,Absolute_path,Length\n")
    for root, dirs, files in os.walk(path):
        for name in files:
            NUMBEROFFILES += 1
            filename_w_abs_path = os.path.join(root, name)
            filename_w_relative_path = filename_w_abs_path.strip(path)
            if (len(filename_w_relative_path) > length) and not (filename_w_relative_path.startswith(".git")):
            # result.append(os.path.join(root, name))
                num_of_lengthy_files += 1
                print(filename_w_relative_path)
                lines.append(name + "," + filename_w_relative_path.split("\\")[1] + "," + filename_w_relative_path)
                lines.append("," + str(len(filename_w_relative_path)) + "," + filename_w_abs_path + "," + str(len(filename_w_abs_path)) + "\n")
    with open("data_file.csv", "w") as write_data:
        for line in lines:
            write_data.write(str(line))
    print(f"Total number of files with lenthy file name -->{num_of_lengthy_files}")

def create_dataxl():
    data_file = pd.read_csv("data_file.csv")
    # print(data_file[0:3])
    data_file.to_excel("data_file.xlsx")
    data_file.to_html("data_file.html")
    
def main():
    global NUMBEROFFILES
    args = get_args(sys.argv[1:])
    cwd = os.getcwd()
    print(f"Tool to find and create list of files with lengthy name")
    find_all_files(args.length, args.inputfolder)
    print(f"Total number of files in given folder -->{NUMBEROFFILES}")
    create_dataxl()


if __name__ == "__main__":
    sys.exit(main())