# This program receives two integer arrays from the user, combines them, and calculates the median of the resulting list
# Use: Simply run the program and follow on-screen prompts

def findMedianSortedArrays(nums1, nums2) -> float:
    nums3 = nums1 + nums2 # Combine both arrays
    nums3.sort() # Sort the array
    print(nums3) # Print the resulting array

    n = len(nums3)

    if(n % 2 == 0): # Check if the median must be calculated
        return float((((nums3[int((n/2)-1)]))+(nums3[int(n/2)]))/2) # Calculates and returns median if the array length is even 
    else:
        return float(nums3[int(n/2)]) # Returns median if the array length is odd

print("Input two integer arrays and I will combine them to find the median!")
print("Enter the first array with the elements separated by spaces")
x = input().split() # Splits the input into separate elements and stores it into a list
print(x)
print("Enter the second array with the elements separated by spaces")
y = input().split()
print("Calculating median...")
try:
    print("The median of " + str(x) + " and " + str(y) + " is " + str(findMedianSortedArrays(list(map(int, x)), list(map(int, y)))))
except:
    print("Please enter only integers separated by spaces.")
