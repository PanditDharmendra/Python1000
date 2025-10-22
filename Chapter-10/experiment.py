#👉 This simple test will solidify your understanding of
#  how Python attribute resolution order works (Instance → Class → Parent Classes).
class Demo:
    x = 1

d1 = Demo()
d2 = Demo()

Demo.x = 5

d1.x = 99
print(d1.x, d2.x, Demo.x)
