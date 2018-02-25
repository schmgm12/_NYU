
def ask_integer():
    """this function asks for an integer value"""
    return int(input("\nEnter an integer: "))

def odd_or_even(integer):
    """this function will tell you if the integer input is odd or even"""

    if integer % 2 == 0:
        print("even")
    else:
        print("odd")

def main():
    user_input = ask_integer()
    odd_or_even(user_input)

if __name__ == '__main__':
    main()
