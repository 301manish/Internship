import re

print("""
Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
Note- Store given sample text in the text file and then to remove the parenthesis area from the text.
---------------------------
""")


def my_regex(pat):
    return re.compile(pat)


my_patter = r' \((?=.com)|\)|\('
regex_object = my_regex(my_patter)
sample_text = open(file='q6.txt', mode='r', closefd=True).read()
print("Data from file::", sample_text)
edited_text = regex_object.sub('',sample_text)
print('Edited data::', edited_text)
with open(file='q6_edited.txt', mode='w+', closefd=True) as ff:
    ff.write(edited_text)
