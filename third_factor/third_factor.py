import string
import sys
from time import sleep
import random

def main():

    about_to = f"{sys.argv[1]}, which is risky." if len(sys.argv) > 1 else "do something risky."
    verify(f"You're about to {about_to} Are you sure this is a good idea?","YES")
    verify("Are you sure there isn't a better, safer way to achieve what you're about to do?", "I AM SURE THERE IS NOT")
    verify("You’re not too sleep deprived, under-caffeinated, too many beers etc.?","I AM OF SOUND MIND")
    verify("Prove it: type this random string.", ''.join(random.choice(string.ascii_uppercase) for i in range(10)))
    print("Let's cool off for 10 seconds and think...")
    for i in range(1,11):
        print(f"{i}..", end='', flush=True)
        sleep(1)
    print()
    verify("You're still sure?","YES")
    print('Be careful, and don’t say you weren’t warned…')
    sys.exit(0)


def verify(question: str, answer: str) :
    success = False
    while not success:
        print(question)
        response = input(f"Type {answer.upper()} to continue: ")
        if response.upper() != answer.upper():
            print("OK then.")
            sys.exit(1)
        print("--------------------------")
        if response == answer.upper():
            success = True
        else:
            print("I can't HEAR you...")


if __name__ == '__main__':
    main()