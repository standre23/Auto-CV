
  
# opening a text file
file1 = open("IndeedSample.txt", "r")


# variables
Title = "Title"
companyName = "companyName"
companyLocation = ""
flag = 0
index = 0
delimArray = ['\'' , '\"', '\\' , '|', '-' , '_', '‧']
  
# Loop through the file line by line
for line in file1: 

    if Title in line:
        line = line.replace("Title = ", "")
        Title = line
    if companyName in line:
        line = line.replace("companyName = ", "")
        companyName = line
    if companyLocation in line:
        line = line.replace("companyLocation = ", "")
        companyLocation = line


      
   
newFile = open("CoverLetterDemoOutput", 'x+')
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
file1.close() 
newFile.close()