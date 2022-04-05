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