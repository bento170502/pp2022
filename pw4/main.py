import input as inp


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
    inp.sif()
  elif choice == 2:
    inp.cif()
  elif choice == 3:
    inp.MarkInput()
  elif choice == 4:
    inp.PrintStudentInfo()
  elif choice == 5:
    inp.PrintCourseInfo()
  elif choice == 6:
    inp.CourseMark()
  elif choice == 7:
    inp.avgGPA()
  elif choice == 8:
    inp.PrintStudentList()
  elif choice == 9:
    break
  else:
    print("Invalid input! Please enter again!")
