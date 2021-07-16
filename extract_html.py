from bs4 import BeautifulSoup
import requests

def extract_html(date):
    date_str = date.strftime('%Y/%m/%d')

    # Browse date for the website
    kpk = requests.get("https://kpkesihatan.com/"+date_str)

    # If error such as 404, goto next date
    if kpk.status_code >= 400:
        return

    # Start parsing html with bs4, take link with covid-19 ref
    cv_link = ''
    soup = BeautifulSoup(kpk.text, 'html.parser')
    articles = soup.find("div", {"id": "main-content"})

    # Get all a reference, remove duplicate and discard author
    links = set([i.get('href') for i in articles.find_all('a')])
    links.discard('https://kpkesihatan.com/author/pejabatkpk/')

    # Search terms
    search = ["covid-19","2019-ncov","coronavirus","pneumonia"]
    htmls = {}

    # Loop through links
    for link in links:
        if any(map(link.__contains__, search)):

            # Get title from URL
            title = link.split('/')[-2]

            # Navigate to the link and parse again
            kpk = requests.get(link)
            soup = BeautifulSoup(kpk.text, 'html.parser')

            # Find the content and remove unrelated div (share)
            content = soup.find("div", {"class": "main-content"})
            soup.find('div', id="jp-post-flair").decompose()

            # Append title as key and content as value in dict
            htmls[title] = str(content)

    return htmls
    
