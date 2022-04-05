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