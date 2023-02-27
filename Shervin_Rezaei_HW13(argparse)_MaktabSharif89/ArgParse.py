import os
import argparse


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-f', '--file')
group.add_argument('-d', '--directory')
parser.add_argument('-F', '--file-extension')
args = parser.parse_args()

if args.file:
    byte = os.path.getsize(args.file)
    byte =  byte / 1000
    print(f'Directory "/{args.file}" size is {byte} KB')

if args.directory:
    byte = 0
    for path, dirs, files in os.walk(args.directory):
        for file in files:
            if args.file_extension and not file.endswith(args.file_extension):
                continue
            file_path = os.path.join(path, file)
            byte += os.path.getsize(file_path)
    byte = byte / 1000
    print(f'Directory "/{args.directory}" size is {byte} KB')
