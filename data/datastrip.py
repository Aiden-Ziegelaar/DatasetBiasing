import csv
from datetime import datetime

with open("BankChurners.csv") as csvFile:
    with open("BankChurners_sanitized.csv", "w", newline='') as outFile:
        reader = csv.reader(csvFile)
        writer = csv.writer(outFile)
        for row in reader:
            stripped_row = row[2:-2] + [row[1]]
            writer.writerow(stripped_row)
