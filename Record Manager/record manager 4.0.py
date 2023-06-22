import os
import sys
from pathlib import Path

class Record:
    def __init__(self, name, age, interests):
        self.name = name
        self.age = age
        self.interests = interests

class RecordManager:
    def __init__(self):
        self.file_path = r"c:\Users\training.user\Downloads\record.txt"
        self.records = []
        self.record_count = 0
        self.load_records()
    def load_records(self):
        if not Path(self.file_path).exists():
            self.create_file()
        with open(self.file_path, "r") as records:
            for line in records.readlines()[1:]:
                fields = line.strip().split("\t")
                if len(fields) < 4:
                    print(f"Error: Line '{line.strip()}' does not have the expected format.")   #error handling to continue code even if format is not correct
                    continue
                record = Record(fields[1], fields[2], fields[3])
                self.records.append(record)
    def create_file(self):
        with open(self.file_path, "w+") as create:
            create.write("#\t\t\tName\t\t\t\t\tAge\t\t\t\tInterests\n")
    def add_record(self):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        interests = input("Enter your interest: ")
        record = Record(name, age, interests)
        self.record_count += 1                          #record count clearly shows which record is which number
        self.records.append(record)
        with open(self.file_path, "a") as writeRecord:
            writeRecord.write(f"{self.record_count}\t\t\t{name}\t\t\t\t{age}\t\t\t\t{interests}\n")  #record count under #
    def view_records(self):
        if len(self.records) == 0:
            print("There are no records")
            print()
        else:
            with open(self.file_path, "r") as readRecords:
                print(readRecords.read())
    def delete_record(self):
        record_id = int(input("Enter Record #: ")) - 1
        if 0 <= record_id < len(self.records):
            del self.records[record_id]
            with open(self.file_path, "w") as readRecords2:
                readRecords2.write("#\t\t\tName\t\t\t\tAge\t\t\t\tInterests\n")
                for record in self.records:
                    readRecords2.write(f"\t\t\t{record.name}\t\t\t\t{record.age}\t\t\t\t{record.interests}\n")
            print("Record Deleted.")
        else:
            print("Invalid record number.")
    def clear_records(self):
        self.records = []
        with open(self.file_path, "w") as f:
            f.truncate(0)
            f.write("#\t\t\tName\t\t\t\tAge\t\t\t\tInterests\t\t\t\n")
    def find_records(self):
        name = input("Enter name to search for: ")
        with open(self.file_path, "r") as f:
            for line in f:
                if name in line:
                    print(line)
manager = RecordManager()

while True:            #print in loop so displayed after completing any option
    print("==========================================================")
    print(" ~ ----------------- Record Manager --------------------- ~")
    print("===========================================================")
    print("Available Options:")
    print("A) Add Record\t\tB) View Record")
    print("C) Delete Record\tD) Clear Records")
    print("E) Exit Manager\t\tF) Find Records \n")

    selection = input('Enter selection: ').upper()
    if selection == 'A':
        manager.add_record()
    elif selection == 'B':
        manager.view_records()
    elif selection == 'C':
        manager.delete_record()
    elif selection == 'D':
        manager.clear_records()
    elif selection == 'F':
        manager.find_records()
    elif selection == 'E':
        sys.exit()
    else:
        print("Invalid selection. Please try again.")
