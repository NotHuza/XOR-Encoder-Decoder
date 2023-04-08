import itertools

def xor_cipher(data, key):
    key_len = len(key)
    return bytearray([datum ^ key[i % key_len] for i, datum in enumerate(data)])

def encode_file():
    key = input("Enter a key (string): ")
    input_file = "files/" + input("Enter the input file name: ")
    output_file = "files/" + input("Enter the output file name: ")
    with open(input_file, 'rb') as f:
        data = f.read()
    encoded_data = xor_cipher(data, key.encode())
    with open(output_file, 'wb') as f:
        f.write(encoded_data)
    print(f"Data encoded with key {key} and written to {output_file}")

def decode_file():
    key = input("Enter a key (string): ")
    input_file = "files/" + input("Enter the input file name: ")
    output_file = "files/" + input("Enter the output file name: ")
    with open(input_file, 'rb') as f:
        data = f.read()
    decoded_data = xor_cipher(data, key.encode())
    with open(output_file, 'wb') as f:
        f.write(decoded_data)
    print(f"Data decoded with key {key} and written to {output_file}")

def exit_program():
    print("Goodbye!")
    exit()

while True:
    mode = input("Enter 'encode', 'decode', or 'exit': ")
    if mode == 'encode':
        encode_file()
    elif mode == 'decode':
        decode_file()
    elif mode == 'exit':
        exit_program()
    else:
        print("Invalid mode. Please enter 'encode', 'decode', or 'exit'.")
