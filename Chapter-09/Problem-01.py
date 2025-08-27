def find():
    f = open("poem.txt", 'r')
    text = f.read()
    print(text)
    found = text.find("twinkle")
    print(found)

    f.close()

find()
