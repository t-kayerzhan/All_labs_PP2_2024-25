import re
txt_file = '../row.txt'

with open(txt_file, 'r') as file:
    text_to_match = file.read()

pattern = '[A-Z][a-z]+'

result = re.findall(pattern, text_to_match)

if(result):
    print(result)
else:
    print("None")