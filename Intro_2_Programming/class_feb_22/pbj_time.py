
def ask_for_slices_bread():
    """asks for the number of slices of bread"""
    return int(input("\nHow many slices of bread do you have?\n"))

def ask_for_peanut_butter():
    """asks for the amount of units of peanut butter"""
    return int(input("\nHow many sandwiches worth of peanut butter do you have\n"))

def ask_for_jelly():
    """asks for the amount of units of jelly"""
    return int(input("\nHow many sandwiches worth of jelly do you have?\n"))

def left_over_bread(bread_input):
    """tells someone that there is a leftover slice"""
    if bread_input % 2 == 1:
        print("\nThere is an extra slice of bread!\n\n")

## tell the user how many sandwiches they can make
def sandwich_count(slices_of_bread, peanut_butter, jelly):
    """will tell the user how many sandwiches they can make"""
    bread_pairs = (slices_of_bread // 2)
    possible_sandwiches = min(bread_pairs, peanut_butter, jelly)
    print("You can make {} sandwiches.".format(possible_sandwiches))

def main():

    bread = ask_for_slices_bread()
    pb = ask_for_peanut_butter()
    jelly = ask_for_jelly()

    sandwich_count(slices_of_bread = bread, peanut_butter = pb, jelly = jelly)
    left_over_bread(bread_input = bread)

if __name__ == '__main__':
    main()
