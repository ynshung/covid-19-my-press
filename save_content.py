from pathlib import Path
from extract_html import extract_html

def save_content(date):
    html_dict = extract_html(date)

    if html_dict is None:
        return

    for title, ct in html_dict.items():
        # Define file path and name to be stored
        if "situasi" in title:
            fpath = f"current-situation/{date.strftime('%Y/%m')}/"
        else:
            fpath = f"special/{date.strftime('%Y')}/"
        if len(title) > 248:
            title = title[:248]

        fname = f"{title}.html"

        # Make directory if not exist
        Path(fpath).mkdir(parents=True, exist_ok=True)

        # Write html
        with open(fpath+fname,'w',encoding="utf-8") as f:
            f.write(ct)
            # print(title)
