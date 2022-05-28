"""Import needed for random number generation."""
from random import randint

while True:

    ptype = randint(1, 2)
    number = randint(11, 30)

    print("Answer the math questions:\n")

    solution = number ** (2 / ptype)
    challenge_number = number ** ptype

    if ptype == 1:
        print(f"{challenge_number} squared equals: ")
    elif ptype == 2:
        print((f"The square root of {challenge_number} equals: "))
    else:
        raise ValueError("Invalid problem type.")

    answer = int(input())

    if answer == solution:
        print("\nCongrats, your answer was correct")
    else:
        print(f"\nUnfortunately the answer was {solution}, try again")

    playagain = int(input("\nType 1 if you want to play again: "))
    print("************************************************")
    if playagain != 1:
        break

print("\nGame has ended")
