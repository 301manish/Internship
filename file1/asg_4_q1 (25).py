import re

def remove_duplicates(sentence):
    # Define a regular expression pattern for continuous duplicate words
    pattern = r'\b(\w+)(?: \1\b)+'

    # Replace continuous duplicates with a single occurrence
    result = re.sub(pattern, r'\1', sentence)

    return result

# Example input text
sample_text = "Hello hello world world"
output = remove_duplicates(sample_text)
print(output)  # Expected output: "Hello hello world"
