import domains.class_student as student
import domains.class_course as course
import domains.class_marks_object as marks_object
import math
import numpy as np
studentlist = []

def getNumOfStudent():
    return int(input("Enter number of students : ")) 

def sif():
 for i in range(getNumOfStudent()):   
  stu = student.StudentInfo()
  studentlist.append(stu)

def getNumOfCourses():
  return int(input("Enter the number of courses : "))

courselist = []

def crd_of_course():
  return int(input("Enter the course's credit : "))
def cif():
 for i in range(getNumOfCourses()):
  cse = course.CourseInfo()
  courselist.append(cse)

stumarks = []

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
