import os

file = open("example.txt", 'r')
content_to_copy = file.read()

with open("example_copy.txt", 'w') as file:
    file.write(content_to_copy)