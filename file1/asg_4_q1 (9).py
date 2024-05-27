import re

print("""
Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython
---------------------------
""")


def my_regex(pat):
    return re.compile(pat)


my_patter =r'(\d)([A-Z])'
regex_object = my_regex(my_patter)

default_input = 'RegularExpression1IsAn2ImportantTopic3InPython'
while True:
    inputText = input("Input String:: ")
    if inputText.lower() == 'exit':
        break
    elif len(inputText) == 0:
        inputText = default_input
        print('using default input: ', inputText)
    result = regex_object.sub(r' \1 \2',inputText)
    if result:
        print(result)
        print("Match Found")
    else:
        print("No Match Found")
    print('Type "Exit" to exit...\n')

