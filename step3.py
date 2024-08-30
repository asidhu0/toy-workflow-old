import os
import sys

def subtractOne(read_data):
    input_number = int(sys.argv[1])
    result = input_number - 1
    print(result)

    os.makedirs('/mnt/vol/subtraction', exist_ok=True)

    output_path = f'/mnt/vol/subtraction/{result}.txt'

    with open(output_path, 'w') as output_file:
        output_file.write(str(result))

subtractOne(sys.argv[1])