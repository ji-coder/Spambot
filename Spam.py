import pyautogui
import time

def DisplayMenu():
    print("""
[1]Create Spam
[2]Run Script
[3]Exit""")

    choose = int(input('>'))

    if choose == 1:
        spam_name = input('Create Name of Spam text File: ')
        f = open(spam_name,'a')
        spam_words = input('Input Spam words : ')
        f.write(spam_words)
        f.close()
        DisplayMenu()
    elif choose == 2:
        i = 0
        spam_find = input('Enter your Create Name of Spam Text file: ')
        f = open(spam_find, 'r')
        count = int(input('How many Spam do you want? '))
        #Spam Message
        for word in f:
            time.sleep(3)
            while i < count:
                pyautogui.typewrite(word)
                pyautogui.press('enter')
                time.sleep(0.2)
                i += 1
    else:
        pass


DisplayMenu()
