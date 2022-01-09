import re
from fpdf import FPDF
from indeed_scraper import create_company_info


URL = "https://ca.indeed.com/jobs?q=software%20developer&l=Richmond%20Hill%2C%20ON&vjk=19e1a9fac332fc27"
companies = create_company_info(URL)

for company in companies:
    # variables
    Title = company[1]
    companyName = company[0]
    companyLocation = company[2]
    InternFlag = 0
    index = 0
    keywords = ['Software', 'Developer', 'Mobile', 'Web']
    delimArray = ['\'' , '\"', '\\' , '|', '-' , '_', '‧', '•']


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

    newFile = open("CoverLetterDemoOutput_" + companyName + Title, 'w+')
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
            else:
                newFile.write(line + '\n')

    # pdf = FPDF()
  
    # # insert the texts in pdf
    # for x in newFile:
    #     pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
   
    # # save the pdf with name .pdf
    # pdf.output("mygfg.pdf")











print(companyName)

print(companyLocation)

# closing text file 
#   
f.close()
newFile.close()