# Problem 1: Reverse a String
        # TODO: Find length of string (len())
        # -1 always gives you the last character of word/string
        # USE for loop w/ range function


# def reverser(theword):
#     reversed_word= ""       # Why a blank "" ?
#     for index in range(len(theword)-1, -1, -1):  # What is the signifigance of 3 -1's ??
#         reversed_word += theword[index]     # Why += and why [ ]
#     return reversed_word

# print(f"Hello Phil reversed is: {reverser('Hello Phil')}")   # Why { } ?    # <-- print() line would not work with '' it needed ""




# Problem 2: Capitalize Letter
    ## Use the capitalize() function: Capitalizes only the FIRST letter of a string (Possibly use split() function to split the string into words)
    #** capwords() function (string.capwords()): converts first letter of every word into uppercase** (Use split() method)
    # upper() function: Takes all lower case letters in a string and turns them to capital letters
    # swapcase() function: Returns string with their opposite casing (uppercase to lower & lower to upper)

import string 

sentence= 'Hello world, my name is phil'
formatted= string.capwords(sentence, sep= None)
print(formatted)    






# Problem 3: Compress a string of characters



# Problem 4 (BONUS): Palindrome







