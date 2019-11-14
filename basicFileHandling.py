# open the file
file=open("helloworld.txt","r")
# read the content of the file
content=file.read()
# print the content of the file
print(content)
# means go back to the first line
file.seek(0)

# notes to remember
'''
r opens aa file for reading only. file pointer is at the beginning of the file.
r+ opens a file for both reading and writing. file pointer at the beginning
w opens a file for both writing and reading. overwrites the existing file. creates a new file if the file does not exist
w+ opens a file for writing and reading. same as while
a opens a file to append file pointer at the end of the file existi. it creates a new file if the file does not exist.
a+ opens a file for both appending and reading. same as a
'''

# with open("example.txt","a+") as file: when put in the python console will immediately execute the things you wanted to do.
