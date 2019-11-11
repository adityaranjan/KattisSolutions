#Prerequisites?
while True:
    Input = input()
    if Input == "0":
        break
    else:
        NumCoursesTaken, NumCategories = map(int, Input.split(" "))
        CoursesTaken = list(map(int, input().split(" ")))
        CategoryCheck = 0
        i = 0
        for i in range(NumCategories):
            CategoryList = list(map(int, input().split(" ")))
            CourseCheck = 0
            NumCoursesNeeded = CategoryList[1]
            del CategoryList[0]
            del CategoryList[0]
            j = 0
            for j in range(len(CategoryList)):
                if CategoryList[j] in CoursesTaken:
                    CourseCheck += 1
            if CourseCheck >= NumCoursesNeeded:
                CategoryCheck += 1
        if CategoryCheck == NumCategories:
            print("yes")
        else:
            print("no")