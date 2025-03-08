import os
import string

# Проверьте правильное название папки!
path = "/Users/tanzilya/Documents/new_folder/labs/lab6/directories_and_files/alphabet"

# ✅ Гарантируем, что папка alphabet существует
if not os.path.exists(path):
    os.makedirs(path) 
for letter in range(65, 91):
    with open((path+'\\'+chr(letter)+'.txt'), 'w') as file:
        pass