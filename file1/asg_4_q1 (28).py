import re

def remove_unicode_symbols(text):
    # Define a regular expression pattern for <U+..> symbols
    pattern = r'<U\+[0-9A-Fa-f]+>'

    # Replace all occurrences of the pattern with an empty string
    result = re.sub(pattern, '', text)

    return result

# Example sample text
sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"

# Call the function
output = remove_unicode_symbols(sample_text)
print(output)
