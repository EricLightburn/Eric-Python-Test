import os    #started again on 3.0.py to avoid errors
import sys
from pathlib import Path


class Records:
    def __init__(self, choice):
        self.choice = choice
        if choice == "A":
            with open(r"c:\Users\training.user\Downloads\record.txt", "r") as records:
                for last_line in records:
                    pass
            if last_line[0] == "#":
                num = 1
            else:
                num = int(last_line[0]) + 1

            name = input("Enter your name: ")
            age = input("Enter your age: ")
            interests = input("Enter your interest: ")
            with open(r"c:\Users\training.user\Downloads\record.txt", "a") as writeRecord:
                writeRecord.write(f"{num}\t\t\t{name}\t\t\t\t{age}\t\t\t\t{interests}\n")
        elif choice == "B":
            with open(r"c:\Users\training.user\Downloads\record.txt", "r") as countRecords:
                count = len(countRecords.readlines()[1:])

                if count == 0:
                    print("There are no records")
                    print()
                else:
                    with open(r"c:\Users\training.user\Downloads\record.txt", "r") as readRecords:
                        print(readRecords.read())
        elif choice == "C":
            record_id = input("Enter Record #: ")
            with open(r"c:\Users\training.user\Downloads\record.txt", "r") as f:
                lines = f.readlines()
            with open(r"c:\Users\training.user\Downloads\record.txt", "w") as readRecords2:
                for line in lines:
                    if not line.startswith(record_id):
                        readRecords2.write(line)
            print("Record Deleted.")
        elif choice == "D":
            print("No records found.")
            with open(r"c:\Users\training.user\Downloads\record.txt", "r+") as f:
                f.truncate(0)
        elif choice == "E":
            sys.exit("Thank you!")
        else:
            print("Invalid response. Please try again.")


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
    print("E. Exit\n")

    selection = input('Enter selection: ').upper()
    Records(selection)