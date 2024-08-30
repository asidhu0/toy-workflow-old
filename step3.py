# import os
# import sys

# def subtractOne(read_data):
#     print("Iteration 6")
#     print(f"Input file: {read_data}")

#     with open(read_data, 'r') as file_list:
#         file_ids = [line.strip().rstrip('.txt') for line in file_list]

#     os.makedirs('/mnt/vol/subtraction', exist_ok=True)

#     for file_id in file_ids:
#         input_file_path = f'/mnt/vol/multiplication/{file_id}.txt'
#         output_path = f'/mnt/vol/subtraction/{file_id}.txt'

#         print(f"Processing file: {file_id}")
#         print(f"Reading data from: {input_file_path}")
#         with open(input_file_path, 'r') as input_file:
#             number = int(input_file.read())

#         subtracted = number - 1

#         print(f"Subtracted number is {subtracted}")
#         print(f"Saving subtracted number to: {output_path}")
#         with open(output_path, 'w') as output_file:
#             output_file.write(str(subtracted))

#         print(f"Processed file '{file_id}.txt' from {input_file_path}. Subtracted one from {number} to get {subtracted}. Saved to {output_path} as {output_file}")
#         print()

# subtractOne(sys.argv[1])

# print("Finished step 3")

import os
import sys

def subtractOne(read_data):
    input_number = int(sys.argv[1])
    result = input_number - 1
    print(result)

    os.makedirs('/mnt/vol/subtraction', exist_ok=True)

    output_path = f'/mnt/vol/subtraction/{sys.argv[1]}.txt'

    with open(output_path, 'w') as output_file:
        output_file.write(str(result))

subtractOne(sys.argv[1])