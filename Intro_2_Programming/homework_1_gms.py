## Sentence Tweet Length Calculator

# ask for the character limit and save to char_limit
# convert input to an integer
char_limit = int(input("What is the character limit?\n"))
tweet = input("Type your tweet here:\n")

tweet_checked = False # initialize a variable for checking tweet
tweet_approved = False # initialize a variable for user approving tweet
while tweet_checked == False & tweet_approved == False:

    if len(tweet) > char_limit:
        trim_chars = len(tweet) - char_limit
        print("Your Tweet is {} characters over the limit.".format(trim_chars))
        print("Re-enter your tweet trimming {} characters.\n".format(trim_chars))
        tweet = input()

    else:

        rem_chars = char_limit - len(tweet)
        print("You have {} characters remaining.\n".format(rem_chars))
        approval = str(input("Are you ready to submit this tweet (y/n)?\n"))

        if approval.lower() == 'y' or approval.lower() == 'yes':
            tweet_approved = True
            tweet_checked = True
        elif approval.lower() == 'n' or approval.lower() == 'no':
            tweet = input("Okay enter your new tweet.\n")
        else:
            tweet = input("Sorry, we didn't understand that\nEnter your tweet\n")
