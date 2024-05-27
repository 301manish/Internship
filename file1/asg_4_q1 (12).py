import re

print("""

Question 12- Write a Python program where a string will start with a specific number. 
---------------------------
""")


def my_regex(pat):
    return re.compile(pat)


while True:
    inputText = input("Input String:: ")
    if inputText.lower() == 'exit':
        break
    search_character = input("Enter a digit to search in string starts with:: ")
    my_patter = r'^[' + search_character + r']\w+'
    regex_object = my_regex(my_patter)
    result = regex_object.findall(inputText)
    if result:
        print(result)
        print("Match Found")
    else:
        print("No Match Found")
    print('Type "Exit" to exit...\n')

