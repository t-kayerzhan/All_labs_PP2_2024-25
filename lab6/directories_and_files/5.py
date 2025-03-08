import os

mylist = ["apple", "banana", "tl"]

file_name = 'test.txt'

with open(file_name, 'w') as file:
    for element in mylist:
        file.write(element + "\n")