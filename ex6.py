# I chose a while loop for this operation
while True:
    # we take user input
    user_input = input("Enter any number that you want to find the cubic root of: ")
    # break condition stated
    if user_input == 'stop':
        break
    # user input is turned into float as it has to operate with another float in the below cube root formula
    user_input = float(user_input)
    # We use a formula instead of built in function for calculating cube root
    cubic_root = user_input ** (1/3)
    # we state that if the cubic root to the power 3 is not equal to original input, it is not perfect cube
    # we use this as stating equality ends up in errors. I would appreciate help in improving this.
    if cubic_root ** 3 != user_input:
        print('not a perfect cube')
    else:
        print(f'the cubic root is: {cubic_root}')
