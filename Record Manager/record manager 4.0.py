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