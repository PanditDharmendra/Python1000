word = ["gadaha", "Donkey", "bad"]
with open("Donkey.txt", "r") as file:
    line = file.read()
for word in word:
    line = line.replace(word, "#"* len(word))

with open("Donkey.txt", "w") as file:
    file.write(line)
    
