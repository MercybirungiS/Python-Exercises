# Removing  the argv feature from the sys package
from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here is your file {filename}:")
print(txt.read())

txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()

# code that i wrote in the terminal to open the file 
# filename = input()
# ex15_sample.txt
# >>> txt = open(filename)
# >>> txt.read()