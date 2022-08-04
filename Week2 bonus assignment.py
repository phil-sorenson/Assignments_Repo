# Use and practice Python fundamentals, w/ an emphasis on SINGLE RESPONSIBILITY FUNC.
# Practices used: Func (def), Data Type, Flow Control (Conditionals), Loops, Dictionary/List Data Structure (USE W3 school link to research)

## Python Dictionaries-- Used to store data values "key:value pairs" (Written with {} and have keys & values)
    # Dictionary Items-- Are ordered, changeable, and does not allow duplicates (presented in 'Key:Value' pair & can be referred to by using "Key Name")
    # Dictionaries (thisdict=) Ordered= items have defined order, and will not change Unordered= VICA VERSA and cant refer via INDEX
    # Dictionaries (thisdict=) are changeable==can change, add, or remove items after thisdict= has been created
    # Duplicates are NOT allowed
    # len() function determines the number of items print(len(thisdict)) = 3
    # type() Dictionaries are defined as OBJECTS w/ data type "dict"  print(type(thisdict))= <class 'dict'>
    ## 4 Types of Collections (ARRAYS): 1. LIST- IS ordered and IS changeable. Allows duplicates
    #                                   2. TUPLE- IS ordered and NOT changeable. Allows duplicates
    #                                   3. SET- IS NOT ordered and NOT changeable and Unindexed. NO duplicates
    #                                   4. DICTIONARY- IS ordered and IS changeable. NO duplicates
 
# thisdict = {
#     "brand": "Ford",   # <---- EXAMPLE (KEYS= brand, model, year)    (VALUES= Ford, Mustang, 1964-->2020)
#     "model": "Mustang",                                                # CAN BE ANY DATA TYPE (str, int, boolean, or list)
#     "year": 1964,
#      "year": 2020}        <--- DUPLICATE VALUES WILL OVERWRITE== will print(2020) & NOT print(1964)
# print(thisdict['brand'])

# As a developer, I want to make at least five commits on GitHub with descriptive messages.
# As a user, I want an engaging story to be told using print() statements.
# As a user, I want Hercules (and each enemy), to have health, attack power, and a List of attack names saved in a Dictionary.
# As a user, I want the ability to select Hercules’ attack using a menu prompt.
# As a user, I want the foe’s attack to be chosen at random.
# As a user, I want the results of each attack to be logged in the terminal.
# As a developer, I want to use an Attack() function that will terminate when Hercules or an enemy’s health reaches zero.
# As a developer, I want my RunGame() function to call my other functions in a logical order that will determine game flow.
# As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!