# This script accepts a string and finds the longest palindromic substring in it
# Use: palindrome.py <string>

import sys
def longestPalindrome(s) -> str:
    n = len(s)
    if(n == 0):
        return ""
    elif(n == 1):
        return s[0]
    i = 0
    subs = dict()
    
    while(i <= n):
        j = i+1
        while(j <= n):
            sub = s[i:j]
            if(sub == sub[::-1]):
                subs[sub] = len(sub)
            j += 1
            
        i += 1

    return max(subs, key=subs.get)
    #END longestPalindrome
print(longestPalindrome(sys.argv[1]))