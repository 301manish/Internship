import re

def remove_words_between_2_and_4(text):
    # Define a regular expression pattern for words of length 2 to 4
    pattern = re.compile(r'\b\w{2,4}\b')

    # Replace all occurrences of the pattern with an empty string
    result = pattern.sub('', text)

    return result

# Example input text
sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

# Call the function
output = remove_words_between_2_and_4(sample_text)
print(output)
