

def ask_day():
    """asks for the current day"""
    return input('What day is it?\n')

def sleep_in_checker(day_of_week):
    """checks if the day is a weekend day"""
    if day_of_week.lower() == "friday" or day_of_week.lower() == "saturday":
        print("You can sleep in tomorrow...enjoy!\n")
    elif day_of_week.lower() == 'sunday' or day_of_week.lower() == 'monday' or\
    day_of_week.lower() == 'tuesday' or day_of_week.lower() == 'wednesday'or\
    day_of_week.lower() == 'thursday':
        print("You need to set an alarm for the morning...")
    else:
        print("Error: day of week not found.")

def main():
    today = ask_day()
    sleep_in_checker(today)

if __name__ == '__main__':
    main()
