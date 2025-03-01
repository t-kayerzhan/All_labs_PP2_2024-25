import re

txt_file = '../row.txt'

with open(txt_file, 'r') as file:
    text_to_match = file.read()

pattern = r"[ ,.]"

result = re.sub(pattern, ':', text_to_match)

print(result)