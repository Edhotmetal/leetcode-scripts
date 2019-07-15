# This program extracts all of the integers in a string and prints them
# Usage: extractAllIntegers.py <String>
# This script is a spinoff of my solution to leetcode challenge #8
# Limitations: This script does not pull integers that are part of a word

import logging
import logging.handlers
import sys

def extractInt(s, *log_option):
    # Create Logger
    log = logging.getLogger("IntegerLogger")
    
    # Set the log handlers if the DEBUG option has been specified by the caller    
    if('DEBUG' in log_option):
        log.setLevel(logging.DEBUG)
        # Create handler for outputting logs to integerlog.txt
        fileHandler = logging.handlers.RotatingFileHandler("integerLog.txt", maxBytes=2000, backupCount=2)
        formatter = logging.Formatter(logging.BASIC_FORMAT)
        fileHandler.setFormatter(formatter)
        log.addHandler(fileHandler)

        # Create handler for outputting logs to standard output
        stdHandler = logging.StreamHandler(sys.stdout)
        stdHandler.setFormatter(formatter)
        log.addHandler(stdHandler)
    if(len(s)==0): # Conversion fails if string is empty
        log.warning("Conversion failed because the string is empty ")
        return 0

    resultList = []
    # Extract digits from string
    log.debug("Extracting digits from the string...")
    for d in s.split():
        try:
            log.debug(d)
            resultList.append(int(d))
        except ValueError:
            log.warning(d + " is not an integer")
            
    log.debug("resultList: " + str(resultList))

    return resultList

mainLog = logging.getLogger("MainLog")

if(len(sys.argv) == 3 and sys.argv[2] == "DEBUG"):
    mainLog.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(logging.BASIC_FORMAT)
    handler.setFormatter(formatter)
    mainLog.addHandler(handler)

    mainLog.debug("Debug logs turned on")

    mainLog.debug("Extracting integer from \"" + sys.argv[1] + "\"")
    print(extractInt(sys.argv[1], 'DEBUG'))
elif(len(sys.argv) != 2):
    print("### This program extracts the first integer in a string and prints it")
    print("Returns 0 when conversion fails")
    print("Usage: extractAllIntegers.py <string>")
    print("extractAllIntegers.py <string> \"DEBUG\" for extra debugging information")
else:
    print(extractInt(sys.argv[1]))