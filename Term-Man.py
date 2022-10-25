from random import choices
from cryptography.fernet import Fernet
import os

print("""\n\n
████████╗███████╗██████╗░███╗░░░███╗░░░░░░███╗░░░███╗░█████╗░███╗░░██╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║░░░░░░████╗░████║██╔══██╗████╗░██║
░░░██║░░░█████╗░░██████╔╝██╔████╔██║█████╗██╔████╔██║███████║██╔██╗██║
░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║╚════╝██║╚██╔╝██║██╔══██║██║╚████║
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║░░░░░░██║░╚═╝░██║██║░░██║██║░╚███║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝\n""")



p = input('press enter to continue: ')
if p == 'decrypt':
    try:
        txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
        if len(txt_files) == 0:
            raise ValueError('There should be a txt file in the current directory')

        key = ''
        with open('Decrypter.key', 'rb') as file:
            key=file.read()

        fernet = Fernet(key)

        with open(f'{txt_files[0]}', 'rb') as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        with open(f'{txt_files[0]}', 'wb') as dec_file:
            dec_file.write(decrypted)



    except:
        print('--\n-----Invalid-Input\n--')
elif p == 'quit':
    print('quitting...')
    quit()

def quit_menu():
    q = input('Would you like to quit--(Y-N): ').upper()
    try:
        if q == 'Y':
            print('quitting...')
        elif q == 'N':
            return generate()
        else:
            print('\n\n--Invalid-Input---\n\n')
            return quit_menu()
    except:
        print('\n\n---ERROR')
        return quit_menu()


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+1234567890-=/.,<>?`~"


def generate():
    lit = []

    def save_command():
        s = input('Would you like to save these passwords---(Y_N): ').upper()

        try:
            if s == 'Y':
                try:
                    encryption_choice = input('\nWould you like to encrypt the file--(Y_N): ').upper()
                    if encryption_choice == 'Y':
                        check = input('Enter G to generate a key. If you already did this, skip ahead: ')
                        if check == 'G':
                            name = input('Enter file name: ')
                            f = open(f"{name}.txt", "w+")
                            for password in lit:
                                f.write(password)
                            f.close()
                            # Generating decryption key file
                            key_file = Fernet.generate_key()
                            with open('Decrypter.key', 'wb') as file:
                                file.write(key_file)

                            # Reading key from file
                            key = ''
                            with open('Decrypter.key', 'rb') as file:
                                key = file.read()

                            # Reading password file
                            data = ""
                            with open(f'{name}.txt', 'rb') as file:
                                data = file.read()

                            # Encrypting the file
                            f = Fernet(key)
                            encrypted_password = f.encrypt(data)

                            # saving file
                            with open(f"{name}.txt", 'wb') as file:
                                file.write(encrypted_password)

                            return "To decrypt files, type decrypt"
                        else:
                            pass
                    elif encryption_choice == 'N':
                        name = input('Enter file name: ')
                        f = open(f"{name}.txt", "w+")
                        for password in lit:
                            f.write(password)
                        f.close()
                    else:
                        print('\n--Invalid-Input--\n')
                        return save_command()
                except:
                    print('\n\n---ERROR')
                    return save_command()
            elif s == 'N':
                return quit_menu()
            else:
                print('\n\n--Invalid-Input--\n')
                return save_command()
        except:
            print('\n\n---ERROR')
            return save_command()

    try:
        Length = int(input("\n|Input the Length of the password you wish to create: "))
        Amount = int(input("\n|Input the amount of passwords you wish to create: "))
        print('\n\n')

    except:
        print("\n\nYou may only input digits, try again.\n\n")
        return generate()

    try:
        for c in range(Amount):
            pass_chars = choices(chars, k=Length)
            Password = "Password: " + "".join(pass_chars) + "\n"
            print(Password)
            lit.append(Password)
    except:
        print("\n\nERROR: Something went wrong???\n\n")
        return generate()

    print(save_command())


print(generate())
