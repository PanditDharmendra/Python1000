# 7. Write a program to find out the line number where python is present from ques 6.
with open("log.txt", "r") as f:
    str = f.read()
index = str.find("python")
print(index)