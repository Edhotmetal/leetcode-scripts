# This program extracts the first integer in a string and prints it
# Usage: extractInteger.py <String>

import sys
def extractInt(s):
    if(len(s)==0): # Conversion fails if string is empty
        return 0

    s = s.lstrip() # Remove beginning whitespace

    isPositive = True

    if(s[0]=='-'):
        isPositive = False # If the first character is a negative sign, the result will be multiplied by -1 later
            
    resultList = []
    result = 0
    # Extract digits from string
    for d in s.split():
        try:
            resultList.append(int(d))
        except ValueError:
            pass

    numLen = len(resultList) # The length of the number
            
    # Take digits from list and place in variable
    i = 0
    while(numLen > 0):
        result += int(resultList[i]) * (10 ** (numLen-1))
        i += 1
        numLen -= 1

    if(isPositive==False):
        result = result * -1

    return result

if(len(sys.argv) != 2):
    print("###This program extracts the first integer in a string and prints it")
    print("Returns 0 when conversion fails")
    print("Usage: extractInteger.py <string>")
else:
    print(extractInt(sys.argv[1]))