import requests

class fakejobscrape:
    def __init__(self):
        self.URL="https://realpython.github.io/fake-jobs/"
        page = requests.get(self.URL)
        print(page.text)
    
if __name__ == '__main__':
    ob = fakejobscrape()