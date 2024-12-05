class student():

    def __init__(self, name, degree, student_id):

        #check and set student name 
        if not name:
            raise ValueError("missing name")
        self.name = name

        #check and set student degree
        if degree not in ["ECE", "BIO", "MECH", "EENG"]:
            raise ValueError("invalid degree")
        self.degree = degree

        #check and set student id
        if len(student_id) != 6 and student_id.isdigit() == False:
            raise ValueError("invalid student id")
        self.student_id = student_id
    
    def __str__(self):
        return f"name: {self.name} \ndegree: {self.degree}\nstudent ID: {self.student_id}"

def main():
    Student = newstudent()
    print(f"name: {Student.name} \ndegree: {Student.degree}\nstudent ID: {Student.student_id}")

def newstudent():
    name = input("Name: ")
    degree = input("degree: ")
    student_id = input("student id: ")
    Student = student(name, degree, student_id)
    return Student



#beginning of main code
main()