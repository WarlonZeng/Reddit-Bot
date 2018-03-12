# Reddit-Bot
Get top submissions of various subreddits. Built for weekly updates.

***I typically don't put comments in the code because it gets in the way of reading. Python code should be self-explanatory.*** Instead, all resources are dumped into docs. Helpful documents below and challenges (more like thoughts) I went through.

---

# HOW TO RUN

## SETTINGS
In _settings folder, rename "**dummy_settings**" to "**settings**" and edit the fields below with the correct information. To make it simpler on the command line:
```git
cp dummy_settings.py settings.py
vi settings.py
// do your changes here
rm dummy_settings.py
```

```python
limit = 25
subreddit = 'cscareerquestions'

client_id = '???'
client_secret = '???'
user_agent = 'python:X.Y.Z:v1.0.0 (by /u/???)'

gmail_user = '???@???.???'
gmail_password = '???'

sender = '???@???.???'
recipient = '???@???.???'
subject = 'Top Trending on /r/%s' % (subreddit)
```

## MAKEFILE
My setup is Ubuntu 16.04 LTS WSL.

### INSTALL PYTHON3, PIP3
I use python3, pip3.
```
make install-pip
```

### INSTALL
Assuming you have python3 and pip3, install praw and pytest:
```git
make install
```

## TEST
Make sure your credentials are valid:
```git
make test
```

## RUN
Lastly, run (this is non-daemon mode):
```
make
```

--- 

# Resources

## PRAW & REDDIT
Praw -- python client for reddit api
https://praw.readthedocs.io/en/latest/getting_started/quick_start.html

## GETTING SUBMISSIONS (tiny rant)
This Paw API design is pretty stupid, should be get_top() or something and not member activated but instead its .top(). Like, as soon as I instantiate a subreddit and I want to get new stuff a day later, will it be updated if I use the same object?? At least a member function will more likely say yes.
Output nature if using Reddit's "**Hot**" algorithm:
```git
Higher limit = more submissions, more "accurate in numbers", can pull from 1-2 days ago
Lower limit = less submissions, less "accurate in numbers", pulls fresh items
```

## SUBREDDIT SUBMISSIONS MEMBER VARIABLES
```git
from pprint import pprint
pprint(vars(submissions)) # member variables
```
There's a lot to list here, but the most notable ones are num_comments, score, title, url, and stickied.
Example:
```git
{'_comments_by_id': {},
 '_fetched': False,
 '_flair': None,
 '_info_params': {},
 '_mod': None,
 '_reddit': <praw.reddit.Reddit object at 0x000002A11FC2B588>,
 'approved_at_utc': None,
 'approved_by': None,
 'archived': False,
 'author': Redditor(name='AutoModerator'),
 'author_flair_css_class': None,
 'author_flair_text': 'Robot',
 'banned_at_utc': None,
 'banned_by': None,
 'brand_safe': True,
 'can_gild': False,
 'can_mod_post': False,
 'clicked': False,
 'comment_limit': 2048,
 'comment_sort': 'best',
 'contest_mode': False,
 'created': 1520435264.0,
 'created_utc': 1520406464.0,
 'distinguished': 'moderator',
 'domain': 'self.cscareerquestions',
 'downs': 0,
 'edited': False,
 'gilded': 0,
 'hidden': False,
 'hide_score': False,
 'id': '82merx',
 'is_crosspostable': False,
 'is_reddit_media_domain': False,
 'is_self': True,
 'is_video': False,
 'likes': None,
 'link_flair_css_class': None,
 'link_flair_text': None,
 'locked': False,
 'media': None,
 'media_embed': {},
 'mod_note': None,
 'mod_reason_by': None,
 'mod_reason_title': None,
 'mod_reports': [],
 'name': 't3_82merx',
 'no_follow': True,
 'num_comments': 403,
 'num_crossposts': 0,
 'num_reports': None,
 'over_18': False,
 'parent_whitelist_status': 'all_ads',
 'permalink': '/r/cscareerquestions/comments/82merx/official_salary_sharing_thread_for_new_grads/',
 'pinned': False,
 'quarantine': False,
 'removal_reason': None,
 'report_reasons': None,
 'saved': False,
 'score': 233,
 'secure_media': None,
 'secure_media_embed': {},
 'selftext': 'moderator's speech,
 'selftext_html': 'some lengthy markup',
 'send_replies': False,
 'spoiler': False,
 'stickied': False,
 'subreddit': Subreddit(display_name='cscareerquestions'),
 'subreddit_id': 't5_2sdpm',
 'subreddit_name_prefixed': 'r/cscareerquestions',
 'subreddit_type': 'public',
 'suggested_sort': None,
 'thumbnail': '',
 'title': '[OFFICIAL] Salary Sharing thread for NEW GRADS :: March, 2018',
 'ups': 233,
 'url': 'https://www.reddit.com/r/cscareerquestions/comments/82merx/official_salary_sharing_thread_for_new_grads/',
 'user_reports': [],
 'view_count': None,
 'visited': False,
 'whitelist_status': 'all_ads'}
```

## GOOGLE SMTP (BARE SOCKET):
Shamless plug -- *if you wanna check out my bare-socket version for smtp with google*:
CS-4793/6843 course @ NYU
https://github.com/WarlonZeng/CS4793-Computer-Networking/blob/master/python%20google%20mail%20spammer%20SMTP/lab_mail.py

## GOOGLE STMP (SMTPLIB EASY WAY):
Configure provider permissions for google email on rates for gmail smtp. You'll need to enable less-secure permissions for the account that's sending and it's probably up to 100 per day.
https://support.google.com/a/answer/176600?hl=en
https://support.google.com/a/answer/6260879?hl=en
https://support.google.com/accounts/answer/6010255
https://stackoverflow.com/questions/14139165/how-to-get-line-breaks-in-e-mail-sent-using-pythons-smtplib

## MIMETEXT
MIMEText is a wrapper for **message** buildup in the message field to
```git
smtplib.SMTP_SSL('smtp.gmail.com', 465).sendmail(sender, recipient, message.as_string())
```
https://stackoverflow.com/questions/14139165/how-to-get-line-breaks-in-e-mail-sent-using-pythons-smtplib

---

# Design

## QUICK AND EASY
Break down script into modules. They're not really object orientated, but it's quite modular as modules. Added minimal testing to see if your credentials are valid. Added Makefile. Try and catch the whole thing cuz it's gonna run forever. Used public libraries -- smtplib, praw, time, logging, etc. Runs on my personal AWS EC2 instance.