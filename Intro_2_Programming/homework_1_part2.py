## Sentence Tweet Length Calculator

# Part 2 - Adjust the code to say how many characters you have remaining to
# use, or how many you need to trim it by to turn it into a tweet.

print("Type your tweet here:")
tweet = input()

tweet_checked = False # initialize a variable for checking tweet
while tweet_checked == False:

    if len(tweet) > 280:
        trim_chars = len(tweet) - 280
        print("Your Tweet is " + str(trim_chars) + " characters over the limit.")
        print("Re-enter your tweet trimming " + str(trim_chars) + " characters.")
        tweet = input()

    else:
        rem_chars = 280 - len(tweet)
        print("You have " + str(rem_chars) + " characters remaining.")
        tweet_checked = True
