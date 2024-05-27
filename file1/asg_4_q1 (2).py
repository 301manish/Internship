import pandas as pd
import re

print("""
Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.
Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
Expected output-
0      hello world
1             test
2    four five six
""")

data = {
    'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']
    }
df = pd.DataFrame(data)
df=df['SUMMARY'].apply(lambda x: re.sub(r'[,!,X:;.\d]+','',x))
print(df)
