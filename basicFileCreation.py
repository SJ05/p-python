# This script creates an empty file

filename="emptyFile"

def createFile():
    with open(filename,"w") as file:
        file.write("") # Writes an empty string