marks=input("enter your marks: ")
marks=int(marks)

if marks >= 91:
  grade = "O"
elif marks >= 81:
  grade = "A+"
elif marks >= 71:
  grade = "A"
elif marks >= 61:
  grade = "B+"
elif marks >= 56:
  grade = "B"
elif marks >= 51:
  grade = "C"
else:
  grade = "F"

print("your grade is ", grade)