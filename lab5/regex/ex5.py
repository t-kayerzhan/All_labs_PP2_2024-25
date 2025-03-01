import re

txt_file = '../row.txt'

with open(txt_file, 'r') as file:
    text_to_match = file.read()

pattern = 'a.+b$'

result = re.findall(pattern, text_to_match, re.IGNORECASE)

if(result):
    print(result)
else:
    print("None")