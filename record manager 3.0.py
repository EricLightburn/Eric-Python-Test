import os
import sys                  
from pathlib import Path

class Records:                     #struggled to switch to using more classes
    def __init__(self, choice):
        self.choice = choice
        self.file_path = r"c:\Users\training.user\Downloads\record.txt"   #makes it much easier to change file location
        if choice == "A":
            with open(self.file_path, "r") as records:
                for last_line in records:
                    pass
            if last_line[0] == "#":
                num = 1
            else:
                num = int(last_line[0]) + 1

            name = input("Enter your name: ")           #when it tried to switch to using functions, it wouldn't work like my excel test
            age = input("Enter your age: ")
            interests = input("Enter your interest: ")
            with open(self.file_path, "a") as writeRecord:
                writeRecord.write(f"{num}\t\t\t{name}\t\t\t\t{age}\t\t\t\t{interests}\n")
        elif choice == "B":
            with open(self.file_path, "r") as countRecords:
                count = len(countRecords.readlines()[1:])

                if count == 0:
                    print("There are no records")
                    print()
                else:
                    with open(self.file_path, "r") as readRecords:
                        print(readRecords.read())
        elif choice == "C":
            record_id = input("Enter Record #: ")
            with open(self.file_path, "r") as f:
                lines = f.readlines()
            with open(self.file_path, "w") as readRecords2:
                for line in lines:
                    if not line.startswith(record_id):
                        readRecords2.write(line)
            print("Record Deleted.")
        elif choice == "D":
            print("No records found.")
            with open(self.file_path, "r+") as f:
                f.truncate(0)
        elif choice == "E":
            sys.exit("Thank you!")
        elif choice == "F":                                     #implementation of find/get option
            name = input("Enter name to search for: ")
            self.find(name)
        else:
            print("Invalid response. Please try again.")

    def find(self, name):
        with open(self.file_path, "r") as f:
            for line in f:
                if name in line:
                    print(line)

while True:
    def createFile():
        with open(r"c:\Users\training.user\Downloads\record.txt", "w+") as create:
            create.write("#\t\t\tName\t\t\t        Age\t\t\t        Interests\n")
    if Path(r"c:\Users\training.user\Downloads\record.txt"):
        if os.stat(r"c:\Users\training.user\Downloads\record.txt").st_size != 0:
            with open(r"c:\Users\training.user\Downloads\record.txt", "r+") as readFirstLine:
                first = readFirstLine.readlines()[0][0]
                if first != "#":
                    readFirstLine.write("#\t\t\tName\t\t\t       Age\t\t\t       Interests\n")
        else:
            createFile()
    else:
        createFile()

    print("==========================================================")
    print(" ~ ----------------- Record Manager --------------------- ~")
    print("===========================================================")
    print("Available Operators:")
    print("A) Add Record\t\tB) View Record")
    print("C) Delete record\tD) Clear Records")
    print("E) Exit manager\t\tF) Find Records \n")

    selection = input('Enter selection: ').upper()
    Records(selection)