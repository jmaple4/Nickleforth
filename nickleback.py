# This is a program that prompts for a file name, then opens that file and 
# reads through the file, and print the contents of the file backwards. 
# you know...so Nicklebackk lyrics look like devil verses

fileName = input("Enter file name: ")

try:
    fileHandle = open(fileName)
except:
    print('File cannot be opened:', fileName)
    quit()

print("\nThese are the regular lyrics\n".upper())

for line in fileHandle:
    line = line.rstrip()
    print(line)
# line = line.rstrip()[::-1] # this slicing reverses the strings characters: [::-1]
# line = line[::-1] # this slicing reverses the strings characters: [::-1]
# print('Here it is as satanic verse')
# print(line)