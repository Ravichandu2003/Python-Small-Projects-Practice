import random   #for selecting a random number
import math     #for math operations
#range boundaries
low = int(input("enter the lower number of range: "))
upp = int(input("enter the upper number of range: "))
# selecting a random number in the range between low and upp
number = random.randint(low,upp)
#printing number of chances for guessing
print("\n\tYou've only ",round(math.log(upp - low + 1, 2))," chances to guess the integer!\n")
count = 0
#loop for guessing
while count < math.log(upp - low + 1, 2):
    count+=1
    # guessing the number
    guess = int(input("enter the number: "))
    #checking the number
    if guess == number:
        print("you win")
        break #break the loop
    elif guess > number:
        print("too high")
    elif guess < number:
        print("too low")
#guesses more then the no of chances
else:
    print("\n\tyou lose\t\n")
if count >= math.log(upp - low + 1, 2):
    print("\nThe number is %d" % number)
    print("\tBetter Luck Next time!")