# I use a while loop as I want to take user input continuously until the break condition is met.
while True:
    # I take a user line as my first input var.
    # I state the break statement right after as I want to break out directly without having to go through typing another input in user_word.
    user_line = input("enter a string of words: ")
    if user_line.lower() == "quit":
        break
    # I take the second input var
    user_word = input("now enter the magical word: ")
    
    # Now i use the in method to check whether the word exists in the line.    
    if user_word in user_line:
        # if the condition is met, i use the f'string method with the find method to find and print out the position of the word in the line.
        print(f"The word does exist in zee line and zee position of the word in line is: {user_line.find(user_word)}")
    # If the word does not exist in the line, I just print out a response.    
    else:
        print("word not in line")