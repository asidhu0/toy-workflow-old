# import os

# def detemineDatasetsToRun():
#     print("In detemine datasets to run try 21")
#     for root, dirs, files in os.walk('.'):
#         print(f"Root: {root}")
#         for dir in dirs:
#             print(f"Directory: {os.path.join(root, dir)}")
#         for file in files:
#             print(f"File: {os.path.join(root, file)}")
#     file_path = '/mnt/vol/datasets_to_run.txt'
#     with open(file_path, 'r') as file_list:
#         file_ids = [line.strip() for line in file_list]

#     print(f"Need to process these datasets: {file_ids}")

# detemineDatasetsToRun()

# print("Finished step 1")

import os
import json
import sys

def detemineDatasetsToRun():
    for root, dirs, files in os.walk('.'):
        print(f"Root: {root}")
        for dir in dirs:
            print(f"Directory: {os.path.join(root, dir)}")
        for file in files:
            print(f"File: {os.path.join(root, file)}")
    file_path = '/mnt/vol/datasets_to_run.txt'
    file_path = './datasets_to_run.txt'
    with open(file_path, 'r') as file_list:
        json.dump([line.strip() for line in file_list], sys.stdout)

detemineDatasetsToRun()

# print("Finished step 1")