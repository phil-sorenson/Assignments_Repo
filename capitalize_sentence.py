# INSTRUCTOR SOLUTION:

original_sentence= "a great day to be alive!"
final_result= ""

for index_num in range(len(original_sentence)):
    if index_num == 0:
        final_result += original_sentence[index_num].capitalize()
    elif original_sentence[index_num -1] == ' ':
        final_result += original_sentence[index_num].capitalize()
    else:
        final_result += original_sentence[index_num]
print(final_result)






# def capitalizing():
#     string= "Hello world my name is phil!"
#     capital_string= string.title()
#     print(capital_string) 
#     return capital_string
# capitalizing()  



