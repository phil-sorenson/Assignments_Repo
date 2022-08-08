# Problem #3: Compress a String
# Compress a string of characters
# a. For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"


original_string= 'aaabbbbbccccaacccbbbaaabbbaaa'
final_result= ''
letter_counter= 1

for index_num in range(len(original_string)):     # index_num can be named ANYTHING
    if index_num == len(original_string)-1:
        final_result+= str(letter_counter) + original_string[index_num]
    elif original_string[index_num] == original_string[index_num+1]:
        letter_counter += 1
    elif original_string [index_num] != original_string[index_num+1]:
        final_result += str(letter_counter) + original_string[index_num]
        letter_counter= 1

print(final_result)
