import re

print("Question 10- Write a RegEx pattern in python program to find all words that are 4 digits long in a string."
      "Sample text- '01 0132 231875 1458 301 2725.'"
      "Expected output- ['0132', '1458', '2725']?\n")


def my_regex(pat):
    return re.compile(pat)


my_patter = r'\d{4}\b'
regex_object = my_regex(my_patter)

while True:
    inputText = input("Input String:: ")
    if inputText.lower() == 'exit':
        break
    result = regex_object.findall(inputText)
    if result:
        print(result)
        print("Match Found")
        print("Total count: ", len(result))
    else:
        print("No Match Found")
    print('Type "Exit" to exit...\n')
