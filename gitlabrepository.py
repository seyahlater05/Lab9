def encode(key):
    encoded_key = ''
    for i in key:
        if int(i) + 3 < 10:
            encoded_key += f'{int(i)+3}'
        else:
            encoded_key += f'{int(i)-7}'
    return encoded_key


if __name__ == '__main__':
    while 1:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        choice = input('Please enter an option: ')
        if choice == '1':
            key = input('Please enter your password to encode: ')
            encoded_key = encode(key)
