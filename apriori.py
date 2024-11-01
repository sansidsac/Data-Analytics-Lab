import csv

def read_file(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)