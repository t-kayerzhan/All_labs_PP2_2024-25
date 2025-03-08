import os 

path = "/Users/tanzilya/Documents/new_folder/labs/lab6/directories_and_files/todelete.txt"


if os.access(path, os.F_OK):
    os.remove(path)