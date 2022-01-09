import requests
import bs4
from bs4 import BeautifulSoup

import time

# def extract_job_title_from_result(soup):
#     jobs = []
#     spans = soup.findAll("span", attrs={"class":"jobTitle"})
#     print("got here")
#     print(spans)
#     for span in spans:
#         jobs.append(span.text)
#     return(jobs)

def extract_job_title_from_result(soup):
    jobs = []
    for div in soup.find_all(name="a"):
        for h2 in div.find_all(name="h2", attrs={"class":"jobTitle"}):
            for title in h2.find_all(name="span"):
                if title.get_text() != "new":
                    jobs.append(title.get_text())
    return(jobs)




if __name__ == "__main__":
    URL = "https://ca.indeed.com/jobs?q=software%20developer&l=Richmond%20Hill%2C%20ON&vjk=70fbf10fa42d3311"
    #conducting a request of the stated URL above:
    page = requests.get(URL)
    #specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
    soup = BeautifulSoup(page.text, "html.parser")
    #printing soup in a more structured tree format that makes for easier reading
    jobs = extract_job_title_from_result(soup)
    for word in jobs:
        print(word, "\n")
    #print(soup.getText())
    #print(soup.prettify())








