import math 
import numpy as np
#Input number of students and student's info
def getNumOfStudent():
    return int(input("Enter number of students : ")) 

studentlist = []

class student: 
  def __init__(self,id,name,DOB):
    self.id = id
    self.name = name
    self.DOB = DOB
    self.avgGPA = None
  @classmethod
  def StudentInfo(cls):
    return cls(
     input("Enter the student's id : "),
     input("Enter the student's name : "),
     input("Enter the student's DOB : ")
      )
def sif():
 for i in range(getNumOfStudent()):   
  stu = student.StudentInfo()
  studentlist.append(stu)



#Input the number of courses and the course's info
def getNumOfCourses():
  return int(input("Enter the number of courses : "))



courselist = []
class course: 
  def __init__(self,id,name):
    self.id = id
    self.name = name
    
  @classmethod
  def CourseInfo(cls):
    return cls(
     input("Enter the course ID : "),
     input("Enter the course name : ")
      )
   
def crd_of_course():
  return int(input("Enter the course's credit : "))
def cif():
 for i in range(getNumOfCourses()):
  cse = course.CourseInfo()
  courselist.append(cse)

stumarks = []
class marks_object:
  def __init__(self,CID, SID,SN, m,crd):
    self.CID = CID
    self.SID = SID
    self.SN = SN
    self.m = m
    self.crd = crd
 

  
def RoundDown(): 
    x = float(input("Enter the mark : "))
    return math.floor( x * 10) / 10

def MarkInput(): 
 CourseID = input("Enter the course's ID : ")
 credit = crd_of_course()
 if CourseID not in [CourseInfo.id for CourseInfo in courselist]:
       print(" The course's id isn't founded! Please try again!")
 else:
  nm = int(input("Number of student that you want to enter marks: "))
  for i in range(nm):
    while True: 
      StuID = input("Enter a student's ID : ")
      SN = input("Enter the student's name : ")
      if StuID not in [StudentInfo.id for StudentInfo in studentlist]:
        print("The student's ID isn't founded! Please try again! ")
        continue
      if SN not in [StudentInfo.name for StudentInfo in studentlist]:
        print("The student's name isn't founded! Please try again! ")
        continue
      break
    marks = RoundDown()
    obj = marks_object(CourseID,StuID,SN,marks,credit)
    stumarks.append(obj)
 

def PrintStudentInfo():
  for student in studentlist:
    print(f"Student's ID :{student.id}  Name: {student.name}  DOB: {student.DOB}")


def PrintCourseInfo():
  for course in courselist:
    print(f"Course's ID :{course.id}  Name: {course.name}") 

def CourseMark():
  CourseID = input("Enter a couse ID to show the mark : ")
  for sm in stumarks:
    if sm.CID == CourseID:
      print(f"Student's ID :{sm.SID} Student's name:{sm.SN}  Mark: {sm.m}")


def avgGPA():
  coursecredit = []
  coursemark = []
  avgcourse= []
  totalcrd = []
  sid = input("Enter the student's ID : ") 
  for course in stumarks:
    if sid in course.SID:
      coursecredit.append(course.crd)
      coursemark.append(course.m)
      totalcrd.append(course.crd)
  coursecredit = np.array(coursecredit)
  coursemark = np.array(coursemark)
  output = np.multiply(coursecredit,coursemark)
  avgcourse.append(output)
  totalcrd = np.array(totalcrd)
  totalcrd = np.sum(totalcrd)
  avgcourse = np.array(avgcourse)
  avgcourse = np.sum(avgcourse)
  avgGPA = round(avgcourse/totalcrd,2)
  for std in studentlist:
    if sid in std.id:
      std.avgGPA = avgGPA
  print(f"Student's GPA : {avgGPA}")



  

def PrintStudentList():
  for student in studentlist:
   studentlist.sort(key=lambda x: x.avgGPA, reverse=True) #
  for student in studentlist:
    print(f"Student's ID :{student.id}  Name: {student.name}  DOB: {student.DOB}  GPA: {student.avgGPA}")
      

print("ENTER A NUMBER IN THE LIST BELOW TO SELECT THE FUNCTION YOU WANT TO USE: ")
while True: 
  print("1. Input student's info")
  print("2. Input course's info")
  print("3. Input student's marks")
  print("4. Print student's info")
  print("5. Print course's info")
  print("6.Enter a course ID to show the mark")
  print("7. GPA of a student")
  print("8. Sorted student's list")
  print("9.Exit")
  choice = int(input("Enter a number : "))
  if choice == 1:
    sif()
  elif choice == 2:
    cif()
  elif choice == 3:
    MarkInput()
  elif choice == 4:
    PrintStudentInfo()
  elif choice == 5:
    PrintCourseInfo()
  elif choice == 6:
    CourseMark()
  elif choice == 7:
    avgGPA()
  elif choice == 8:
    PrintStudentList()
  elif choice == 9:
    break
  else:
    print("Invalid input! Please enter again!")