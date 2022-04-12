import os, requests
from bs4 import BeautifulSoup

class jobFinder:
    def __init__(self):
        self.start = 0
        self.jobs = [[],[]]

        os.system('cls' if os.name == 'nt' else 'clear')
        self.URL = 'https://ca.indeed.com/jobs?'
        print('*'*50)
        print(f"{'Welcome To The CLI Job Finder :D':^50}")
        print('~'*50)

    def driver(self):
        self.query = input("What kind of job are you looking for?  ->  ")
        self.location = input("What location are you looking to work in? ^-^  ->  ")
        page = requests.get(f"{self.URL+'q='+self.query+'&l='+self.location}")
        soup = BeautifulSoup(page.content, "html.parser")
        jobs = soup.find_all("div", class_="job_seen_beacon")
        for job in jobs:
            temp = job.find("h2", recursive=True).find("span", recursive=False)
            self.jobs[0].append(temp.text)
            temp = job.find("span", class_="companyName", recursive=True)
            if temp.find("a", recursive=False) == None:
                self.jobs[1].append(temp.text)
                continue
            temp = temp.find("a", recursive=False)
            self.jobs[1].append(temp.text)
        print(self.jobs)

if __name__ == '__main__':
    ob = jobFinder()
    ob.driver()

