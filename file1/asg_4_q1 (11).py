import re

print("""
Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
---------------------------
""")


def my_regex(pat):
    return re.compile(pat)


my_patter =r'^\w+$'
regex_object = my_regex(my_patter)

default_input = 'RegularExpression1IsAn2ImportantTopic3InPython'
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
    else:
        print("No Match Found")
    print('Type "Exit" to exit...\n')

