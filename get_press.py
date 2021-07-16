import datetime
import os.path
from save_content import save_content

# Current progress file
curr_prog = "currprog.txt"

# Check if file exists, if not default to 2020-01-05
if not os.path.isfile(curr_prog):
    with open(curr_prog, 'w') as f:
        f.write("2020/1/5")

# Convert to datetime format
with open(curr_prog, 'r') as f:
    date = datetime.date(*map(int,f.read().split('/')))

# Start check up to today
while datetime.date.today() > c_date:
    
    date += datetime.timedelta(days=1)

    save_content(date)

    with open(curr_prog, 'w') as f:
        f.write(date.strftime('%Y/%m/%d'))
