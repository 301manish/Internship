import re

print("""
Question 8- Create a function in python to insert spaces between words starting with numbers.
Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython
---------------------------
""")


def my_regex(pat):
    return re.compile(pat)


my_patter =r'(\d)([A-Za-z])'
regex_object = my_regex(my_patter)

default_input = 'RegularExpression1IsAn2ImportantTopic3InPython'
while True:
    inputText = input("Input String:: ")
    if inputText.lower() == 'exit':
        break
    elif len(inputText) == 0:
        inputText = default_input
        print('using default input: ', inputText)
    result = regex_object.sub(r' \1\2',inputText)
    if result:
        print(result)
        print("Match Found")
    else:
        print("No Match Found")
    print('Type "Exit" to exit...\n')

