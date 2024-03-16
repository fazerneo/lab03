# Firstr I initialize a variable char with the number sequence
char = "123456789"

# Then I create a for loop that iterates over a range, that starts at the length of the string, stops at zero and has a decrement of -1
for i in range(len(char), 0, -1):
    # Then we make a nested for loop where we iterate over j in the range(i). Here i holds the value from the above loop
    # Each iteration of j is from 1 and ends at the value of range(i), which is lower with each iteration.
    for j in range(i):
        # we print the character at index j and make sure all iterations of this inner loop are in one line with end=''
        print(char[j], end='')
    # After one round of inner loop iteration, we run a blank print statement to move to the next line.
    print()