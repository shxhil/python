# def  display_emp(**kwargs):   #dictionary aaayt idkkm, key vech idkkan aayt eg:name=shahil
#     print(kwargs.get("name"))
#     print(kwargs.get("salary"))


# display_emp(name="hari",dept="hr",place="ekm",location="tkm",salary=240000)



#create a function display_student and print student name and course

#display_student(name="ravi",course="django",role=1000,gender="male")


def display_student(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("course"))

display_student(name="ravi",course="django",role=1000,gender="male")
