import os
from pathlib import Path
import sys 

class Record:
    def __init__(self, name, age, interests):
        self.name = name
        self.age = age
        self.interests = interests

class RecordFile:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            self.create_file()
    
    def create_file(self):
        with open(self.file_path, "w+") as create:
            create.write("#\t\t\tName\t\t\t\t\tAge\t\t\t\tInterests\n")
    
    def read_records(self):
        records = []
        with open(self.file_path, "r") as records_file:
            for line in records_file.readlines()[1:]:
                fields = line.strip().split("\t")
                if len(fields) < 4:
                    print(f"Error: Line '{line.strip()}' does not have the expected format.")
                    continue
                record = Record(fields[1], fields[2], fields[3])
                records.append(record)
        return records
    
    def write_record(self, record_count, record):
        with open(self.file_path, "a") as writeRecord:
            writeRecord.write(f"{record_count}\t\t\t{record.name}\t\t\t\t{record.age}\t\t\t\t{record.interests}\n")

class RecordManager:
    def __init__(self):
        file_path = os.path.join(r"c:\Users\training.user\Downloads\record.txt")
        self.record_file = RecordFile(file_path)
        self.records = self.record_file.read_records()
        self.record_count = len(self.records)
    
    def add_record(self):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        interests = input("Enter your interest: ")
        record = Record(name, age, interests)
        self.record_count += 1
        self.records.append(record)
        self.record_file.write_record(self.record_count, record)
    
    def view_records(self):
        if len(self.records) == 0:
            print("There are no records")
            print()
        else:
            with open(self.record_file.file_path, "r") as readRecords:
                print(readRecords.read())
    def clear_records(self):
        self.records = []
        with open(self.record_file.file_path, "w") as f:
            f.truncate(0)
            f.write("#\t\t\tName\t\t\t\tAge\t\t\t\tInterests\t\t\t\n")
    def delete_record(self):
        try:
            record_id = int(input("Enter Record #: ")) - 1
            if not (0 <= record_id < len(self.records)):
                raise ValueError("Invalid record number.")
            del self.records[record_id]
            self.record_count -= 1
            self.record_file.create_file()
            for i, record in enumerate(self.records):
                self.record_file.write_record(i+1, record)
            print("Record deleted successfully.")
        except ValueError as e:
            print(e)

    def find_records(self):
        name = input("Enter name to search for: ")
        with open(self.record_file.file_path, "r") as f:
            for line in f:
                if name in line:
                    print(line)
manager = RecordManager()

while True:            #print inside loop- displayed after completing any option
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
