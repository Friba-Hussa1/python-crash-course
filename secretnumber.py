secret=20
number=int(input("Guess the secret number: "))

if number==secret:
    print("Congratulations! You guessed the secret number.")
elif number<secret:
    print("Too low! Try again.")
else:
    print("Too high! Try again.")   
    