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

# Other way to solve (IF ITS JUST ONE WORD)

original_word= "Time is a great thing" 
final_result= ''




# final_result += original_word[3]
# final_result += original_word[2]
# final_result += original_word[1]
# final_result += original_word[0]


# print(final_result)

# ANOTHER WAY incorporating Loops to print 'str' backwards

# for index_num in range(3, -1, -1):      # <--- range object (START(10), STOP(0), STEP-IN (-1))
#     final_result+= original_word[index_num]

# print(final_result)             # <--- Hard coded so need to find the legth of word/string


for index_num in range(len(orignal_word)-1, -1, -1):
    final_result+= original_word[index_num]

print(final_result)       # <----- FINAL SOLUTION      
