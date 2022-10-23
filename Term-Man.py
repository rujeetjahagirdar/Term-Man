from random import choices

print("""\n\n
████████╗███████╗██████╗░███╗░░░███╗░░░░░░███╗░░░███╗░█████╗░███╗░░██╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║░░░░░░████╗░████║██╔══██╗████╗░██║
░░░██║░░░█████╗░░██████╔╝██╔████╔██║█████╗██╔████╔██║███████║██╔██╗██║
░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║╚════╝██║╚██╔╝██║██╔══██║██║╚████║
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║░░░░░░██║░╚═╝░██║██║░░██║██║░╚███║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝\n""")



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
                    name = input('Enter file name: ')
                    f = open(f"{name}.txt", "w+")
                    for password in lit:
                        f.write(password)
                    f.close()
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

