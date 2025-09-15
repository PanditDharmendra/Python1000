# 11. Write a python program to rename a file to “renamed_by_ python.txt.
import os
def rename_file( old_name, new_name):
    os.rename(old_name, new_name)
    print("File renamed sucessfully")

rename_file("renamed.txt", "renamed_by_python.txt")