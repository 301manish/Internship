def find_substrings(sample_text, pattern):
    """
    Splits the sample text into substrings based on the specified pattern.

    Args:
        sample_text (str): The input text.
        pattern (str): The pattern to split on.

    Returns:
        list: A list of substrings.
    """
    substrings = sample_text.split(pattern)
    return substrings

# Sample text
sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

# Find substrings
substrings = find_substrings(sample_text, pattern)

# Print the result
print("Substrings:")
for substring in substrings:
    print(substring.strip())  # Remove leading/trailing spaces
