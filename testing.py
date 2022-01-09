import re
from indeed_scraper import create_company_info



def parse_skills_file():
    skillsFile = open("skills.txt", 'r')
    skills = []
    for line in skillsFile:
        line = line.replace("\n", "")
        skills.append(line.split("-"))

    skillsFile.close()
    return skills

def choose_skills(job_summary, skills):
    skill_value = []
    max=0
    for skill in skills:
        count = 0
        for keyword in skill[1].split():
            count = count + job_summary.count(keyword)
        if max < count:
            max = count
        skill_value.append((count, skill[0]))

    selected_skills = []
    max+=1
    while len(selected_skills) <= 3 and max > 0:
        max -= 1
        for skill in skill_value:
            if skill[0] == max:
                selected_skills.append(skill[1])
            if len(selected_skills) >= 3:
                break

    return selected_skills



def create_cv(company, skills):
    Title = company.get("title")
    companyName = company.get("company")
    companyLocation = company.get("location")
    InternFlag = 0
    index = 0
    keywords = ['Software', 'Developer', 'Mobile', 'Web']
    delimArray = ['\'', '\"', '\\', '|', '-', '_', '‧', '•']



    SplitList = re.split('; |, |- |\( |\) |/ |– ', Title)

    for potential in SplitList:
        for word in keywords:
            if "Intern" in potential:
                InternFlag = 1
            if "intern" in potential:
                InternFlag = 1
            if word in potential:
                Title = potential

    Title = Title.replace("/", "")

    newFile = open("CoverLetterDemoOutput_" + companyName + Title + ".txt", 'w+')
    with open("CoverLetterDemo.txt", 'r') as f:
        for line in f:
            line = line.rstrip()
            if "Title" in line:
                line = line.replace("Title", Title)
                newFile.write(line)
            elif "companyName" in line:
                line = line.replace("companyName", companyName)
                newFile.write(line + '\n')
            elif "companyLocation" in line:
                line = line.replace("companyLocation", companyLocation)
                newFile.write(line + '\n')
            elif "place skills here" in line:
                str = "\t-" + skills[0] + "\n\n\t-" + skills[1] + "\n\n\t-" + skills[2]
                line = line.replace("place skills here", str)
                newFile.write(line + '\n')
            else:
                newFile.write(line + '\n')

    f.close()
    newFile.close()

def create_cv_from_list(companies):
    for company in companies:
        skills = parse_skills_file()
        skills = choose_skills(company.get("summary"), skills)
        create_cv(company, skills)


if __name__ == "__main__":
    URL = "https://ca.indeed.com/jobs?q=software%20developer&l=Richmond%20Hill%2C%20ON&vjk=19e1a9fac332fc27"
    companies = create_company_info(URL)

    create_cv_from_list(companies)



