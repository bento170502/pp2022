#Input number of students and student's info
def getNumOfStudent():
    return int(input("Enter number of students : ")) 

studentlist = []

class student: 
  def __init__(self,id,name,DOB):
    self.id = id
    self.name = name
    self.DOB = DOB
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
def cif():
 for i in range(getNumOfCourses()):
  cse = course.CourseInfo()
  courselist.append(cse)



stumarks = {}
def MarkInput(): 
 CourseID = input("Enter the course's ID : ")
 if CourseID not in [CourseInfo.id for CourseInfo in courselist]:
       print(" The course's id isn't founded! Please try again!")
 else:
  nm = int(input("Number of student that you want to enter marks: "))
  for i in range(nm):
    while True: 
      StuID = input("Enter a student's ID : ")
      if StuID not in [StudentInfo.id for StudentInfo in studentlist]:
        print("The student's ID isn't founded! Please try again! ")
        continue
      break
    marks = float(input("Enter the mark: "))
    if CourseID in stumarks:
      stumarks[CourseID].append((StuID,marks))
    else:
      stumarks[CourseID] = [(StuID,marks)]

def PrintStudentInfo():
  for student in studentlist:
    print(f"Student's ID :{student.id}  Name: {student.name}  DOB: {student.DOB}")

def PrintCourseInfo():
  for course in courselist:
    print(f"Course's ID :{course.id}  Name: {course.name}") 

def CourseMark():
  CourseID = input("Enter a couse ID to show the mark : ")
  if CourseID in stumarks:
    for sm in stumarks[CourseID]:
      print(f"Student's ID :{sm[0]}  Mark: {sm[1]}")


print("ENTER A NUMBER IN THE LIST BELOW TO SELECT THE FUNCTION YOU WANT TO USE: ")
while True: 
  print("1. Input student's info")
  print("2. Input course's info")
  print("3. Input student's marks")
  print("4. Print student's info")
  print("5. Print course's info")
  print("6.Enter a course ID to show the mark")
  print("7. Exit")
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
    break
  else:
    print("Invalid input! Please enter again!")