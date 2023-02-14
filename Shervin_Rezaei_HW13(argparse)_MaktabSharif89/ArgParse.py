import argparse
import os

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-f', '--file')
group.add_argument('-d', '--directory')
parser.add_argument('-F', '--file-extension')
args = parser.parse_args()

def file_size(file_path):
    byte = os.path.getsize(file_path)
    return byte / 1024

def dir_size(dir_path, extension=None):
    byte = 0
    for path, dirs, files in os.walk(dir_path):
        for thing in files:
            if extension and not thing.endswith(extension):
                continue
            file_path = os.path.join(path, thing)
            byte += os.path.getsize(file_path)
    return byte / 1024

if args.file:
    file_size = file_size(args.file)
    print(f'/{args.file}  is {file_size} KB')

if args.directory:
    dir_size = dir_size(args.directory, args.file_extension)
    print(f'Directory "/{args.directory}" size is {dir_size} KB')
