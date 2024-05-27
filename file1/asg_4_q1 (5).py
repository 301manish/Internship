import re

print("""
Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# Expected Output:
# example.com
# hr@fliprobo.com
# github.com
# Hello Data Science World
# Data Scientis
---------------------------
""")


def my_regex(pat):
    return re.compile(pat)


my_patter = r' \((?=.com)|\)|\('
regex_object = my_regex(my_patter)

s_list = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

for i in s_list:
    result = regex_object.sub( '', i )
    if result:
        print(result)
    else:
        print("No Match Found")




