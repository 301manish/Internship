import re

def check_string(string):
    # Define a regular expression pattern for ending with an alphanumeric character
    pattern = r'[a-zA-Z0-9]$'

    if re.search(pattern, string):
        print("Accept")
    else:
        print("Discard")

# Example strings
string1 = "ankirai@"
string2 = "ankitrai326"
string3 = "ankit."
string4 = "geeksforgeeks"

# Check each string
check_string(string1)  # Output: Discard
check_string(string2)  # Output: Accept
check_string(string3)  # Output: Discard
check_string(string4)  # Output: Accept
