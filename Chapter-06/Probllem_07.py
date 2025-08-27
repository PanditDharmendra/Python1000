list = ["harry"]
user_input = input("Enter the post: ").lower()
if (phrase in user_input for phrase in list):
    print("It talking about harry")
else:
    print("It is not talking about harry")
 