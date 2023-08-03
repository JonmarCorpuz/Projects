""" IMPORT MODULES """
from CLASSES import *
from FUNCTIONS import *


""" FUNCTIONS """
def ASCIIart():
    print("""
.▄▄ ·  ▄▄▄· ▄▄▌  ▄▄▄▄▄ ▄· ▄▌     ▄▄▄· ▄▄▄· .▄▄ · .▄▄ · ▄▄▌ ▐ ▄▌      ▄▄▄  ·▄▄▄▄  .▄▄ · 
▐█ ▀. ▐█ ▀█ ██•  •██  ▐█▪██▌    ▐█ ▄█▐█ ▀█ ▐█ ▀. ▐█ ▀. ██· █▌▐█▪     ▀▄ █·██▪ ██ ▐█ ▀. 
▄▀▀▀█▄▄█▀▀█ ██▪   ▐█.▪▐█▌▐█▪     ██▀·▄█▀▀█ ▄▀▀▀█▄▄▀▀▀█▄██▪▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌▄▀▀▀█▄
▐█▄▪▐█▐█ ▪▐▌▐█▌▐▌ ▐█▌· ▐█▀·.    ▐█▪·•▐█ ▪▐▌▐█▄▪▐█▐█▄▪▐█▐█▌██▐█▌▐█▌.▐▌▐█•█▌██. ██ ▐█▄▪▐█
 ▀▀▀▀  ▀  ▀ .▀▀▀  ▀▀▀   ▀ •     .▀    ▀  ▀  ▀▀▀▀  ▀▀▀▀  ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀▀▀▀▀▀•  ▀▀▀▀
by Jonmar Corpuz
     """)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")

def CreateDatabase():

    try:
        PasswordDatabase = open("PasswordDatabase.csv", "x")

        file = open("PasswordDatabase.csv", "w+", newline = "")    
        with file:
            header = ["Username", "Plaintext Password", "Salt Value", "Salted Password Hash"]
            writer = csv.DictWriter(file, fieldnames = header)
            writer.writeheader()
        
    except:
        pass


""" CLASSES """
# DEFINE A CLASS TO CREATE A USER'S ACCOUNT
class CreateAccount():

    # CONSTRUCTOR
    def __init__(self):
        self.Username = "EMPTY"
        self.Password = "EMPTY"
        self.Salt = "EMPTY"
        self.PasswordHash = "EMPTY"

    def PromptAccountInfo(self):
        
        while True:
            UsernameCollision = False
            self.Username = input("Enter a username: ")

            """
            # CHECK IF THE USERNAME EXISTS
            for i in range(len(UserDatabase)):
                if UserDatabase[i][0] == self.Username:
                    UsernameExist = True
                else:
                    continue
            
            if UsernameExist == True:
                print("Username already exists\n")
                continue
            else:
                break
            """

            with open("PasswordDatabase.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    if self.Username.upper() in line:
                        UsernameCollision = True
                    else:
                        continue
                    
            if UsernameCollision == False:
                break
            else:
                print("ERROR: Username already exists!\n")
            
        self.Password = input("Enter a password: ")
        
        print(" ")

    # HASH THE USER'S PASSWORD BY PASSING IT THROUGH A HASHING ALGORITHM
    def HashFunction(self):
        PasswordHash = hashlib.sha256(self.Password.encode('utf-8')).hexdigest()
        return PasswordHash

    # APPEND A SALT VALUE TO THE USER'S PASSWORD THEN PASS IT THROUGH A HASHING ALGORITHM
    def HashFunctionPlusSalt(self):
        RandomSalt = os.urandom(32)
        self.Salt = RandomSalt.hex()
        PlaintextPassword = self.Password.encode()
        PasswordPlusSalt = PlaintextPassword + RandomSalt
        EncodedPasswordHash = hashlib.pbkdf2_hmac('sha256', PlaintextPassword, RandomSalt, 10000)
        self.PasswordHash = EncodedPasswordHash.hex()
        return self.PasswordHash

    def AddToDatabase(self):
        file = open("PasswordDatabase.csv", "a", newline = "")    
        with file:
            header = ["Username", "Plaintext Password", "Salt Value", "Salted Password Hash"]
            writer = csv.DictWriter(file, fieldnames = header)

            writer.writerow({"Username" : self.Username.upper(),
                             "Plaintext Password" : self.Password,
                             "Salt Value" : self.Salt,
                             "Salted Password Hash" : self.PasswordHash})


""" MAIN CODE """
print("WELCOME TO KNOW CYBERSECURITY'S CLIENT-SIDE PASSWORD SALTING ALGORITHM!\n")
    
# USER DATABASE
"""
global Users
Users = []
"""

ASCIIart()
CreateDatabase()

# CREATE A USER
while True:
    User = CreateAccount()
    User.PromptAccountInfo()
    User.HashFunction()
    User.HashFunctionPlusSalt()
    User.AddToDatabase()

    while True:
        Continue = input("Would you like to continue?\nO/N: ")
        if Continue.upper() == "O" or Continue.upper() == "N":
            break
        print('ERROR: Please enter either "O" or "N"\n')

    if Continue.upper() == "O":
        print(" ")
        continue
    else:
        print(" ")
        break

# EXIT 
print("You have successfully exited the program!")
