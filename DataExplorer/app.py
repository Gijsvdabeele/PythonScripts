# pyinstaller --onefile --distpath <dir> app_json.py
import json
import time
import os
from datetime import datetime
files_dir = "files/"
files = []
output_file = "output.txt"

for file in os.listdir(files_dir):
    files.append(file)
print("Please choose option by entering the corresponding number:\n"
      "1. Count occurrences of term\n"
      "2. List occurrences of term\n"
      "3. List comments from username\n"
      "4. Count total number of lines")
action = input()

if action == "1":
    # Defining vars for action
    print("Please enter search term")
    inp = input()
    count = 0
    start = time.time()

    # Going through all files in specified directory
    for file in os.listdir(files_dir):
        filename = str(file)
        print("Reading file " + str(files.index(filename)+1) + "/" + str(len(files)))

        # Open the file
        with open(files_dir+filename) as data:
            # Read each fow
            for row in data:
                data = json.loads(row)
                try:
                    if inp in data["body"]:
                        count += 1
                except UnicodeDecodeError:
                    print("Bad row:"+row)
    print("Total count is " + str(count))
    end = time.time()
    print("Done in " + str(round(end - start)) + " seconds.")
    input()

if action == "2":
    # Defining vars for action
    print("Please enter search term")
    inp = input()
    # Check if should output to file
    print("1. Print results to console\n2. Print to file")
    out_format = input()
    if out_format == "2":
        ttime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ttime = ttime.replace(":", "-").replace(" ", "_")
        output_file = open(str(ttime)+".txt", "a+")
    start = time.time()

    # Going through all files in specified directory
    for file in os.listdir(files_dir):
        filename = str(file)
        print("Reading file " + str(files.index(filename) + 1) + "/" + str(len(files)))

        # Open the file
        with open(files_dir+filename) as data:
            # Read each fow
            for row in data:
                data = json.loads(row)
                try:
                    if inp in data["body"]:
                        if out_format == "2":
                            try:
                                output_file.write(data["body"]+"\n")
                                output_file.write("-"+data["author"]+"\n")
                                output_file.write("----------------------\n")
                            except UnicodeEncodeError:
                                continue
                        else:
                            print(data["body"])
                            print("-"+data["author"] + "\n")
                            print("----------------------")
                except UnicodeDecodeError:
                    print("Bad row:"+row)
    end = time.time()
    print("Done in " + str(round(end - start)) + " seconds.")
    input()

if action == "3":
    # Defining vars for action
    print("Please enter username")
    inp = input()
    # Check if should output to file
    print("1. Print results to console\n2. Print to file")
    out_format = input()
    if out_format == "2":
        out_format = True
        ttime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ttime = ttime.replace(":", "-").replace(" ", "_")
        output_file = open(str(ttime) + ".txt", "a+")
    start = time.time()

    # Going through all files in specified directory
    for file in os.listdir(files_dir):
        filename = str(file)
        print("Reading file " + str(files.index(filename) + 1) + "/" + str(len(files)))

        # Open the file
        with open(files_dir+filename) as data:
            # Read each fow
            for row in data:
                data = json.loads(row)
                try:
                    if inp == data["author"]:
                        if out_format == "2":
                            try:
                                output_file.write(data["body"] + "\n")
                                output_file.write("----------------------\n")
                            except UnicodeEncodeError:
                                continue
                        else:
                            print(data["body"])
                            print("----------------------")
                except UnicodeDecodeError:
                    print("Bad row:"+row)
    end = time.time()
    print("Done in " + str(round(end - start)) + " seconds.")
    input()

if action == "4":
    # Defining vars for action
    count = 0
    start = time.time()

    # Going through all files in specified directory
    for file in os.listdir(files_dir):
        filename = str(file)
        print("Reading file " + str(files.index(filename)+1) + "/" + str(len(files)))

        # Open the file
        with open(files_dir+filename) as data:
            # Read each fow
            for row in data:
                count += 1
        print("Current number of lines is "+str(count))
    print("Total number of lines is " + str(count))
    end = time.time()
    print("Done in " + str(round(end - start)) + " seconds.")
    input()
