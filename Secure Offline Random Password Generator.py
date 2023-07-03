""" IMPORTED MODULES """
import random

""" FUNCTIONS """

# ASCII ART
def ASCIIart():
    print("""

░██████╗███████╗░█████╗░██╗░░░██╗██████╗░███████╗
██╔════╝██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔════╝
╚█████╗░█████╗░░██║░░╚═╝██║░░░██║██████╔╝█████╗░░
░╚═══██╗██╔══╝░░██║░░██╗██║░░░██║██╔══██╗██╔══╝░░
██████╔╝███████╗╚█████╔╝╚██████╔╝██║░░██║███████╗
╚═════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝

░█████╗░███████╗███████╗██╗░░░░░██╗███╗░░██╗███████╗
██╔══██╗██╔════╝██╔════╝██║░░░░░██║████╗░██║██╔════╝
██║░░██║█████╗░░█████╗░░██║░░░░░██║██╔██╗██║█████╗░░
██║░░██║██╔══╝░░██╔══╝░░██║░░░░░██║██║╚████║██╔══╝░░
╚█████╔╝██║░░░░░██║░░░░░███████╗██║██║░╚███║███████╗
░╚════╝░╚═╝░░░░░╚═╝░░░░░╚══════╝╚═╝╚═╝░░╚══╝╚══════╝

██████╗░░█████╗░███╗░░██╗██████╗░░█████╗░███╗░░░███╗  
██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗████╗░████║  
██████╔╝███████║██╔██╗██║██║░░██║██║░░██║██╔████╔██║  
██╔══██╗██╔══██║██║╚████║██║░░██║██║░░██║██║╚██╔╝██║  
██║░░██║██║░░██║██║░╚███║██████╔╝╚█████╔╝██║░╚═╝░██║  
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░╚═╝░░░░░╚═╝  

██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░

░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
by Jonmar Corpuz
    """)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")

# STARTING MENU 
def StartingMenu():
    
    print("This python program generates a secure password that's 20 characters long and contains at least two uppercase letters, two numbers and two special characters.\n")
    
    while True:
        RandomizeOption = input("Would you like to generate a password?\n[y] YES\n[n] NO\nPlease type in your answer: ")
        if RandomizeOption.lower() == "y" or RandomizeOption.lower() == "n":
            print(" ")
            break
        print(" ")
        print('----- ERROR #1: Please type in either "y" or "n" -----\n')

    if RandomizeOption.lower() == "y":
        GeneratePassword()
    else:
        while True:
            ExitConfirmation = input("Would you like to exit the program?\n[y] YES\n[n] NO\nPlease type in your answer here: ")
            if ExitConfirmation.lower() == "y" or ExitConfirmation.lower() == "n":
                print(" ")
                break
            print(" ")
            print('----- ERROR #2: Please type in either "y" or "n" -----\n')

        if ExitConfirmation.lower() == "y":
            exit("----- You have successfully exited the program -----")
        else:
            StartingMenu()


# SET PASSWORD PREFERENCES
def GeneratePassword():

    Length = 20

    while True:

        # GENERATE THE NUMBER OF LOWERCASE LETTERS THAT'LL BE IN THE RANDOMLY GENERATED PASSWORD
        Random_LowercaseLetterQuantity = random.randint(0, Length)
                

        # GENERATE THE NUMBER OF UPPERCASE LETTERS THAT'LL BE IN THE RANDOMLY GENERATED PASSWORD
        NewLength = Length - Random_LowercaseLetterQuantity
        Random_UppercaseLetterQuantity = random.randint(0, NewLength)

        # GENERATE THE NUMBER OF DIGITS THAT'LL BE IN THE RANDOMLY GENERATED PASSWORD
        NewLength = NewLength - Random_UppercaseLetterQuantity
        Random_DigitQuantity = random.randint(0, NewLength)

        # GENERATE THE NUMBER OF SPECIAL CASE CHARACTERS THAT'LL BE IN THE RANDOMLY GENERATED PASSWORD
        Random_SpecialCharacterQuantity = NewLength - Random_DigitQuantity
        
        if Random_SpecialCharacterQuantity > 1 and Random_DigitQuantity > 1 and Random_UppercaseLetterQuantity > 1 and Random_LowercaseLetterQuantity > 1:
            break

    # GENERATE RANDOM PASSWORD
    Password = ""

    for i in range(Random_LowercaseLetterQuantity):
        RandomIndex = random.randint(0, len(LOWERCASE_LETTERS)-1)
        Password += LOWERCASE_LETTERS[RandomIndex]

    for i in range(Random_UppercaseLetterQuantity):
        RandomIndex = random.randint(0, len(UPPERCASE_LETTERS)-1)
        Password += UPPERCASE_LETTERS[RandomIndex]

    for i in range(Random_DigitQuantity):
        RandomIndex = random.randint(0, len(DIGITS)-1)
        Password += DIGITS[RandomIndex]

    for i in range(Random_SpecialCharacterQuantity):
        RandomIndex = random.randint(0, len(SPECIAL_CHARACTERS)-1)
        Password += SPECIAL_CHARACTERS[RandomIndex]

    # SHUFFLE THE GENERATED PASSWORD'S CHARACTERS AROUND 
    PasswordCharactersList = []
    ###IndexList = []
    for i in range(len(Password)):
        PasswordCharactersList.append(Password[i])
        ###IndexList.append(i)

    ShuffledIndexes = []
    for i in range(len(Password)):
        while True:
            RandomIndex = random.randint(0, len(Password)-1)
            if RandomIndex not in ShuffledIndexes:
                ShuffledIndexes.append(RandomIndex)
                break

    ShuffledPassword = ""
    for i in range(len(ShuffledIndexes)):
        ShuffledPassword += Password[ShuffledIndexes[i]]

    ###print(PasswordCharactersList)
    ###print(ShuffledIndexes)
    ###print(ShuffledPassword)

    print(f"Your randomly generated password is: {ShuffledPassword}\n")

    ###ExportPassword(Password)
    AskGenerateAgain()

      
# ASK IF THE USER WANTS TO GENERATE A NEW RANDOM PASSWORD
def AskGenerateAgain():
    while True:
        Continue = input("Would you like to generate another password?\n[y] YES\n[n] NO\nPlease type in your answer: ")
        if Continue.lower() == "y" or Continue.lower() == "n":
            print(" ")
            break
        print(" ")
        print('----- ERROR #3: Please type in either "y" or "n" -----\n')

    if Continue.lower() == "y":
        ###StartingMenu()
        GeneratePassword()
    else:
        while True:
            ExitConfirmation = input("Are you sure you want to exit the program?\n[y] YES\n[n] NO\nPlease type in your answer here: ")
            if ExitConfirmation.lower() == "y" or ExitConfirmation.lower() == "n":
                print(" ")
                break
            print(" ")
            print('----- ERROR #4: Please type in either "y" or "n" -----\n')

        if ExitConfirmation.lower() == "y":
            exit("----- You have successfully exited the program -----")
        else:
            AskGenerateAgain()
        

""" MAIN CODE """

LOWERCASE_LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPERCASE_LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL_CHARACTERS = ["!", "?", ".", "_", "-", "$", "#", "&"]

ASCIIart()
StartingMenu()
