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