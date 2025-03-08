import os 


path = "/Users/tanzilya/Documents/new_folder/labs/lab6/directories_and_files/alphabet"



for letter in range(65, 91):
    with open((path+'\\'+chr(letter)+'.txt'), 'w') as file:
        pass