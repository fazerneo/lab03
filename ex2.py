'''I could not remember exactly how sir did it and realised that now I have to do these assignments on monday or tuesday itself.
However, i tried what I could. I tried taking the first user input as the largest but I could not do it, would be grateful if sir
can show us that way also'''
# I initialized a variable callest largest with the float -infinity
largest = float('-Infinity')

# I made a while loop as I wanted the iterations to be continuous unless broken with the break condition
while True:
    # I take a use input
    user_input = input("enter your decimal numbers: ")
    # I create a break condition that states if the user types stop then the loop breaks. I use the lowe function to accept all cases of STOP, Stop or stop
    if user_input.lower() == 'stop':
        break
    # I turn the user input into a float for processing
    user_input = float(user_input)    
    ''' Now I start keeping track of the largest decimal, since the largest var is -Inf, so if user types that then the largest var 
    will be printed to the console. We cannot check if the input is lower than largest as -inf is the lowest possible. '''
    if largest == user_input:
        print(f"Largest number is: {largest}")
    # However, if the largest is smaller than the user input, which is almost always true, the largest var is updated and the largest var is printed
    elif largest < user_input:
        largest = user_input
        print("Largest number is: {:.3f}".format(largest))
        
    

    
