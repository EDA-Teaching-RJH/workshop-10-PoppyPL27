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
    
    #function to return string displaying all the students key attributes
    def __str__(self):
        return f"name: {self.name} \ndegree: {self.degree}\nstudent ID: {self.student_id}"
    
    #getter for degree
    @property
    def degree(self):
        return self._degree
    
    #setter for degree
    @degree.setter
    def degree(self, degree):
        if degree not in ["ECE", "BIO", "MECH", "EEE"]:
            raise ValueError("Invalid degree")
        self._degree = degree

class 

def main():
    





#beginning of main code
main()