import praw

# quick intro to **kwargs:
# send the entire dict of args to praw (that accepts kwargs)
# if the client accepts something like client_id=... it's probably **kwargs

def get_reddit_instance(**kwargs):
    reddit = praw.Reddit(**kwargs)
    print('Sucessfully authenticated into Reddit')
    return reddit

def get_submissions(reddit, subreddit, **kwargs):
    subreddit = reddit.subreddit(subreddit)
    submissions = subreddit.top('week', **kwargs) 
    submissions = sorted(submissions, key=lambda x: x.score, reverse=True)
    return submissions
