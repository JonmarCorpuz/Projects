""" IMPORT MODULES """
import random
import csv


""" FUNCTIONS """
def ASCIIart():
    print("""
                 d8b                          d8,                            d8,                  
   d8P           ?88                         `8P                      d8P   `8P                   
d888888P          88b                                              d888888P                       
  ?88'   d8888b   888  d88' d8888b  88bd88b   88bd88888P  d888b8b    ?88'    88b d8888b   88bd88b 
  88P   d8P' ?88  888bd8P' d8b_,dP  88P' ?8b  88P   d8P' d8P' ?88    88P     88Pd8P' ?88  88P' ?8b
  88b   88b  d88 d88888b   88b     d88   88P d88  d8P'   88b  ,88b   88b    d88 88b  d88 d88   88P
  `?8b  `?8888P'd88' `?88b,`?888P'd88'   88bd88' d88888P'`?88P'`88b  `?8b  d88' `?8888P'd88'   88b

by Jonmar Corpuz
    """)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")

# STARTING MENU
def Menu():

    while True:

        Choice = input("What would you like to do?\n 1 - Generate a token for a piece of data\n 2 - Fetch the data that's mapped to a token\n 3 - View token database\n 4 - Exit the program\nEnter your choice: ")

        if Choice == "1" or Choice == "2" or Choice == "3" or Choice == "4":
            print("")
            return Choice
            break
        else:
            print("Error: Please enter a valid option")
            print("")
    
# CREATE CLIENT-SIDE TOKEN DATABASE FILE
def CreateTokenDatabase():

    try:
        TokenDatabase = open("TokenDatabase.csv", "x")

        file = open("TokenDatabase.csv", "w+", newline = "")    
        with file:
            header = ["Data", "Token"]
            writer = csv.DictWriter(file, fieldnames = header)
            writer.writeheader()
        
    except:
        # print("The file already exists!")
        # print("")
        pass

# COLLECT THE USER'S INPUT 
def CollectInput():

    Data = input("Enter something: ")
    return Data

# GENERATE TOKEN 
def GenerateToken():

    CharactersList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    CharctersListLength = len(CharactersList)
    TokenLength = 20
    TokenCollision = False

    while True:
        Token = ""

        for i in range(TokenLength):
            Character = random.randint(0, CharctersListLength - 1)
            Token += CharactersList[Character]

        with open("TokenDatabase.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if Token in line:
                    TokenCollision = True
                else:
                    continue
                    
        if TokenCollision == False:
            return Token
            break
        else:
            continue
            

# STORE AND MAP THE TOKEN IN THE CLIENT-SIDE DATABASE 
def StoreToken(Data, Token):

    DataMap = [Data, Token]

    file = open("TokenDatabase.csv", "a", newline = "")    
    with file:
        header = ["Data", "Token"]
        writer = csv.DictWriter(file, fieldnames = header)
        
        writer.writerow({"Data" : Data,
                         "Token" : Token})

# FETCH THE DATA FROM THE DATABASE
def FetchTokenData():

    TokenOutput = ""
    Error = "ERROR: Data not found"
    Token = input("Enter a token: ")
    
    with open("TokenDatabase.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            # print(line)
            
            if Token in line[1]:
                print("")
                TokenOutput = "String found: " + line[0]
                return TokenOutput
            
            else:
                continue
            
        print("")
        return Error

# ASK THE USER IF THEY WANT TRY AGAIN
def TryAgain():

    while True:
        while True:
            Choice = input("Would you like to try again?\n Y - Yes\n N - No\nEnter your choice: ")

            if Choice.upper() == "Y" or Choice.upper() == "N":
                return Choice
                break
            else:
                print("ERROR: Please enter a valid option")
                print("")
            break

# ASK THE USER IF THEY WANT TO FETCH MORE DATA
def FetchAgain():
    
    while True:
        while True:
            Choice = input("Would you like to fetch another piece of data?\n Y - Yes\n N - No\nEnter your choice: ")

            if Choice.upper() == "Y" or Choice.upper() == "N":
                return Choice
                break
            else:
                print("ERROR: Please enter a valid option")
                print("")
            break


""" MAIN CODE """
ASCIIart()

while True:

    Choice = Menu()

    if Choice == "1":
        # COLLECT USER INPUT
        Data = CollectInput()

        # CREATE TOKEN DATABASE FILE 
        CreateTokenDatabase()

        # GENERATE TOKEN
        Token = GenerateToken()

        # STORE AND MAP THE TOKEN IN THE DATABASE 
        StoreToken(Data, Token)

    elif Choice == "2":
        # FETCH DATA 
        while True:
            ReturnedData = FetchTokenData()
            print(ReturnedData)
            print("")

            if ReturnedData == "ERROR: Token not found":
                Choice = TryAgain()
                if Choice.upper() == "Y":
                    continue
                else:
                    print("")
                    break
            else:
                Choice = FetchAgain()
                if Choice.upper() == "Y":
                    continue
                else:
                    print("")
                    break

    elif Choice == "3":
        SetPassword = "Admin"
        Attempts = 3
        LoginStatus = False

        while Attempts > 0:
            CreateTokenDatabase()

            Data = False
            Password = input(f"Please enter the set password to view this file ({Attempts} Left): ")
            print("")

            if Password == SetPassword:
                with open("TokenDatabase.csv", "r") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    print("DATA, TOKEN")
                    next(csv_reader)
                    
                    for line in csv_reader:
                        print(line)
                        Data = True

                    if Data == False:
                        print("No data")
                    else:
                        pass
                        
                    print("")
                    LoginStatus = True
                    break

            else:
                print("LOGIN FAILED: Wrong password")
                print("")
                Attempts -= 1

        if LoginStatus == False:
            print("LOGIN FAILED: No more attempts")
            print("")
        else:
            continue
        
    else:
        exit("You have successfully exited the program!")
