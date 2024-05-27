import re

pattern = r'[A-Z][a-z]+'
text = "This is a Sample Text with Multiple Matches"
matches = re.findall(pattern, text)
print(matches)
