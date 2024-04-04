# lab03
Week 3 python principles and programming lab
Questions:
Ex1. Write a program that reads a string and reverses it. Your program must be able to save the new reversed string in another variable. You must use "for loop" and indexing to accomplish this task. Compare your reversed string with the reversed string produced using the built-in syntax such as s[: : -1] to see if they look the same (using comparison operator "==").

Ex2. Write a program that reads in a continuous input of decimal numbers, stops when the user enters "stop". Think carefully about the most appropriate loop to use for this task. Upon entry into the loop body, keep track of the largest number input. Once input is complete, the program should output the largest number received accurate to the 3rd decimal place.

Hint: to keep track of the largest number during the input, you can use a variable, such as largest, to keep the running largest number. Each time you get a new number from the user, compare it with the largest. If it is larger than the largest, you update the largest. But what initial value should you give to variable largest? One way is to assign the first number read from the user to this variable. Alternatively, you may initialise the variable to float('-Infinity').

Ex3. Write a program that repeatedly reads in a line and a word from the user and then report whether the line contains the word. If the line contains the word, print out the position of the word in the line. The program would finish if the line entered by the user is "quit".

Use one of the string methods to complete the above task.

Ex4. Write a program that creates the following output pattern using a nested loop and a string.

123456789 
12345678 
1234567 
123456 
12345 
1234
123 
12 
1
Hint: 1) store a digit sequence in a string, such as char = "123456789" ; 2) when printing a digit inside a row, use print(char[j], end='') to avoid the newline at the end of each line.

Ex5. Write a program to read a list of marks in a unit until the user enters "end". Calculate and report the following: 1) the total number of marks, 2) the number of students receiving HD, D, C, P and N grades, 3) the percentage of students who fail the unit. Note, when you print the numbers and the percentage, you must use formatted strings and you must print the percentage sign, such as "30.1% of students failed the unit".

Ex6. Modify the program in Lecture Notes to use the Guess-and-Check algorithm to calculate the cubic root of a number. The modified program can take any integer number as input, including negative integer number. It also repeatedly asks the user to enter a number and then output its cubic root if it is a perfect cube until the user enter "stop".


