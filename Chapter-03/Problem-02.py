letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>'''

# Replace the placeholder with actual values
Name = input("Enter the name:")
Date = input("Enter the date: ")

letter = letter .replace("<|Name|>", Name )
letter = letter.replace("<|Date|>", Date )

print(letter)