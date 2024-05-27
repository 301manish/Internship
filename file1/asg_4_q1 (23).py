import re

def insert_spaces(text):
    # Use regular expression to find words starting with capital letters
    pattern = r'([A-Z][a-z]+)'

    # Replace each match with the same word followed by a space
    result = re.sub(pattern, r'\1 ', text)

    # Remove any trailing space
    result = result.strip()

    return result

# Example input string
sample_text = "RegularExpressionIsAnImportantTopicInPython"

# Call the function
output = insert_spaces(sample_text)
print(output)  # Expected output: "Regular Expression Is An Important Topic In Python"
