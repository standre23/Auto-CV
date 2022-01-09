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
            jobs.append(h2.get_text())
    return(jobs)

def extract_company_name_from_result(soup):
    companies = []
    for div in soup.find_all(name="a"):
        for title in div.find_all(attrs={"class":"companyName"}):
            companies.append(title.get_text())
    return companies

def extract_company_location_from_result(soup):
    locations = []
    for div in soup.find_all(name="a"):
        for title in div.find_all(attrs={"class":"companyLocation"}):
            locations.append(title.get_text())
    return locations

def extract_company_salary_from_result(soup):
    salaries = []
    for div in soup.find_all(name="a"):
        for title in div.find_all(attrs={"class": "salarySnippet"}):
            salaries.append(title.get_text())
    return salaries




if __name__ == "__main__":
    URL = "https://ca.indeed.com/jobs?q=software%20developer&l=Richmond%20Hill%2C%20ON&vjk=19e1a9fac332fc27"
    #conducting a request of the stated URL above:
    page = requests.get(URL)
    #specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
    soup = BeautifulSoup(page.text, "html.parser")
    #printing soup in a more structured tree format that makes for easier reading
    jobs = extract_job_title_from_result(soup)
    comp = extract_company_name_from_result(soup)
    loc = extract_company_location_from_result(soup)
    salary = extract_company_salary_from_result(soup)
    for index in range(len(jobs)):
        print(jobs[index])
        print(comp[index])
        print(loc[index], "\n")

    print(len(jobs))
    #print(soup.getText())
    #print(soup.prettify())








