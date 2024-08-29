# import os
# import sys

# def doubleNumbers(read_data):
#     print("Iteration 16")
#     print(f"Input file: {read_data}")

#     with open(read_data, 'r') as file_list:
#         file_ids = [line.strip().rstrip('.txt') for line in file_list]

#     os.makedirs('/mnt/vol/multiplication', exist_ok=True)

#     for file_id in file_ids:
#         input_file_path = f'/mnt/vol/raw-data/{file_id}.txt'
#         output_path = f'/mnt/vol/multiplication/{file_id}.txt'

#         print(f"Processing file: {file_id}")
#         print(f"Reading data from: {input_file_path}")
#         with open(input_file_path, 'r') as input_file:
#             number = int(input_file.read())

#         doubled_number = number * 2

#         print(f"Doubled number is {doubled_number}")
#         print(f"Saving doubled number to: {output_path}")
#         with open(output_path, 'w') as output_file:
#             output_file.write(str(doubled_number))

#         print(f"Processed file '{file_id}.txt' from {input_file_path}. Doubled the number from {number} to {doubled_number}. Saved to {output_path} as {output_file}")
#         print()


# doubleNumbers(sys.argv[1])

# print("Finished step 2")



import os
import sys
import json

def doubleNumbers(read_data):
    try:
        input_data = json.loads(sys.argv[1])
        input_number = int(input_data)
        result = input_number * 2
        print(result)
    except ValueError:
        print(f"Error: '{sys.argv[1]}' is not a valid number")
        sys.exit(1)

doubleNumbers(sys.argv[1])

# print("Finished step 2")