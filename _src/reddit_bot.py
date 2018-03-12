import logging
import time

from _settings import settings
from _src._email import email
from _src._reddit import reddit
from _src._parser import parser

logging.basicConfig(format = "[%(asctime)s] [%(levelname)s] %(message)s", level = logging.DEBUG)
logger = logging.getLogger()

# i think reddit and subreddit can get outdated
# reddit
#   subreddit
#     submissions

while (True):
    try:
        reddit_inst = reddit.get_reddit_instance(client_id=settings.client_id, client_secret=settings.client_secret, user_agent=settings.user_agent)
        submissions = reddit.get_submissions(reddit_inst, settings.subreddit, limit=settings.limit)

        text = parser.get_submissions_text(submissions)

        message = email.build_email(text, settings.subject, settings.sender, settings.recipient)
        email.send_email(message, settings.gmail_user, settings.gmail_password, settings.sender, settings.recipient)

        # 1 week = 604,800 seconds
        time.sleep(604800)
    except Exception as e:
        print(e)

