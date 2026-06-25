# Python file detection

# import os

#  file_path = "Get_Better/test.txt" # Relative 
# file_path = "C:/Users/Jacky Phuong/Desktop/skola.txt" # Absolute

# if os.path.exists(file_path):
#     print(f"The location {file_path} exists")

#     if os.path.isfile(file_path):
#         print("That is a file")
#     elif os.path.isdir(file_path):
#         print("That is a directory")

# else:
#     print(f"That location doesn't exist")

#-------------------------------------------

# Python writing files (.txt, .json, .csv)

# txt_data = "I like pizza!"
# employees = ["BOB", "ROB", "SOB", "TOB"]


# import json
# import csv

# employee = {
#     "name": "ROB",
#     "age": 20,
#     "job": "cook"
# }

# employees = [["Name", "Age", "Job"], 
#             ["BOB", 20, "Cook"], 
#             ["ROB", 30, "Painter"], 
#             ["SOB", 25, "Sceintist"]]


# file_path = "output.csv"

# try:
#     with open(file=file_path, mode="w", newline="") as file:
#         wrtier = csv.writer(file)
#         for row in employees:
#             wrtier.writerow(row)
#         print(f"csv file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")

#-------------------------------------------

# Python reading files (.txt, .json, .csv)

import json
import csv

file_path = "output.csv"

try:
    with open(file_path, "r") as file:
        # content = file.read()
        # content = json.load(file)
        content = csv.reader(file)
        for line in content:
            print(line)
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission tp read that file")