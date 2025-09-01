# Write a program to find out whether a file is identical & matches the content of 
# another file
with open("this.txt", "r") as f:
    index1 = f.read()

with open("poem.txt", "r") as f:
    index2 = f.read()

if index1 == index2:
    print("Both files are same")

else: print("Files are not same")


