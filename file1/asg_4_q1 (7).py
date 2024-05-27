import re

print("""
Question 7- Write a regular expression in Python to split a string into uppercase letters.
Sample text: “ImportanceOfRegularExpressionsInPython”
Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]
---------------------------
""")


def my_regex(pat):
    return re.compile(pat)


my_patter = r'[A-Z][a-z]*'
regex_object = my_regex(my_patter)

default_input = 'ImportanceOfRegularExpressionsInPython'
while True:
    inputText = input("Input String:: ")
    if inputText.lower() == 'exit':
        break
    elif len(inputText) == 0:
        inputText = default_input
        print('using default input: ', inputText)
    result = regex_object.findall(inputText)
    if result:
        print(result)
        print("Match Found")
        print("Total count: ", len(result))
    else:
        print("No Match Found")
    print('Type "Exit" to exit...\n')

