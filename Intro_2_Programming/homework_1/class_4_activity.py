
## 2-15-2018
## Class 4 Activity

## Rewrite HW #1 so that all the code runs with functions and a main function
## Sentence Tweet Length Calculator

## Funtion to ask for the character limit
def set_char_limit():
    return int(input("What is the character limit?\n"))

## Function to ask for tweet
def input_tweet():
    return input("Type your tweet here:\n")

## Check if the tweet is within the character limit
def tweet_length_checker(tweet, char_limit):

    if len(tweet) > char_limit:
        print("Your tweet is {} characters over the limit.\n".format(\
        len (tweet) - char_limit))
        return False
    else:
        print("Your tweet is within the limit")
        return True

def main():

    char_limit = set_char_limit()

    tweet_checked = False # initialize a variable for checking tweet

    while tweet_checked == False:

        tweet = input_tweet()
        tweet_checked = tweet_length_checker(tweet, char_limit)




if __name__ == '__main__':
    main()
