"""Sentiment Classifier"""
"""This project is to classify extracted tweets with their number of retweets and number of replies"""

"""Task is to build a sentiment classifier, which will detect how positive or
negative each tweet is. I created a csv file, which contains columns for the
Number of Retweets, Number of Replies, Positive Score (which is how many happy
words are in the tweet), Negative Score (which is how many angry words are in
the tweet), and the Net Score for each tweet. At the end, I uploaded the
csv file to Excel or Google Sheets, and produce a graph of the Net Score vs
Number of Retweets.

To start,I defined a function called strip_punctuation which takes one parameter,
a string which represents a word, and removes characters considered punctuation
from everywhere in the word."""

# Punctuation characters to be filtered from the words or sentences
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(astr):
    """This function  strip_punctuation takes one parameter,
    a string which represents a word, and removes characters considered
    punctuation from everywhere in the word."""
    for char in punctuation_chars:
        char_strip = astr.replace(char, '')
        astr = char_strip
    return  char_strip#.strip()

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def get_pos(astr):
    """This function called get_pos takes one parameter, a string
    which represents a one or more sentences, and calculates how many words in
    the string are considered positive words. Use the list, positive_words to
    determine what words will count as positive. The function should return a
    positive integer - how many occurances there are of positive words in the
    text. """
    num_pos_words = 0
    astr_split = astr.split()
    astr = astr_split
    for word in astr:
        words_pos_strip = strip_punctuation(word.strip())
        if words_pos_strip in positive_words:
            num_pos_words = num_pos_words + 1
        else:
            continue
    return num_pos_words

# list of negative words to use
negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_neg(astr):
    """This function called get_neg takes one parameter, a string which
    represents a one or more sentences, and calculates how many words in the
    string are considered negative words. Use the list, negative_words to
    determine what words will count as negative. The function should return a
    positive integer - how many occurances there are of negative words in the
    text. """
    num_neg_words = 0
    astr_split = astr.split()
    astr = astr_split
    for word in astr:
        words_pos_strip = strip_punctuation(word.strip())
        if words_pos_strip in negative_words:
            num_neg_words = num_neg_words + 1
        else:
            continue
    return num_neg_words

# Open the project file containing the fake twitter data
with open('project_twitter_data.csv') as pro_tweet_f:
    """This code opens the file project_twitter_data.csv which has the fake
    generated twitter data (the text of a tweet, the number of retweets of that
    tweet, and the number of replies to that tweet). """
    with open("resulting_data.csv","w") as output_tweet_f:
        """This code to create a csv file called resulting_data.csv, which
        contains the Number of Retweets, Number of Replies, Positive Score
        (which is how many happy words are in the tweet), Negative Score
        (which is how many angry words are in the tweet), and the Net Score
        (how positive or negative the text is overall) for each tweet."""
         #header = pro_tweet_f.readlines()[0]
        #output_tweet_f.write(pro_tweet_f.readline()[0][1:])
        """# This creates the header of the csv file"""
        output_tweet_f.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
        output_tweet_f.write("\n") # I added the newline character since to write to new lines
        for tweet in pro_tweet_f.readlines()[1:]: # Since the first line is the csv file header, i started from the second line
            tweets = tweet.strip().split(",")
            num_retweets = tweets[1]
            num_replies = tweets[2]
            pos_tweets = get_pos(strip_punctuation(tweets[0]))
            neg_tweets = get_neg(strip_punctuation(tweets[0]))
            net_tweets = pos_tweets - neg_tweets
            row_str_tweets = "{}, {}, {}, {}, {}".format(num_retweets, num_replies, pos_tweets, neg_tweets, net_tweets)
            output_tweet_f.write(row_str_tweets)
            output_tweet_f.write("\n")
            print("{} {} {}".format(pos_tweets, neg_tweets, net_tweets))
