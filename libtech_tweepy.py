#!/usr/bin python
"""A quick script to grab @liberationtech's last 10 tweets."""

import tweepy
import datetime as dt
import time


def days_tweet_search():
    """Get one user's tweets for the day (max set to 10)."""
    consumer_key = "" # Add your Twitter API key between the quote marks
    consumer_secret = "" # Add your Twitter API secret between the quote marks

    access_token = "" # Add your Twitter OAuth access token between the quote marks
    access_secret = "" # Add your Twitter token secret between the quote marks

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    pulled_tweets = []
    try:
        new_tweets = api.user_timeline(screen_name="@liberationtech", count=10)

        print('found', len(new_tweets), 'tweets')
        if not new_tweets:
            print('no tweets found')
        pulled_tweets.extend(new_tweets)
    except tweepy.TweepError:
        print('exception raised, waiting 15 minutes')
        print('(until:', dt.datetime.now() + dt.timedelta(minutes=15), ')')
        time.sleep(15 * 60)
    with open("days_tweets.txt", "w") as out:
        # import pdb; pdb.set_trace()
        for tweet in pulled_tweets:
            relevant_stuff = []
            relevant_stuff.append(
                "https://twitter.com/Liberationtech/status/" + tweet._json["id_str"])
            relevant_stuff.append(tweet._json["text"])
            if tweet._json["entities"]["urls"]:
                relevant_stuff.append(tweet._json["entities"]["urls"][0]["expanded_url"])
            for segment in relevant_stuff:
                out.write(segment + "\n")
            out.write("\n")


if __name__ == "__main__":
    days_tweet_search()
