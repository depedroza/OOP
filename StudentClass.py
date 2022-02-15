class Student:
    def __init__(self, studentID, name, DOB, classification):
        self.__studentID = studentID
        self.__name = name
        self.__studentDOB = DOB
        self.__class = classification

    def calculate_age(self, YEAR):
        age = YEAR - self.__studentDOB
        return age

    def get_registration_time(self, classification):
        if self.__class == "Senior":
            registrationTime = "11/1 thru 11/3"
        elif self.__class == "Junior":
            registrationTime = "11/4 thru 11/6"
        elif self.__class == "Sophomore":
            registrationTime = "11/7 thru 11/9"
        elif self.__class == "Freshman":
            registrationTime = "11/10 thru 11/12"
        return registrationTime
