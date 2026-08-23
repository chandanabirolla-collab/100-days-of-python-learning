def welcome():
    print("Hey, welcome!")

def main():
    welcome()

if __name__ == "__main__":
    main()
import sys

def welcome():
    print("Hey, welcome!")

# Checks if the script running is the main executing module
if sys.argv[0] == __file__:
    welcome()