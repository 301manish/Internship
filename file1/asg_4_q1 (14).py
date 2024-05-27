import re

# Sample text
sample_text = "On August 15th 1947 that India was declared independent from British colonialism. On June 12th 1950  and the reins of control were handed over to the leaders of the Country."

with open('asg_4_q1 (14)', 'w+') as file:
    file.write(sample_text)
# Regular expression pattern to match the date format (Month name followed by day number and year)
date_pattern = r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2}(?:st|nd|rd|th)?\s\d{4}\b"

# Find all matches in the sample text
matches = re.findall(date_pattern, sample_text)

# Print the extracted date strings
# Print the extracted date strings
with open('asg_4_q1 (14)_edited.txt', 'a+') as file:
    file.write('\n')
    for match in matches:
        file.write(match)
        print(match)

