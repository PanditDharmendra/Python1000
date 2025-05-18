marks = []
# Taking input of marks of 6 students
for i in range(6):
    mark = int(input(f"Enter the marks of student{i + 1}: "))
    marks.append(mark)
    mark =+ 1
#sorting them in ascending order
marks.sort()
print("The marks of the students are:",marks)
