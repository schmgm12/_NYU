
def odd_or_even(integer):
    """this function will tell you if the integer input is odd or even"""

    if integer % 2 == 0:
        print("even")
    elif integer % 2 == 1:
        print("odd")
    else:
        print("Error: This funciton only takes integer values.")

odd_or_even(4)
odd_or_even(5)
odd_or_even(4.5)
odd_or_even(5.6)
