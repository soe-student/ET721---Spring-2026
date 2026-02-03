"""
Feb 3, 2026
Soe Kaythi
Lab 3, Conditional Statements and Loop python
"""
#conditional statement states the flow of the program
print("\n---Example 1: Conditional Statements and Loops in Python---")
age = 21
if age < 18:
    print("You are a minor.")
elif age == 21:
    print("You just became an adult.")
elif age > 21:
    print("You are an adult.")
else:
    print("You are in your golden years.")

print("\n ---Example 2:For Loop ----")
# for loop as a counter to print from 9 to 1
for i in range(9, 0, -1):
    print("Iteration:", i)

print("\n---Example 3: for Loop in a list----")
num = [1, -2, 3, 4, -9]
count_negative = 5
for n in num:
    if n < 0:
        count_negative += 1
else:
    print("There is/are", count_negative, "negative numbers.")
print("\n---End of Program---")

print("\n---Example 4: while Loop as a counter ----")
# while loop to print from -3 to 5, inclusive, step of 2, output --> -3 -1 1 3 5
x = -3
while x <= 5:
    print(x)
    x += 2

print("\n---Example 5: while Loop with user input ----")
# program collects a number from the user and if the number is even or odd
# after that, the program will ask the user if another number will be tested
# if the user enters 'y', the loop continues; else, the program ends

decision_user = 'y'
user_number = 0

while True:
    user_number = int(input("Enter a number: "))
    if user_number % 2 == 0:
        print(f"The number {user_number} is even.")
    else:
        print(f"The number {user_number} is odd.")
    
    decision_user = input("Do you want to test another number? (y/n): ")
    if decision_user.lower() != 'y':
        print("Exiting the program. Goodbye!")
        break

print("\n---Exercise 1: Validate a number between 1 and 9---")
user_number = 0
while user_number < 1 or user_number > 9:
    user_number = int(input("Enter a number between 1 and 9: "))
print(f"You entered: {user_number}")


print("\n---Exercise 2: Guess the number with 3 attempts---\n")
number = 9
attempts = 0
for attempts in range(3):
    guess = int(input("Enter your guess(1-9): "))
    if guess == number:
        print("Congratulations!Your guess is correct.")
        break
    elif guess < number:
        print("Too low. Try again!\n")
    else:
        print("Uhh.. too high!\n")
else:
    print("\nSorry, you've used all your attempts.")
    print(f"The correct number was: {number}")

