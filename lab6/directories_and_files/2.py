import os

def check_access(path):
    
    print(f"Checking access for: {path}\n")

    if os.path.exists(path):
        print("Exists:         Yes")
    else:
        print("Exists:         No")

    if os.access(path, os.R_OK):
        print("Readable:       Yes")
    else:
        print("Readable:       No")

    if os.access(path, os.W_OK):
        print("Writable:       Yes")
    else:
        print("Writable:       No")

    if os.access(path, os.X_OK):
        print("Executable:     Yes")
    else:
        print("Executable:     No")

path = r"/Users/tanzilya/Documents" 
check_access(path)
