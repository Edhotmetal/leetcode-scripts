# Problem #11
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Usage: python waterContainer.py <int1> <int2> ... <intn> *"DEBUG" *"GRAPH"
# The DEBUG flag outputs extra debugging information
# The GRAPH flag uses matplotlib to create a separate window where the data is plotted on a bar graph

import sys
import logging
# Imports for graph
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# Creates and returns a logger that outputs to standard output
def stdLogger(loggerName):
    log = logging.getLogger(loggerName)
    stdHandler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(logging.BASIC_FORMAT)
    stdHandler.setFormatter(formatter)
    log.addHandler(stdHandler)
    return log

# graph(height, bar1, bar2)
# Displays a separate window using matplotlib to graph the data
# Highlights the bars used to create the largest area in green

def graph(height, bar1, bar2):
    y_pos = np.arange(len(height))
    
    barlist = plt.bar(y_pos, height, align = 'center', alpha = 0.5)
    plt.ylabel("Container Height")
    barlist[bar1].set_color('g')
    barlist[bar2].set_color('g')
    plt.show()

# maxArea(height, *debug_option)
# Receives a list of non-negative integers that represent points: (i, height[i])
# Each point creates a vertical line from the x-axis up to the point
# maxArea returns the area of the pair of lines that creates the largest container of water
# 1. Start with the first value.
# 2. Compare with next value. If it is less than or equal, use first height. If greater, use next height and calculate area.
# 3. If area is greater than stored result, store both values and area. If not, skip.

def maxArea(height, *debug_option):
    log = stdLogger("maxArea")

    # If caller has requested logs, make it happen!
    if((["DEBUG"] in debug_option) or (["GRAPH", "DEBUG"] in debug_option) or (["DEBUG", "GRAPH"] in debug_option)):
        log.setLevel(logging.DEBUG)
        log.debug("Logs ready")

    log.debug("List length: " + str(len(height)))
    area = 0 # Area between i and j
    result = ([0,0], 0) # Tuple that stores the indexes and area of largest pair
    i = 0
    j = len(height) - 1

    # This loop uses a two pointer method to iterate from each end of the list and find the largest area
    while(i < j):
        log.debug("i = " + str(i) + " j = " + str(j))
        if(height[i] < height[j]):
            area = height[i] * (j - i)
        else:
            area = height[j] * (j - i)
        log.debug("area = " + str(area))
        if(result[1] < area):
            log.debug(str(result[1]) + " is less than " + str(area))
            result = ([i,j], area)
        else:
            log.debug(str(result[1]) + " is not less than " + str(area))
        if(height[i] < height[j]):
            i += 1
            log.debug("Moving i to the right")
        else:
            j -= 1
            log.debug("Moving j to the left")


    log.debug("Max area is between (" + str(result[0][0]) + ", " + str(height[result[0][0]]) + ") and (" + str(result[0][1]) + ", " + str(height[result[0][1]]) + ") with an area of " + str(result[1]))

    # If caller has requested a graph, make it happen too!
    if((["GRAPH"] in debug_option) or (["GRAPH", "DEBUG"] in debug_option) or (["DEBUG", "GRAPH"] in debug_option)):
        log.debug("Attempting to graph data")
        graph(height, result[0][0], result[0][1])

    return result[1]

if(len(sys.argv) == 1):
    print("                 ~~~~~~~~~~waterContainer.py~~~~~~~~~~")
    print("This script receives a list of integers representing the potential walls of a container of water")
    print("The script then returns the area of the largest container that can be made from the data")
    print("Usage: python waterContainer.py <int1> <int2> ... <intn> \"DEBUG\" \"GRAPH\"")
    print("The DEBUG flag shows the logic of the algorithm")
    print("The GRAPH flag uses matplotlib to create a separate window and represent the data using a bar graph")
else:
    mainLog = stdLogger("mainLogger")
    # Pass DEBUG and/or GRAPH options to maxArea
    options = list()

    args = list() # Place integer arguments into list to pass them into maxArea
    for arg in sys.argv:
        mainLog.debug(arg)
        try:
            args.append(int(arg))
        except ValueError:
            if(arg == "waterContainer.py"):
                pass
            elif(arg == "DEBUG" or arg == "GRAPH"):
                options.append(arg)
            else:
                mainLog.warning(arg + " is not an integer")
    
    if(len(args) == 0):
        print("Please enter a list of integers. Execute the script without arguments for help.")
        sys.exit()

    print(maxArea(args, options))
