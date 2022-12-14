from random import*

#greet user
print("Welcome to guess my number you will try to guess the number im thinking of between 1 and 6, Good luck and have fun")

#generate random number
Random_Number = randint(1, 6)
guess = int(input("Please enter your guess:"))

#Check if number is correct
if Random_Number == guess:
  print("correct the number was" + str(Random_Number))
else:
  print("incorrect the number was " + str(Random_Number))