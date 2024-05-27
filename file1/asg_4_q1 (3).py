import re

print("""
Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory?\n
""")


def my_regex(pat):
    return re.compile(pat)


my_patter = r'\b\w{4}\b'
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




