def search_literals(sample_text, searched_words):
    """
    Searches for literal strings in the sample text.

    Args:
        sample_text (str): The input text to search within.
        searched_words (list): List of words to search for.

    Returns:
        list: A list of found words.
    """
    found_words = []
    for word in searched_words:
        if word in sample_text:
            found_words.append(word)
    return found_words

# Sample text
sample_text = 'The quick brown fox jumps over the lazy dog.'

# Words to search for
searched_words = ['fox', 'dog', 'horse']

# Search for the words
found_words = search_literals(sample_text, searched_words)

# Print the results
if found_words:
    print(f"Found words: {', '.join(found_words)}")
else:
    print("No matching words found.")
