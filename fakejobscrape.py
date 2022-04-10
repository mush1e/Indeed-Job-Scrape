import requests
from bs4 import BeautifulSoup

class fakejobscrape:
    def __init__(self):
        self.URL="https://realpython.github.io/fake-jobs/"
        page = requests.get(self.URL)
        soup = (BeautifulSoup(page.content, "html.parser"))
        titles = soup.find_all(class_="media-content")
        for title in titles:
            print(title.text)
    
if __name__ == '__main__':
    ob = fakejobscrape()