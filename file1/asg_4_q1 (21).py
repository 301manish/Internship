import re

def find_numbers_with_positions(text):
    # Define a regular expression pattern for finding numbers
    pattern = re.compile(r'\d+')

    # Find all matches in the input text
    for match in re.finditer(pattern, text):
        number = match.group(0)
        start_pos = match.start()
        end_pos = match.end()
        print(f"Number: {number}, Position: {start_pos}-{end_pos}")

# Example input string
input_string = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the70 ArrayList is trimmed accordingly."

# Call the function with the input string
find_numbers_with_positions(input_string)
