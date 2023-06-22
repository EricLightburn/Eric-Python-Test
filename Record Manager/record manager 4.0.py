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
        self.load_records()
    def load_records(self):
            if not Path(self.file_path).exists():
                self.create_file()
            with open(self.file_path, "r") as records:
                for line in records.readlines()[1:]:
                    fields = line.strip().split("\t")
                    record = Record(fields[1], fields[2], fields[3])
                    self.records.append(record)

    def create_file(self):
            with open(self.file_path, "w+") as create:
                create.write("#\t\t\tName\t\t\tAge\t\t\tInterests")
    def add_record(self):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        interests = input("Enter your interest: ")
        record = Record(name, age, interests)
        self.records.append(record)
        with open(self.file_path, "a") as writeRecord:
            writeRecord.write(f"\t\t\t{name}\t\t\t\t{age}\t\t\t\t{interests}\n")
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
                readRecords2.write("#\t\t\tName\t\t\tAge\t\t\tInterests\n")
                for record in self.records:
                    readRecords2.write(f"\t\t\t{record.name}\t\t\t{record.age}\t\t\t{record.interests}\n")
            print("Record Deleted.")
        else:
            print("Invalid record number.")
    def clear_records(self):
        self.records = []
        with open(self.file_path, "w") as f:
            f.truncate(0)
            f.write("#\t\t\tName\t\t\tAge\t\t\tInterests\t\t\t")
    def find_records(self, name):
        with open(self.file_path, "r") as f:
            for line in f:
                if name in line:
                    print(line)
print("==========================================================")
print(" ~ ----------------- Record Manager --------------------- ~")
print("===========================================================")
print("Available Operators:")
print("A) Add Record\t\tB) View Record")
print("C) Delete record\tD) Clear Records")
print("E) Exit manager\t\tF) Find Records \n")

selection = input('Enter selection: ').upper()      