
## Re-write the phone number activity from class 3 with functions:

def phone_number_input():

    phone_number = input('What is your phone number?\n')

    number_checked = False

    while number_checked == False:

        if len(phone_number) != 10 or phone_number.isnumeric() == False:
            print('Sorry that is an invalid number.\n')
            phone_number = input('Please enter your number like ##########\n')
        else:
            number_checked == True
            return phone_number

def phone_number_format(phone_number):

    print("Your formatted number is ({}){}-{}".format(phone_number[0:3],
                                                     phone_number[3:6],
                                                     phone_number[6:]))

def main():

    phone_number = phone_number_input()
    return phone_number_format(phone_number)

if __name__ == '__main__':
    main()
