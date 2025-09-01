# 10. Write a program to wipe out the content of a file using python.
with open("this.txt1", "w") as f:
    index = f.write("")

print(index)

