import requests
import bs4
from bs4 import BeautifulSoup

import time


def extract_job_title_from_div(div):
    job = ""
    for h2 in div.find_all(name="h2", attrs={"class":"jobTitle"}):
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
    for thing in soup.find_all(attrs={"class":"mosaic-zone"}):
        for div in thing.find_all(name='a'):
            job = extract_job_title_from_div(div)
            company_name = extract_company_name_from_div(div)
            location = extract_company_location_from_div(div)
            # salary = extract_company_salary_from_div(div)
            if job != "" and company_name != "" and location != "":
                company.append((company_name, job, location))
    return company






if __name__ == "__main__":
    URL = "https://ca.indeed.com/jobs?q=software%20developer&l=Richmond%20Hill%2C%20ON&vjk=9c06e74ec245e94a"

    company = create_company_info(URL)

    for word in company:
        print(word, "\n")








