import random


def user_guess(x):
    num = random.randint(0, x)  # Get the number from 0 to x
    guess = None
    # print(num)

    while guess != num:
        # check user input whether it is number and in range x
        is_not_correct = True
        while is_not_correct:
            try:
                val = input(f"\nPlease enter your guessing number from 0 to {x}: ")
                guess = int(val)
                if guess not in range(x+1):
                    raise ValueError
                is_not_correct = False
            except ValueError:
                print("Invalid guess")

        # Check guessing number
        if guess < num:
            print(f"Sorry, {guess} is too low")
        elif guess > num:
            print(f"Sorry, {guess} is too high")

    # Get here when guess == num
    print(f"Yay! The number is {guess}")


def comp_guess(x):
    low = 0
    high = x
    true_fb = {'c': 'Correct', 'h': 'High', 'l': 'Low'}
    feed_back = None

    while feed_back != 'c' and high >= low:
        if high > low:
            guess = random.randint(low, high)
        elif high == low:
            guess = high

        # Check user input
        feed_back = input(f'\n{guess} is? Too high (h)  ||  Too low (l)  ||  Correct (C): ').lower()
        while feed_back not in true_fb:
            feed_back = input(f"I don't understand your feed back, please input again ").lower()

        # Handle feed back
        if feed_back == 'h':
            high = guess - 1
        elif feed_back == 'l':
            low = guess + 1
        # print(high, low)
    # Get here when guess true or high < low
    if high >= low:
        print(f"My number is {guess}")
    else:
        print("Your feed back must be wrong!!!")

user_guess(15)
