#Eligibility
testcases = int(input())
eligibility = ""
informationeligibility = list(range(0, testcases))
for i in range(testcases):
    information = input()
    name , secondary , birth , courses = map(str, information.split(" "))
    secyear , secmonth , secday = map(int, secondary.split("/"))
    birthyear, birthmonth, birthdate = map(int, birth.split("/"))
    if int(secyear) >= 2010:
        eligibility = "eligible"
    elif int(birthyear) >= 1991:
        eligibility = "eligible"
    elif int(courses) >= 41:
        eligibility = "ineligible"
    else:
        eligibility = "coach petitions"
    informationeligibility[i] = name + " " + eligibility
i = 0
for i in range(int(testcases)):
    print(informationeligibility[i])