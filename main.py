from indeed_scraper import create_company_info
from testing import create_cv_from_list

if __name__ == '__main__':

    URL = ""
    if input(str("would you like to select a URL: ")) == "yes":
        title = input("what position would you like to apply for")
        location = input("which location would you like the job to be in")
        title = title.strip()
        title = title.replace(" ", "%20")
        location = location.strip()
        location = location.replace(" ", "%20")
        URL = "https://ca.indeed.com/jobs?q=" + title + "&l=" + location
    else:
        URL = "https://ca.indeed.com/jobs?q=software%20developer%20intern&l=Richmond%20Hill%2C%20ON&vjk=a4d8dda65bbd8b3d"
    print("if you would like to modify the list of skills and there keywords please manually access the file")
    print(URL)
    companies = create_company_info(URL)
    print(companies)
    create_cv_from_list(companies)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
