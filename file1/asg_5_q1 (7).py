import re 

print("Question 7- Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'?\n")


def my_regex(pat):
    return re.compile(pat)


my_patter = r'a.b$'
regex_object = my_regex(my_patter)

while True:
    inputText = input("Input String:: ")
    if inputText.lower() == 'exit':
        break
    result = regex_object.findall(inputText)
    if result:
        print(result)
        print("Match Found")
    else:
        print("No Match Found")
    print('Type "Exit" to exit...\n')
