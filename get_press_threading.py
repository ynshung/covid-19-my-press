import datetime
import concurrent.futures
from tqdm import tqdm
from save_content import save_content

# First post is on 2020/1/6
c_date = datetime.date(2020,1,6)

# Create array with all dates in-between
dates = []

while datetime.date.today() > c_date:
    dates.append(c_date)
    c_date += datetime.timedelta(days=1)

# Threading, tqdm for progress bar (optional)
with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
    list(tqdm(executor.map(save_content, dates), total=len(dates)))
