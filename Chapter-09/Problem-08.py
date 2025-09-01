# Write a program to make a copy of a text file “this. txt”
import shutil

with open("poem.txt", "r") as f:
    file = f.read()

shutil.copyfile("poem.txt", "this.txt")