def remove(l, word):
    n = []
    for item in l:
        if item != word:
            n.append(item.strip(word))
    return n

l = ["Rohan", "apple", "graphs", "an"]

print(remove(l, "an"))