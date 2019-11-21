# This script creates an empty file with filename current date Time
import datetime

filename=datetime.datetime.now();

def createFile():
    with open(filename,"w") as file:
        file.write("") # Writes an empty string

createFile()