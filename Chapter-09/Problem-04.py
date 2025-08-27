word = "Donkey"
with open("Donkey.txt", "r") as file:
    content = file.read()

contents = content.replace(word, "####")

with open("Donkey.txt", "w") as file:
    file.write(contents)
    
print("Content updated succssfully.")