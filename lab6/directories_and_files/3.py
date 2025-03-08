import os

def check_path(path):

    print(f"Path '{path}' exists.\n")

    directory = os.path.dirname(path)
    filename = os.path.basename(path)

    if directory:
        print(f"Directory: {directory}")
    else:
        print("Directory: N/A")

    if filename:
        print(f"Filename: {filename}")
    else:
        print("Filename: N/A")

path = r"/Users/tanzilya/Documents"  
check_path(path)
