import re
import requests
import bs4
from bs4 import BeautifulSoup

import time


def extract_job_title_from_div(div):
    job = ""
    for h2 in div.find_all('h2', attrs={"class":"jobTitle"}):
        for name in h2:
            if "new" not in name.get_text():
                job = name.get_text()
    return(job)

def extract_company_name_from_div(div):
    company = ""
    for title in div.find_all(attrs={"class":"companyName"}):
        company = title.get_text()
    return company

def extract_company_location_from_div(div):
    locations = ""
    for title in div.find_all(attrs={"class":"companyLocation"}):
        locations = title.get_text()
    return locations

#have to get vjk key
#then open new url with soup
#then find location of summary and snatch all text
#for this to work effecciently need to get different parts of url to do things
def get_summary(div):
    summary = []
    for thing in div.find_all('div', class_="job-snippet"):
        summary.append(thing.get_text())

    return summary

#issues with location of salary in html
#omitting as of right now for the demo
# def extract_company_salary_from_div(div):
#     salaries = ""
#     for title in div.find_all(attrs={"class":"salary-snippet"}):
#         print("got here")
#         salaries = title.get_text()
#     if salaries == "":
#         salaries = "NA"
#     return salaries


def create_company_info(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.text, "html.parser")

    company = []

    for thing in soup.find_all('div', class_="mosaic-zone"):
        for div in thing.find_all(name='a'):
            job = extract_job_title_from_div(div)
            company_name = extract_company_name_from_div(div)
            location = extract_company_location_from_div(div)
            # salary = extract_company_salary_from_div(div)
            if job != "" and company_name != "" and location != "":
                summary = get_summary(div)
                company.append({
                    "title": job,
                    "company": company_name,
                    "location": location,
                    "summary": summary
                })
    return company


if __name__ == "__main__":
    URL = "https://ca.indeed.com/jobs?q=software%20developer%20intern&l=Richmond%20Hill%2C%20ON&vjk=a4d8dda65bbd8b3d"

    company = create_company_info(URL)

    # get_summary(URL)


    for word in company:
        print(word, "\n")








