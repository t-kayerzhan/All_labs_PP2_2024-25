import re

text_to_match = "why_do_i_procrastinate; i_want_to_sleep"

pattern = r'_([a-z])'

result = re.sub(pattern, lambda match1: match1.group(1).upper(), text_to_match)

print(result)