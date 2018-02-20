## Sentence Tweet Length Calculator

# Part 1 - Create a program that measures how many characters are in a
# sentence.  If the sentence is too long for a tweet make sure the program
# tells you so, if the sentence fits into a tweet let me know as well.

# Ask for a tweet and save the input in variable tweet
print("Type your tweet here: ")
tweet = input()

if len(tweet) > 280:
    print("Your Tweet does not fit in the character limit.")
else:
    print("Thank You! Your tweet has been saved.")
