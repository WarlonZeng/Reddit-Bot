import praw
from _settings import settings

def test_reddit_instance():
    '''only testing if you can create a Reddit instance'''
    
    reddit = praw.Reddit(client_id=settings.client_id, client_secret=settings.client_secret, user_agent=settings.user_agent)
    assert True
