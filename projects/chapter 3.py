"""Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.

Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)

Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.

Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1."""


import time

def collatz(number):
    if number%2 == 0:
        new = number // 2
    else:
        new = 3 * number + 1
    print(new)
    return new


print("Type a number")
while True:
    number = input()
    try:
        number = int(number)
        if number != 0:
            break
        else:
            print("Natural numbers only.. try again")
    except ValueError:
        print("Invalid input.. try again")

while number != 1:
    number = collatz(number)
    time.sleep(0.1)
