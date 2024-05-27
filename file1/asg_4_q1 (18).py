import re

text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

for match in re.finditer(pattern, text):
    start_pos = match.start()
    end_pos = match.end()
    print(f'Found "{text[start_pos:end_pos]}" at {start_pos}:{end_pos}')
