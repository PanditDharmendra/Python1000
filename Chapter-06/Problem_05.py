list = ["Rohan", "Ravi", 'Amritu',"Bikee", 'Puja']
User_input = input("Enter the Name:").upper() # Convert inpu to uppercase
if any(phrase.upper() in User_input for phrase in list):
    print("The name is in the list")
else:
    print('The name is not in the list')