# pswd creation
import random
import pathlib

pswd = str()

def pswd_code():
   special_charachter = ["/", "*", "-", "+", ".", ",", "!", "\"", "'", "\#", "$", "%", "^", "&", "-", "_"]

   numbers = str(random.randint(0, 9))

   letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

   letters_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

   global pswd
   pswd = str()

   for x in range (0,14):

      charachter_choice = random.choice([special_charachter, numbers, letters, letters_upper])
      random_charachter = random.choice(charachter_choice)
      pswd += random_charachter

path = pathlib.Path(__file__).parent.absolute()

checking = open(f"{path}/rockyou.txt", "r", encoding= "cp437").read()
used_pswd = open (f"{path}/used_pswd.txt", "r", encoding="cp437").read()

if pswd in checking:
   pswd_code()
elif pswd in used_pswd:
   pswd_code() 

used_pswd = open(f"{path}/used_pswd.txt", "a")
used_pswd.write(pswd+"\n\n")
used_pswd.close()

print("password = '"+pswd+"'")