def storeinfo(courses):
    ccode = input("Enter course code: ").upper()
    if ccode not in courses:
        cname = input("Enter course name: ")
        cfac = input("Enter thr faculty name: ")
        nor = int(input("Enter number of registrations: "))
        courses[ccode] = {'course_name': cname, 'faculty': cfac, 'no_of_regs': nor}
    else:
        print("Duplicate entries not allowed!")


def dispall(courses):
    print("Details of all courses: ")
    for ccode in courses:
        for key in courses[ccode]:
            print(f"{key} : {courses[ccode][key]}")
        print()


def detailsof(courses,ccode):
    if ccode in courses:
        print(f"Details of course with course code {ccode} : ")
        print("Course name : ", courses[ccode]['course_name'])
        print("Course code : ", ccode)
        print("Faculty : ", courses[ccode]['faculty'])
        print("Number of registrations : ", courses[ccode]['no_of_regs'])
    else:
        print("Invalid course code")


def highestnor(courses):
    maxnor=0
    for ccode in courses:
        if courses[ccode]['no_of_regs'] > maxnor:
            maxnor = courses[ccode]['no_of_regs']
            course_name = ccode

    print(f"{course_name} has highest number of registrations")


def main():
    courses = {}
    ch = 0
    while ch != -1:
        print(
            "\nChoices: \n1.Store info\n2.Display details of all courses\n3.Find details od particular course\n4.Find course with highest number of registrations\n5.Exit\n")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            storeinfo(courses)
        elif ch == 2:
            dispall(courses)
        elif ch == 3:
            ccode = input("Enter course code to find details : ").upper()
            detailsof(courses, ccode)
        elif ch == 4:
            highestnor(courses)
        elif ch == 5:
            print("Exiting.....")
            ch = -1
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
