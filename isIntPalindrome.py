# This script receives an integer and determines if it is palindromic
# Returns a boolean value of True or False
#Usage: isIntPalindrome.py <integer>

import sys # Needed to access command line arguments

def isIntPalindrome(n):

    if(int(n) < 0):
        return False

    numLen = len(n) # Retrieve number length
    if(numLen == 0):
        return False
    elif(numLen == 1):
        return True

    # Place integer into list
    resultList = [int(x) for x in n]

    # Extract number from list backwards
    result = 0
    numLen -= 1
    while(numLen >= 0):
        result += resultList[numLen] * (10 ** numLen)
        numLen -= 1
    
    print("Does " + str(n) + " equal " + str(result) + "???????\nDecide for yourself!!!!")
    
    # Check if the number is palindromic
    if(int(n) == int(result)):
        return True
    else:
        return False

if(len(sys.argv) != 2):
    print("This script receives an integer and determines if it is palindromic")
    print("Usage: isIntPalindrome.py <integer>")
else:
    print(isIntPalindrome(sys.argv[1]))