import re

print("Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon. Sample "
      "Text- 'Python Exercises, PHP exercises.' Expected Output: Python:Exercises::PHP:exercises:?\n")


def my_regex(pat):
    return re.compile(pat)


my_patter = r'[ ,.]'
regex_object = my_regex(my_patter)

while True:
    inputText = input("Input String:: ")
    if inputText.lower() == 'exit':
        break
    result = regex_object.subn(string=inputText,repl=':')
    if result:
        print(result)
        print("Match Found")
        print("Total count: ", len(result))
    else:
        print("No Match Found")
    print('Type "Exit" to exit...\n')




