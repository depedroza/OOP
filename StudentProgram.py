import StudentClass as s


def main():
    YEAR = 2022
    new_student = s.Student(901856147, "Daniel Pedroza", 1995, "Senior")

    age = new_student.calculate_age(YEAR)
    print("The student's age is", age)

    registrationTime = new_student.get_registration_time("Senior")
    print("This student should register during the range of:", registrationTime)


main()
