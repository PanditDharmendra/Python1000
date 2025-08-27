def greatest():
    number = []
    for i in range(3):
        User = int(input(f"Enter {i+1} numbers: "))
        number.append(User)
    get = max(number)
    print("The greatest nummber is ", get)


greatest()

