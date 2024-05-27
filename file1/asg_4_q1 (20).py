import re

def find_decimal_numbers(text):
    # Define a regular expression pattern for decimal numbers
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')

    # Find all matches in the input text
    matches = pattern.findall(text)

    return matches

# Sample text
sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"

# Get the decimal numbers with precision 1 or 2
result = find_decimal_numbers(sample_text)
print(result)  # Expected output: ['01.12', '145.8', '3.01', '27.25', '0.25']
