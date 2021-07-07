# Read the argv feature from the sys package
from sys import argv
# Need to get two parameters from the command line
script, filename = argv
# f-string
print(f"We are going to erase {filename}.")
print("If you don't want that hit CTRL-C (^C).")
print("If you do want that hit RETURN.")

input('?')

print("Opening the file...")
# Open the file in write-only mode and return the file object. This file object cannot be read, only write
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file..")

print("First time...")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Second time...")
fline = f"{line1}\n{line2}\n{line3}\n"
target.write(fline)

print("Third time...")
line = "{}\n{}\n{}\n"
target.write(line.format(line1,line2,line3))

print("And finally, we close it.")
target.close()
