"""Twitter."""
import re


class Tweet:
    """Tweet class."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """
        Tweet constructor.

        :param user: Author of the tweet.
        :param content: Content of the tweet.
        :param time: Age of the tweet.
        :param retweets: Amount of retweets.
        """
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets


def find_fastest_growing(tweets: list):
    """
    Find the fastest growing tweet.

    A tweet is the faster growing tweet if its "retweets/time" is bigger than the other's.
    >Tweet1 is 32.5 hours old and has 64 retweets.
    >Tweet2 is 3.12 hours old and has 30 retweets.
    >64/32.5 is smaller than 30/3.12 -> tweet2 is the faster growing tweet.

    :param tweets: Input list of tweets.
    :return: Fastest growing tweet.
    """
    list_of_ratios = []
    for el in tweets:
        list_of_ratios.append(el.retweets / el.time)
    index = list_of_ratios.index(max(list_of_ratios))
    return tweets[index]


def sort_by_popularity(tweets: list) -> list:
    """
    Sort tweets by popularity.

    Tweets must be sorted in descending order.
    A tweet is more popular than the other if it has more retweets.
    If the retweets are even, the newer tweet is the more popular one.
    >Tweet1 has 10 retweets.
    >Tweet2 has 30 retweets.
    >30 is bigger than 10 -> tweet2 is the more popular one.

    :param tweets: Input list of tweets.
    :return: List of tweets by popularity
    """
    tweets.sort(key=lambda x: (-x.retweets, x.time))
    return tweets


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    """
    Filter tweets by hashtag.

    Return a list of all tweets that contain given hashtag.

    :param tweets: Input list of tweets.
    :param hashtag: Hashtag to filter by.
    :return: Filtered list of tweets.
    """
    list_of_tweets_w_hashtag = []
    for el in tweets:
        if hashtag in el.content:
            list_of_tweets_w_hashtag.append(el)
    return list_of_tweets_w_hashtag


def sort_hashtags_by_popularity(tweets: list) -> list:
    """
    Sort hashtags by popularity.

    Hashtags must be sorted in descending order.
    A hashtag's popularity is the sum of its tweets' retweets.
    If two hashtags are equally popular, sort by alphabet from A-Z to a-z (upper case before lower case).
    >Tweet1 has 21 retweets and has common hashtag.
    >Tweet2 has 19 retweets and has common hashtag.
    >The popularity of that hashtag is 19 + 21 = 40.

    :param tweets: Input list of tweets.
    :return: List of hashtags by popularity.
    """
    dictionary_of_tags = {}
    dictionary_keys = []
    pattern = r"[#]+[A-Za-z]+"
    final_hashtag_list = []
    for el in tweets:
        hashtags_from_content = re.findall(pattern, el.content)
        for hashtag in hashtags_from_content:
            if hashtag in dictionary_keys:
                dictionary_of_tags.setdefault(hashtag, []).append(el.retweets)
                dictionary_of_tags[hashtag] = [sum(dictionary_of_tags[hashtag])]
            else:
                dictionary_keys.append(hashtag)
                dictionary_of_tags[hashtag] = [el.retweets]
    sorted_dict = sorted(dictionary_of_tags.items(), key=lambda x: (x[1], x[0]), reverse=True)
    for key, value in sorted_dict:
        final_hashtag_list.append(key)
    return final_hashtag_list


if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart #LFG", 1249, 284200)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart", 366.4, 543)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 2192, 284743)
    tweets = [tweet1, tweet2, tweet3]

    sorted_hashtags = sort_hashtags_by_popularity(tweets)
    print(sorted_hashtags)  # -> "#heart"
