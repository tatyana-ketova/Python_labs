"""
You can actually make a simple command line game. You could put together everything
 you've learned so far about Python. The game goes like this:

1. The computer will think of 3 digit number that has no repeating digits.
2. You will then guess a 3 digit number
3. The computer will then give back clues, the possible clues are:
     Close: You've guessed a correct number but in the wrong position
     Match: You've guessed a correct number in the correct position
     Nope: You haven't guess any of the numbers correctly
 4. Based on these clues you will guess again until you break the code with a
    perfect match!

 There are a few things you will have to discover for yourself for this game!
 Here are some useful hints:

Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
print(digits[:3])

Another hint:
guess = input("What is your guess? ")
print(guess)

 Think about how you will compare the input to the random number, what format
 should they be in? Maybe some sort of sequence?
"""
import random
def thinkNumbers():
    list_digits=[]
    for i in range(3):
        list_digits.append(random.randint(0, 9))

    return list_digits


def guessNumbers(digits):
    userlist=[]
    right_answers=0

    for i in range(3):
        userlist.append(int(input("Write your number ")))
        if digits[i] == userlist[i]:
            print("You've guessed a correct number in the correct position")
            right_answers=right_answers+1
        elif userlist[i] in digits and digits[i] != userlist[i]:
            print("You've guessed a correct number but in the wrong position")
        else:
            print("You've not guessed a number")
    if right_answers==3:
        print("You win!")
    if right_answers < 3:
        answer=input("Do you want to try again? Y/N ")
        if answer == "Y":
            guessNumbers(list_digits)
        else:
             print("Thank you for game!")
             print("Your answer:{} Right answer: {}".format(userlist, digits))

list_digits=thinkNumbers()
print(list_digits)
guessNumbers(list_digits)

