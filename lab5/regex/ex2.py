import re

txt_file = '../row.txt'

with open(txt_file, 'r') as file:
    text_to_match = file.read()
    

pattern = r'ab{2,3}'

result = re.findall(pattern, text_to_match, re.IGNORECASE)

if(result):
    print(result)

else:
    print("None")