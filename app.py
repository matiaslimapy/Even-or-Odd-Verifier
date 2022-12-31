import os


def verifyEvenNumbers(num):
    parsednumber = int(num)
    if parsednumber % 2 == 0:
        return True
    else:
        return False


def initialMenu():
    os.system('cls')
    print("Welcome to even or odd numbers verifier!!!")
    receivedNumber = input("\n\n\nPlease insert one number to verify: ")
    if verifyEvenNumbers(receivedNumber):
        os.system('cls')
        print("Your number is even.")

    else:
        os.system('cls')
        print("Your number is odd.")


initialMenu()
