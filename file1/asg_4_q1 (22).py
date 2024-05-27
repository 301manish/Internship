import re

def extract_maximum(str1):
    num = 0
    res = 0
    for char in str1:
        if char.isdigit():
            num = num * 10 + int(char)
        else:
            res = max(res, num)
            num = 0
    return max(res, num)

# Example input string
input_string = 'My marks in each semester are: 947, 896, 926, 524, 1000,  734, 950, 642'
result = extract_maximum(input_string)
print(f"Maximum numeric value: {result}")
