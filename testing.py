from indeed_scraper import create_company_info


URL = "https://ca.indeed.com/jobs?q=software%20developer&l=Richmond%20Hill%2C%20ON&vjk=19e1a9fac332fc27"
companies = create_company_info(URL)

for company in companies:
    # variables
    Title = company[1]
    companyName = company[0]
    companyLocation = company[2]
    flag = 0
    index = 0
    delimArray = ['\'' , '\"', '\\' , '|', '-' , '_', '‧']

    newFile = open("CoverLetterDemoOutput_" + companyName, 'x+')
    with open("CoverLetterDemo.txt", 'r') as f:
        for line in f:
            line = line.rstrip()
            if "Title" in line:
                line = line.replace("Title", Title)
                newFile.write(line)
            elif "companyName" in line:
                line = line.replace("companyName", companyName)
                newFile.write(line)
            elif "companyLocation" in line:
                line = line.replace("companyLocation", companyLocation)
                newFile.write(line)
            else:
                newFile.write(line + '\n')




    print(Title)

    print(companyName)

    print(companyLocation)

    # closing text file
    #
    f.close()
    newFile.close()