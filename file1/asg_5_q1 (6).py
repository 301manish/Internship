import re 

print("Question 6- Write a RegEx pattern in python program that matches a string that has an 'a' followed by two to three 'b'?\n")


def my_regex(pat):
    return re.compile(pat)


my_patter = r'ab{2,3}'
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
    


