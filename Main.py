#make something like 2 into 00000002
from os import name


def convert_under_8_int(inp):
    if len(inp) < 8:
        inp = (8-len(str(inp)))*"0"+inp
    return inp

#checks if varabile is in the list of letters
def list_checker(lsit):
    for i in lsit:
        if i not in letters:
            return False
    return True


#list of uper & lower case letters
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letters = letters + [x.lower() for x in letters]
#returns false if the input is not a valid 10 digit number 
#if there is an valid it remoes the 
def strips(inp):
    if len(inp) == 10 and list_checker(inp[0]) and list_checker(inp[-1]): 
        imp = inp[1:-1]
        return imp
    return False
if name == "__main__":
    print(strips("B"+convert_under_8_int("2") + "a"))