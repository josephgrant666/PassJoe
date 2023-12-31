#!/usr/bin/python3

import random, pyperclip, sys, string, time
from ctypes import windll

def PassJoeStnrd():
    print('1. How many characters do you want your password to contain? The length should be 7 to 20 characters.')
    while True:
        Length = input()
        if int(Length) >= 7 and int(Length) <= 20:
            break
        elif int(Length) < 7 or int(Length) > 20:
            print('Write a number in between 7 and 20.')
            continue

    print('2. Do you want your password to contain capital letters?')
    while True:
        Caps = input()
        if Caps == 'Yes':
            break
        elif Caps == 'yes':
            break
        elif Caps == 'No':
            break
        elif Caps == 'no':
            break
        else:
            print('Enter a yes or no answer.')
            continue

    print('3. Do you want your password to contain numbers?')
    while True:
        Numbers = input()
        if Numbers == 'Yes':
            break
        elif Numbers == 'yes':
            break
        elif Numbers == 'No':
            break
        elif Numbers == 'no':
            break
        else:
            print('Enter a yes or no answer.')
            continue

    print('4. Do you want your password to contain special characters?')
    while True:
        SCs = input()
        if SCs == 'Yes':
            break
        elif SCs == 'yes':
            break
        elif SCs == 'No':
            break
        elif SCs == 'no':
            break
        else:
            print('Enter a yes or no answer.')
            continue
    # PasswordCombo1
    if Caps and Numbers and SCs == str.lower('no'):
        def PasswordCombo1():
            while True:
                PasswordCombo1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(int(Length)))
                global PassGen
                PassGen = PasswordCombo1
                break
        PasswordCombo1()
    #PasswordCombo2
    if Caps == str.lower('yes') and Numbers and SCs == str.lower('no'):
        def PasswordCombo2():
            while True:
                PasswordCombo2 = ''.join(random.choice(string.ascii_letters) for _ in range(int(Length)))
                global PassGen
                PassGen = PasswordCombo2
                break
        PasswordCombo2()
    #PasswordCombo3
    if Caps and Numbers == str.lower('yes') and SCs == str.lower('yes'):
        def PasswordCombo3():
            while True:
                PasswordCombo3 = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(int(Length)))
                global PassGen
                PassGen = PasswordCombo3
                break
        PasswordCombo3()
    #PasswordCombo4
    if Numbers == str.lower('yes') and Caps and SCs == str.lower('no'):
        def PasswordCombo4():
            while True:
                PasswordCombo4 = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(int(Length)))
                global PassGen
                PassGen = PasswordCombo4
                break
        PasswordCombo4()
    #PasswordCombo5
    if SCs == str.lower('yes') and Caps and Numbers == str.lower('no'):
        def PasswordCombo5():
            while True:
                PasswordCombo5 = ''.join(random.choice(string.ascii_lowercase + string.punctuation) for _ in range(int(Length)))
                global PassGen
                PassGen = PasswordCombo5
                break
        PasswordCombo5()
    #PasswordCombo6
    if Numbers == str.lower('no') and Caps and SCs == str.lower('yes'):
        def PasswordCombo6():
            while True:
                PasswordCombo6 = ''.join(random.choice(string.ascii_letters + string.punctuation) for _ in range(int(Length)))
                global PassGen
                PassGen = PasswordCombo6
                break
        PasswordCombo6()
    #PasswordCombo7
    if Caps == str.lower('no') and Numbers and SCs == str.lower('yes'):
        def PasswordCombo7():
            while True:
                PasswordCombo7 = ''.join(random.choice(string.ascii_lowercase + string.digits + string.punctuation) for _ in range(int(Length)))
                global PassGen
                PassGen = PasswordCombo7
                break
        PasswordCombo7()
    #PasswordCombo8
    if Numbers and Caps and SCs == str.lower('yes'):
        def PasswordCombo8():
            while True:
                PasswordCombo8 = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(int(Length)))
                global PassGen
                PassGen = PasswordCombo8
                break
        PasswordCombo8()

def PassJoeQuick():
    Length = int(20)
    PasswordCombo8 = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(int(Length)))
    global PassGen
    PassGen = PasswordCombo8

def save():
            print('Choose a roughly 3 letter name to be assigned to this password:')
            PassName = input()
            PW = open(r'C:\Users\User\Desktop\PW.txt', 'a')
            PW.write("\n" + PassName + " " + PassGen)
            pyperclip.copy(PassGen)
            print('''Your password has been saved to the PW file \nAnd your password has 
                  been copied onto the clip board so that you can paste it to where you need to. 
                  This clipboard copy will be deleted after 30 seconds.''')
            time.sleep(30)
            if windll.user32.OpenClipboard(None): # Clears clipboard history for security
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            time.sleep(5)
            sys.exit()

while True:
    print('''Hello! This program generates a password of your choice. 
Here are some questions about what your password should look like:''')

    print('''Would you like to use PassJoeQuick? This creates a password that is 20 characters long with caps, numbers 
          and special characters''')
    while True:
            PassJoeQuickQ = input()
            if PassJoeQuickQ == 'Yes':
                PassJoeQuick()
                break
            elif PassJoeQuickQ == 'yes':
                PassJoeQuick()
                break
            elif PassJoeQuickQ == 'No':
                PassJoeStnrd()
                break
            elif PassJoeQuickQ == 'no':
                PassJoeStnrd()
                break
            else:
                print('Enter a yes or no answer.')
                continue

    print('Are you happy with this password? : ' + PassGen)
    while True:
        HappyAnswer = input()
        if HappyAnswer == 'Yes':
            save()
        elif HappyAnswer == 'yes':
            save()
        elif HappyAnswer == 'No':
            break
        elif HappyAnswer == 'no':
            break
        else:
            print('Enter a yes or no answer.')
            continue



