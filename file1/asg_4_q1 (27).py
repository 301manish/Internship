
import re

def extract_hashtags(text):
    # Define a regular expression pattern for hashtags
    pattern = r'#\w+'

    # Find all matches in the input text
    hashtag_list = re.findall(pattern, text)

    return hashtag_list

# Example sample text
sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

# Call the function
hashtags = extract_hashtags(sample_text)
print(hashtags)  # Expected output: ['#Doltiwal', '#xyzabc', '#Demonetization']
