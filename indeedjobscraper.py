import os, requests
from bs4 import BeautifulSoup

class jobFinder:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.URL = 'https://ca.indeed.com/jobs?'
        print('*'*50)
        print(f"{'Welcome To The CLI Job Finder :D':^50}")
        print('~'*50)
        self.jobs = []
        self.companies = []
        self.ratings = []
        self.locations = []
        self.descriptions = []
    
    def driver(self):
        self.query = input("What kind of job are you looking for?")
        self.location = input("What location are you looking to work in? ^-^")
        page = requests.get(f"{self.URL+'q='+self.query+'&l='+self.location}")
        soup = BeautifulSoup(page.content, "html.parser")
        jobs = soup.find_all("h2", class_="jobTitle jobTitle-color-purple")
        companies = soup.find_all("span", class_="companyName")

        for job in jobs:
            temp = job.findChild("span", recursive=False)
            print(temp)
            self.jobs.append(temp.text)
            print(temp.text)

        for company in companies:
            temp = company.findChild("a", recursive=False)
            try:
                print(temp.text)
            except:
                print(company.text)




if __name__ == '__main__':
    ob = jobFinder()
    ob.driver()

