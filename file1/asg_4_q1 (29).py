import re

def extract_dates_from_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            # Define a regex pattern for dates (dd-mm-yyyy or dd/mm/yyyy)
            pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
            dates = re.findall(pattern, text)
            return dates
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

# Example usage
sample_text_filename = "asg_4_q1 (29)"
dates_list = extract_dates_from_file(sample_text_filename)

if dates_list:
    print("Extracted dates:")
    for date in dates_list:
        print(date)
else:
    print("No dates found in the file.")
