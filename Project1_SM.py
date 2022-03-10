school = {
    "Name": "SARA",
    "Phone_Number": 1234567890,
    "Website": "https://saragroup.com",
    "Address": {"Road_Number": 101,
                "Street": "East Road",
                "City": "Varanasi",
                "State": "Uttar-Pradesh",
                "Pin_Code": 221006
    },
    "Pin_Code": 221005,
    "Staff": [
        {
        "Name": "Avinash Pandey",
        "Role": "Teacher",
        "Subjects": ["English","Science"],
        "Phone_Number": 1234567891
    },
    {
        "Name": "Ritesh Srivastav",
        "Rloe": "Teacher",
        "Subjects": "Maths",
        "Phone_Number": 1234567892
    },
    {
        "Name": "Prakash Kumar",
        "Role": "Teacher",
        "Subjects": "Physical Training",
        "Phone_Number": 1234567893
    }],
    "Students": [
        {
         "Name": "Harsh",
         "Contact_Number": 1234567894,
         "Subjects": {"Maths": 80,"English": 73,"Science": 78,"Hindi": 85},
         "Grade": None
        },
        {
        "Name": "Rahul",
        "Contact_Number": 1234567895,
        "Subjects": {"Maths":71, "English": 81, "Science": 89, "Hindi": 73},
        "Grade": None
    },
        {
        "Name": "Shiva",
         "Contact_Number": 1234567896,
         "Subjects": {"Maths": 70,"English": 63,"Science": 58,"Hindi": 65},
         "Grade": None
    },
    {
         "Name": "Amit",
         "Contact_Number": 1234567897,
         "Subjects": {"Maths": 69,"English": 73,"Science": 78,"Hindi": 75},
         "Grade": None
    }],
    "Admission_Cell": [
        {
            "Name": "Hari Babu",
            "Classes": "Pre Primary Classes",
            "Role": "Admission_Officer",
            "Phone_Number": 1234567898
        },
        {
            "Name": "Swathi",
            "Classes": "Primary Classes",
            "Role": "Admission_Officer",
            "Phone_Number": 1234567899 
        },
        {
            "Name": "Swetha Kumari",
            "Classes": "Middle Classes",
            "Role": "Admission_Officer",
            "Phone_Number": 1234567892
        },
        {
            "Name": "Ashish Kumar",
            "Classes": "Secondary and senior-Secondary Classes",
            "Role": "Admission_Officer",
            "Phone_Number": 1234567893
        }],
        "Transportation_Management": [
            {
                "Name": "Ram kumar",
                "Bus_Number": 35,
                "Phone_Number": 1234567894 
            },
            {
                "Name": "Krishna kumar",
                "Bus_Number": 36,
                "Phone_Number": 1234567895
            },
            {
                "Name": "Shiv Shankar",
                "Bus_Number": 40,
                "Phone_Number": 1234567896
            }],
            "Fees_Structure": {
                "Pre_Primary_Classes": 600,
                "Primary_Classes": 850,
                "Middle_Classe": 1050,
                "Secondary_Classes": 1600,
                "Senior_Secondary_Classes": 2300,
                "Foundation_Course": 50000,
                "Transportation_Charge": 850,
                "Extra_Curricular_Activities": 1200,
                "Anual_Function": 2500
            }
    }

# # get_Students_percentage , Here we are getting percentages for students from school.
def get_Students_percentage(school):
    total_subjects_marks = school["Subjects"]["Maths"]+school["Subjects"]["English"]+school["Subjects"]["Science"]+school["Subjects"]["Hindi"]
    percentage = total_subjects_marks/4
    return percentage

# # Here we are getting percentage for first student from school.
p0 = get_Students_percentage(school["Students"][0])
print("The percentage for the first student is",p0)

# get_Studenta_percentage , Here weare getting percentage for second student from school
p1 = get_Students_percentage(school["Students"][1])
print("The percentage for the second student is",p1)

# get_Studenta_percentage , Here weare getting percentage for third student from school.
p2 = get_Students_percentage(school["Students"][2])
print("The percentage for the third student is",p2)


# get_staff_of_school , Here we are getting staff details from school.
def get_staff_of_school (school):
    return school["Staff"]
d = get_staff_of_school(school)
print(d)


# get_fees_details_of_school , Here we wre getting fees details from school.
def get_fees_details_of_school (school):
    return school["Fees_Structure"]
f = get_fees_details_of_school(school)
print(f)

# get_school_transportation , Here we are getting transportation management details from school.
def get_school_transportation (school):
    return school["Transportation_Management"]
print(get_school_transportation(school))


# get_school_admission_details, Here we are getting details about the admission cell from school.
def get_school_admission_details (school):
    return school["Admission_Cell"]
print(get_school_admission_details(school))

# get_number_of_teachers_from_staff , Here we are getting the number of teachers working in school.
def get_number_of_teachers_from_staff(school):
    return len(school["Staff"])
print(get_number_of_teachers_from_staff(school))

# get_numbers_of_the_students , Here we are getting numbers of students from school.
def get_numbers_of_the_students (school):
    return len(school["Students"])
print(get_numbers_of_the_students(school))

# get_name_of_school , Here we are getting the name of the school.
def get_name_of_school (school):
    return school["Name"]
print(get_name_of_school(school))

# get_phone_number_of_school , Here we are getting phone number of the school.
def get_phone_number_of_school (school):
    return school["Phone_Number"]
print(get_phone_number_of_school(school))

# get_address_of_school , Here we are getting address of the schhol.
def get_address_of_school (school):
    return school["Address"]
print(get_address_of_school(school))

# get_website_of_school , Here we are getting website of the school.
def get_website_of_school (school):
    return school["Website"]
print(get_website_of_school(school))

# get_student_details_by_name , Here we are getting details of the student by there name using loop.
def get_student_details_by_name(school,name):
    for student in school["Students"]:
        if student["Name"] == name:
            return student
print(get_student_details_by_name(school,"Harsh"))
print(get_student_details_by_name(school,"Shiva"))
print(get_student_details_by_name(school,"Rahul"))
print(get_student_details_by_name(school,"Amit"))
print(get_student_details_by_name(school,"Akas")) # if students not present in school, it will throw None

# get_details_for_teacher_by_name , Here we are getting the details for teacher's of school by there name using loop.
def get_details_for_teacher_by_name (school,name):
    for teacher in school["Staff"]:
        if teacher["Name"] == name:
            return teacher
print(get_details_for_teacher_by_name(school,'Avinash Pandey'))
print(get_details_for_teacher_by_name(school,'Ritesh Srivastav'))
print(get_details_for_teacher_by_name(school,'Prakash Kumar'))
print(get_details_for_teacher_by_name(school,'Kiran Singh')) # If teacher is not present in school,will throw none.

# get_teacher_details_by_subjects, Here we are getting teacher's details by subjects using for loop. 
def get_teacher_details_by_subjects (school,subject):
    for teacher in school["Staff"]:
        if teacher["Subjects"] == subject:
            return teacher
print (get_teacher_details_by_subjects(school,"Maths"))
print (get_teacher_details_by_subjects(school,["English","Science"]))
print (get_teacher_details_by_subjects(school,"Physical Training"))


# get_details_for_admission_middleclasse , Here we are getting details about admission cell department for middle classes
def get_details_for_admission_in_school (school,name_of_classes): 
    for classes in school["Admission_Cell"]:
        if classes["Classes"] == name_of_classes: 
            return classes
print(get_details_for_admission_in_school(school,"Pre Primary Classes"))
print(get_details_for_admission_in_school(school,"Primary Classes"))
print(get_details_for_admission_in_school(school,"Middle Classes"))

# get_list_of_teachers_by_role , Here we are getting details of teacher by his role using loop.
def get_list_of_teachers_by_role (school):
    for teacher in school["Staff"] :
        if teacher["Role"] == "Teacher":
            return teacher
print(get_list_of_teachers_by_role(school))

# get_list_of_students , Here we are getting list of the students.
def get_list_of_students (school):
    list_of_students=[]
    for students in school["Students"]:
        list_of_students.append(students["Name"])
    return list_of_students
print(get_list_of_students(school))

# get_list_of_teachers , Here we are getting list of teachers.
def get_list_of_teachers (school):
    list_of_teacher=[]
    for staff in school["Staff"]:
        list_of_teacher.append(staff["Name"])
    return list_of_teacher
print(get_list_of_teachers(school))

# get_list_of_buses , Here we are getting list of buses
def get_list_of_buses (school):
    list_of_buses=[]
    for buses in school["Transportation_Management"]:
        list_of_buses.append(buses["Bus_Number"])
    return list_of_buses
print(get_list_of_buses(school))

# get_bus_details , Here we are getting bus details by bus number using for loop.
def get_bus_details (school,bus_number):
    for bus in school["Transportation_Management"]:
        if bus["Bus_Number"] == bus_number:
            return bus
print(get_bus_details(school,35))
print(get_bus_details(school,36))
print(get_bus_details(school,40))
print(get_bus_details(school,37)) # If bus number is not present in school, it will throw None


def get_numbers_of_teachers (school):
    return len(school["Staff"])
print(get_numbers_of_teachers(school))

def get_numbers_of_the_students (school):
    return len(school["Students"])
print(get_numbers_of_the_students(school))

def get_list_of_bus_numbers(school):
    list_of_bus_numbers=[]
    for buses in school["Transportation_Management"]:
        list_of_bus_numbers.append(buses["Bus_Number"])
    return list_of_bus_numbers
print(get_list_of_bus_numbers(school))

def get_bus_details (school,bus_number):
    for buses in school["Transportation_Management"]:
        if buses["Bus_Number"] == bus_number:
            return buses
print(get_bus_details(school,35))
print(get_bus_details(school,36))
print(get_bus_details(school,37))
print(get_bus_details(school,40))

