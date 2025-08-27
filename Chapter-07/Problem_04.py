Prime_number =int(input("Enter the Number:"))

for i in range(2, Prime_number):
    if (Prime_number % 2) == 0:
        print("This is not a Prime Number")
        break
else:
    print("This is  a prime Number")


