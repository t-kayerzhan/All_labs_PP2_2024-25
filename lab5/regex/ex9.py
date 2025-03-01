import re 

text_to_match = "WowItsAlreadyNight"

pattern = r'(?<=[a-z])([A-Z])'

result = re.sub(pattern, r' \1', text_to_match)

print(result)