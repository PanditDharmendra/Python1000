fruits = []
count = 0

# The user is prompted to enter 7 fruit names
while count < 7:
    fruit = input(f"Enter fruit name {count + 1}: ")
    fruits.append(fruit)
    count += 1

print("You entered the following fruits:")
print(fruits)



