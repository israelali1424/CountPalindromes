

# This countPalindromes function will return the number of sunstrings that are palindrome from any given string
#  Funtion that Checks to see if a word is a palindrome
def is_palindrome(string):
    

    for i in range(0,len(string)/2):

        if string[i] != string[-(i+1)]:

            return False
    return True


print is_palindrome('mom')
def countPalindromes(s):
    # an empty array that will store all of the palindromes sunstrings of s
    array_of_palindromes = []
    # save the length of S
    length = len(s)
    # this will find every substirng of s
    for i in range(length):
        for j in range(i+1, length+1):
     # this will check to see if the  substring of s is a palindrome
            if  is_palindrome(s[i:j]):
        # Stores all the palindromes of from substring s in array so they can be counted later
                 array_of_palindromes.append(s[i:j])
        # will give you the exact number of substring of s that are palindromes
    return len(array_of_palindromes)
print countPalindromes("daata")
