# Reverse a string

def reverser(theword):
    reversed_word= ""       # Why a blank "" ?
    for index in range(len(theword)-1, -1, -1):  # What is the signifigance of 3 -1's ??
        reversed_word += theword[index]     # Why += and why [ ]
    return reversed_word

print(f"Hello Phil reversed is: {reverser('Hello Phil')}")   # Why { } ?    # <-- print() line would not work with '' it needed ""