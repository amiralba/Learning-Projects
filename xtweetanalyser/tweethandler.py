import tweepy
import os
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
from tweepy.errors import TooManyRequests, NotFound, TweepyException
import time

load_dotenv()

consumer_key=os.getenv('TWITTER_API_KEY')
consumer_secret = os.getenv('TWITTER_API_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
bearer_token = os.getenv('TWITTER_BEARER_TOKEN')

client = tweepy.Client(bearer_token=bearer_token)
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)
api = tweepy.API(auth)

def get_tweets(username, count=100):
    try:
        user = client.get_user(username=username)
        user_id = user.data.id
        tweets = client.get_users_tweets(user_id, max_results=count, tweet_fields=['created_at'])
        
        tweet_data = []
        for tweet in tweets.data:
            tweet_data.append({
                'tweet': tweet.text,
                'created_at': tweet.created_at
            })
        
        return tweet_data

    except TooManyRequests as e:
        reset_time = int(e.response.headers.get('X-Rate-Limit-Reset', time.time() + 900))
        wait_time = reset_time - int(time.time())
        print(f"Rate limit exceeded. Waiting for {wait_time} seconds.")
        time.sleep(wait_time + 10)
        return get_tweets(username, count)

    except NotFound:
        print(f"User '{username}' not found.")
        return []

    except TweepyException as e:
        print(f"Error with Tweepy request: {e}")
        return []

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def proccess_tweet_data(tweet_data):
    df = pd.DataFrame(tweet_data)
    df['created_at'] = pd.to_datetime(df['created_at'])
    
    tweets_per_day = df.groupby(df['created_at'].dt.date).size()
    tweets_per_month = df.groupby(df['created_at'].dt.to_period('M')).size()
    tweets_per_year = df.groupby(df['created_at'].dt.to_period('Y')).size()
    
    return tweets_per_day, tweets_per_month, tweets_per_year


def plot_tweet_graph(tweets_per_day, tweets_per_month, tweets_per_year):
    plt.figure(figsize=(10, 6))
    tweets_per_day.plot(kind='bar')
    plt.title("Tweets per Day")
    plt.xlabel("Date")
    plt.ylabel("Number of Tweets")
    plt.xticks(rotation=45)
    plt.tight_layout()
    daily_graph_path = 'tweets_per_day.png'
    plt.savefig(daily_graph_path)
    plt.close() 

    plt.figure(figsize=(10, 6))
    tweets_per_month.plot(kind='bar')
    plt.title("Tweets per Month")
    plt.xlabel("Month")
    plt.ylabel("Number of Tweets")
    plt.xticks(rotation=45)
    plt.tight_layout()
    monthly_graph_path = 'tweets_per_month.png'
    plt.savefig(monthly_graph_path)
    plt.close()

    plt.figure(figsize=(10, 6))
    tweets_per_year.plot(kind='bar')
    plt.title("Tweets per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Tweets")
    plt.xticks(rotation=45)
    plt.tight_layout()
    yearly_graph_path = 'tweets_per_year.png'
    plt.savefig(yearly_graph_path)
    plt.close()

    return daily_graph_path, monthly_graph_path, yearly_graph_path