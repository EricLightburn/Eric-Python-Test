import os
import sys
class Color:
    '''Defines colour codes for use in terminal'''
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
class Record:
    '''Represents a single record with name, age, and interests'''
    def __init__(self, name, age, interests):
        self.name = name
        self.age = age
        self.interests = interests
class RecordFile:
    '''Manages reading and writing records to the file'''
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            self.create_file()
    def create_file(self):
        '''Creates a new file and writes the heading'''
        with open(self.file_path, "w+") as create:
            create.write(f"{Color.BLUE}#\t\t\tName\t\t\t\t\tAge\t\t\t\tInterests{Color.RESET}\n")
    def read_records(self):
        '''Reads records from the file and returns them as a list of Record objects'''
        records = []
        with open(self.file_path, "r") as records_file:
            for line in records_file.readlines()[1:]:
                fields = line.strip().split("\t")
                if len(fields) < 4:
                    #print(f"{Color.RED}Error: Line '{line.strip()}' does not have the expected format.{Color.RESET}")
                    continue
                record = Record(fields[1], fields[2], fields[3])
                records.append(record)
        return records
    def write_record(self, record_count, record):
        '''Writes a single record to the file'''
        with open(self.file_path, "a") as writeRecord:
            writeRecord.write(f"{record_count}\t\t\t{record.name}\t\t\t\t{record.age}\t\t\t\t{record.interests}\n")
class RecordManager:
    '''Provides an interface for adding, viewing, deleting, clearing and finding records'''
    def __init__(self):
        file_path = os.path.join("record.txt")
        self.record_file = RecordFile(file_path)
        self.records = self.record_file.read_records()
        self.record_count = len(self.records)
    def add_record(self):
        '''Prompts the user for info and adds it to a new record'''
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        interests = input("Enter your interest: ")
        record = Record(name, age, interests)
        self.record_count += 1
        self.records.append(record)
        self.record_file.write_record(self.record_count, record)
    def view_records(self):
        '''Displays all records in terminal'''
        if len(self.records) == 0:
            print(f"{Color.YELLOW}There are no records{Color.RESET}")
            print()
        else:
            print(f"{Color.BLUE}#\t\t\tName\t\t\t\t\tAge\t\t\t\tInterests{Color.RESET}\n")
        for i, record in enumerate(self.records):
            print(f"{i+1}\t\t\t{record.name}\t\t\t\t\t{record.age}\t\t\t\t{record.interests}")
    def clear_records(self):
        '''Clears all records from the file and record list'''
        self.records = []
        with open(self.record_file.file_path, "w") as f:
            f.truncate(0)
            f.write(f"#\t\t\tName\t\t\t\tAge\t\t\t\tInterests\n")
    def delete_record(self):
        '''Prompts the user for a record number and deletes the one chosen'''
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
        '''Prompts the user for info and displays matching records'''
        search_type = input("Search by name or age? ")
        if search_type.lower() not in ["name", "age"]:
            print(f"Invalid search type: '{search_type}'. Please enter 'name' or 'age'.")
            return
        search_value = input(f"Enter {search_type} to search for: ")
        found = False
        for record in self.records:
            if search_type.lower() == "name" and search_value.lower() in record.name.lower():
                print(f"{record.name}\t\t\t{record.age}\t\t\t{record.interests}")
                found = True
            elif search_type.lower() == "age" and str(record.age) == search_value:
                print(f"{record.name} is {record.age} and likes {record.interests}")
                found = True
        if not found:
            print(f"No records found with the {search_type}: '{search_value}'")
    def get_option(self):
        '''Displays the main menu and prompts user to choose an option'''
        print(f"{Color.CYAN}=========================================================={Color.RESET}")
        print(f"{Color.CYAN} ~ ----------------- Record Manager --------------------- ~{Color.RESET}")
        print(f"{Color.CYAN}==========================================================={Color.RESET}")
        print("Available Options:")
        print(f"A) {Color.GREEN}Add Record{Color.RESET}\tB) {Color.YELLOW}View Record{Color.RESET}")
        print(f"C) {Color.RED}Delete Record{Color.RESET}\tD) {Color.MAGENTA}Clear Records{Color.RESET}")
        print(f"E) {Color.WHITE}Exit Manager{Color.RESET}\tF) {Color.BLUE}Find Records{Color.RESET}")
        option = input("Select an option: ").upper()
        return option
if __name__ == "__main__":
    manager = RecordManager()
    while True:            
        option = manager.get_option()
        match option:
            case "A":
                manager.add_record()
            case "B":
                manager.view_records()
            case "C":
                manager.delete_record()
            case "D":
                manager.clear_records()
            case "E":
                sys.exit(0)
            case "F":
                manager.find_records()
            case _:
                print("Invalid selection. Please try again.")

