import os
import sys

class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
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
            create.write(f"{Color.BLUE}#\t\t\tName\t\t\t\t\tAge\t\t\t\tInterests{Color.RESET}\n")
    def read_records(self):
        records = []
        with open(self.file_path, "r") as records_file:
            for line in records_file.readlines()[1:]:
                fields = line.strip().split("\t")
                if len(fields) < 4:
                    print(f"{Color.RED}Error: Line '{line.strip()}' does not have the expected format.{Color.RESET}")
                    continue
                record = Record(fields[1], fields[2], fields[3])
                records.append(record)
        return records
    
    def write_record(self, record_count, record):
        with open(self.file_path, "a") as writeRecord:
            writeRecord.write(f"{record_count}\t\t\t{record.name}\t\t\t\t{record.age}\t\t\t\t{record.interests}\n")

class RecordManager:
    def __init__(self):
        file_path = os.path.join("record.txt")
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
            print(f"{Color.YELLOW}There are no records{Color.RESET}")
            print()
        else:
            with open(self.record_file.file_path, "r") as readRecords:
                print(readRecords.read())
    def clear_records(self):
        self.records = []
        with open(self.record_file.file_path, "w") as f:
            f.truncate(0)
            f.write(f"#\t\t\tName\t\t\t\tAge\t\t\t\tInterests\n")
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
            print(f"{Color.GREEN}Record deleted successfully.{Color.RESET}")
        except ValueError as e:
            print(f"{Color.RED}{e}{Color.RESET}")
    def find_records(self):
        name = input("Enter name to search for: ")
        with open(self.record_file.file_path, "r") as f:
            for line in f:
                if name in line:
                    print(line)
manager = RecordManager()

while True:            
    print(f"{Color.CYAN}=========================================================={Color.RESET}")
    print(f"{Color.CYAN} ~ ----------------- Record Manager --------------------- ~{Color.RESET}")
    print(f"{Color.CYAN}==========================================================={Color.RESET}")
    print("Available Options:")
    print(f"A) {Color.GREEN}Add Record{Color.RESET}\tB) {Color.YELLOW}View Record{Color.RESET}")
    print(f"C) {Color.RED}Delete Record{Color.RESET}\tD) {Color.MAGENTA}Clear Records{Color.RESET}")
    print(f"E) {Color.WHITE}Exit Manager{Color.RESET}\tF) {Color.BLUE}Find Records{Color.RESET} \n")

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
