user_input = int(input("Enter your mark:"))

if 1 <= user_input <= 100:
    if user_input >= 90:
        print("Excellent")
    elif user_input >= 80:
        print("A")
    elif user_input >= 70:
        print("B")
    elif user_input >= 60:
        print("C")
    elif user_input >= 50:
        print("D")
    else:
        print("Fail")
else:
    print('You have entered an invalid mark')

