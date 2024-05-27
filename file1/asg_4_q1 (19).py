import re

def change_date_format(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', r'\3-\2-\1', dt)

date1 = "2026-01-02"
new_date = change_date_format(date1)

print(f"Original date in yyyy-mm-dd format: {date1}")
print(f"New date in dd-mm-yyyy format: {new_date}")
