# 6. Write a program to mine a log file and find out whether it contains ‘python’.
with open("log.txt", "r") as f:
    str = f.read()
print(str)
if "python" in str:
    print("Yes, Python is presents in log file!")
else:
    print("surry, python is not here!")

