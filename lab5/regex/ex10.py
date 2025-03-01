import re

text_to_match = "letsTurnItIntoSnake"

pattern = r'([A-Z])'

result = re.sub(pattern, (lambda match: '_' + match.group(0).lower()), text_to_match)

print(result)