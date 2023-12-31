'''Caesar Cipher

This program allows you to encrypt / decrypt ciphertexts using the Caesar cipher.
Plaintext is encrypted using shifts to the right.
Ciphertext is decrypted using either basic frequency analysis or brute force.
'''


class Cipher:
    '''Contains functions to encrypt / decrypt ciphertexts.'''

    def prompt(self):
        '''Displays information about program and asks user to pick mode.'''
        print('Caesar Cipher')
        print('---------------------------------------------------------------')
        print('1 - Encrypt plaintext -> ciphertext')
        print('2 - Decrypt ciphertext -> plaintext using frequency analysis')
        print('3 - Decrypt ciphertext -> plaintext using brute force\n')
        while True:
            try:
                mode = int(input('Pick a mode [1-3]: '))
                if mode < 1 or mode > 3:
                    raise ValueError
            except ValueError:
                print('[ERROR] INVALID INPUT!')
            else:
                break
        return mode

    def transcipher(self, mode, msg, key):
        '''Shifts each letter in the ciphertext n positions to the right.'''
        translation = ''
        if mode == 2 or mode == 3:
            key = -key
        for char in msg:
            if char.isalpha():
                num = ord(char)
                num += key
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
                translation += chr(num)
            else:
                translation += char
        return translation

    def get_key(self):
        'Prompts user for shift key for encryption.'
        while True:
            try:
                u_key = int(input('Enter shift key [1-26]: '))
                if u_key < 1 or u_key > 26:
                    raise ValueError
            except ValueError:
                print('[ERROR] INVALID INPUT!')
            else:
                break
        return u_key

    def find_frequency(self, msg):
        '''Finds the top four most frequently used letters in the ciphertext.'''
        char_freq = {}
        for char in msg:
            freq = char_freq.keys()
            if char.isalpha():
                if char in freq:
                    char_freq[char] += 1
                else:
                    char_freq[char] = 1
        char_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
        return char_freq[:4]

    def find_key(self, msg, top_char):
        '''Finds top four most likely cipher keys using 'E' as a reference.'''
        p_keys = []
        for char in top_char:
            num = ord(char[0]) - 65
            a = (num - 4) % 26
            b = (4 - num) % 26
            num = min(a, b)
            p_keys.append(num)
        return p_keys

    def cipher_run(self):
        '''Runs the Caesar cipher encryption / decryption.'''
        cipher_mode = self.prompt()
        if cipher_mode == 1:
            plaintext = str.upper(input('Enter plaintext: '))
            user_key = self.get_key()
            user_msg = self.transcipher(1, plaintext, user_key)
            print('\nEncipherment')
            print('-------------------------------------------')
            print(f'[{user_key}] {user_msg} \n')
        elif cipher_mode == 2:
            ciphertext = str.upper(input('Enter ciphertext: '))
            top_letters = self.find_frequency(ciphertext)
            possible_keys = self.find_key(ciphertext, top_letters)
            print('\nFrequency Analysis')
            print('-------------------------------------------')
            for letter in top_letters:
                print(f'{letter[0]} : {letter[1]}')
            print(f'\nTop Possible Shift Keys: {possible_keys}')
            print('\nTop Possible Translations')
            print('-------------------------------------------')
            for p_key in possible_keys:
                p_msg = self.transcipher(2, ciphertext, p_key)
                print(f'[{p_key}] {p_msg}')
        elif cipher_mode == 3:
            ciphertext = str.upper(input('Enter ciphertext: '))
            print('\nBrute Force')
            print('-------------------------------------------')
            for i in range(1, 27):
                p_msg = self.transcipher(3, ciphertext, i)
                print(f'[{i}] {p_msg}')


def main():
    c = Cipher()
    c.cipher_run()


if __name__ == '__main__':
    main()
