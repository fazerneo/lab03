# I could not remember eactly how sir solved this exercise so I tried my way, i think it is close to what sir did. 
# I take an input from the user
# I initialize an empty variable
# I initalize another variable to store the length of the input string.
# I use a -1 as the length of a string may be 7 but the indexing in python starts from 0 so the length should be -1 than the length
original_str = input("enter your string: ")
reversed_string = ""
original_str_length = len(original_str) -1

# I make a for loop to iterate through all characters in the input string
for char in original_str:
    ''' The reversed string var takes the character at the index number equivalent to the input string length,
    this ensures that the iteration starts from the end. This character is added to the beginning of the reversed string var '''
    reversed_string = reversed_string + original_str[original_str_length]
    ''' Now i ensure that to iterate further, the var holding the string length is reduced by -1, 
    this way the iteration proceeds to the next character in a reverse order. '''
    original_str_length = original_str_length - 1

# now I print the reversed string outside the loop so that i only have the final result     
print(reversed_string)