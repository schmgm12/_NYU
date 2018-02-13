
## Phone Number ##
## this will ask for number
phone_number = input('what is your phone number?\nInclude your area code\n')

phone_number = phone_number.replace('(', "")
phone_number = phone_number.replace(')', "")
phone_number = phone_number.replace('-', "")

if len(phone_number) != 10:
    print('Sorry that is an invalid number')
else:
    print("Your formatted number is {}-{}-{}".format(phone_number[0:3],
                                                    phone_number[3:6],
                                                    phone_number[6:]))
