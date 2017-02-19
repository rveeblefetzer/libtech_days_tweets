# libtech_days_tweets
A script to pull the last 10 tweets by @Liberationtech

## To run:
Add API and OAuth information:

```python
consumer_key = "" # Add your Twitter API key between the quote marks
consumer_secret = "" # Add your Twitter API secret between the quote marks

access_token = "" # Add your Twitter access token between the quote marks
access_secret = "" # Add your Twitter token secret between the quote marks
```

For more information on this, see the [Twitter API documentation](https://dev.twitter.com/ads/tutorials/getting-started).

Once that's set up, you can run the script from the command line:

```
python libtech_tweepy.py
```

The program will tell you the number of tweets it's found (it should be 10, the way it is), or that it hit an error and will run again in 15 minutes. If you want to quit this, type `CONTROL-c`.

The program will write the last 10 tweets to a file in the same directory named `days_tweets.txt`.

The format for each tweet will be the tweet URL, tweet text and the expanded link from within the tweet. E.g.:

```
https://twitter.com/Liberationtech/status/833379727691886592
The latest The Liberationtech Daily! https://t.co/WGRVUpKJUC
http://paper.li/Liberationtech?edition_id=853a4330-f6cf-11e6-89dc-0cc47a0d15fd
```


