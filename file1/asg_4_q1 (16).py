def search_and_locate(sample_text, searched_word):
    """
    Searches for a literal word in the sample text and returns its location.

    Args:
        sample_text (str): The input text to search within.
        searched_word (str): The word to search for.

    Returns:
        list: A list of tuples containing (start_index, end_index) for each occurrence.
    """
    occurrences = []
    start_index = sample_text.find(searched_word)
    while start_index != -1:
        end_index = start_index + len(searched_word)
        occurrences.append((start_index, end_index))
        start_index = sample_text.find(searched_word, end_index)
    return occurrences

# Sample text
sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_word = 'fox'

# Search for the word and get its location
occurrences = search_and_locate(sample_text, searched_word)

# Print the results
if occurrences:
    print(f"'{searched_word}' found at:")
    for start, end in occurrences:
        print(f"Start index: {start}, End index: {end}")
else:
    print(f"'{searched_word}' not found in the sample text.")
