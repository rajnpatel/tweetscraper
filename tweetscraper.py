import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
tweets_list1 = []

username = input("Enter the Twitter username here: ")
numberOfTweets = int(input("Enter the number of tweets you want to parse: "))
keywords = input("Enter the keyword(s) you want to count the sum of, separated by | without spaces if multiple keywords (case-sensitive): ")
print("Parsing...")

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:' + username).get_items()):
    if i == numberOfTweets:
        break
    tweets_list1.append([tweet.url, tweet.date, tweet.content])

# Creating a dataframe from the tweets list above
tweets = pd.DataFrame(tweets_list1, columns=['URL', 'Date/Time', 'Text'])

keywordCount = tweets.Text.str.count(keywords).sum()
numberOfTweets = str(numberOfTweets)

if keywordCount != 1:
    print("Number of times this user has mentioned the specified keyword(s) in the last " + numberOfTweets + " tweets:", keywordCount, "times.")
else:
    print("Number of times this user has mentioned the specified keyword(s) in the last " + numberOfTweets + " tweet:", keywordCount, "time.")

while True:
        save = input("Would you like to archive and save all " + numberOfTweets + " tweets in an excel file? (Y/N): ")
        if save == "Y" or save == "y":
            fileName = input("Enter the name of the excel file ending with .csv: ")
            tweets.to_csv(fileName)
            exit()
        elif save == "N" or save == "n":
            exit()
        else:
            print("Invalid input. Try again.")
