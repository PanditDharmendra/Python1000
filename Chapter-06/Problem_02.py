English = int(input("Enter the percentage of English: "))
Math = int(input("Enter the perrcentage of Math: "))
Science = int(input("Enter the percentage Science: "))
# check if total percentage is atleast 40 percent and each have atlest 33 percent are given or not.
if (English + Math + Science) >= 40 and (English >= 33 and Math >= 33 and Science>= 33):
    print("You are pass")
else:
    print('You are fail')
    