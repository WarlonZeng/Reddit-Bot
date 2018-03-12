import time
from pprint import pprint

def get_submissions_text(submissions):
    text = ''
    n = 1
    
    for i in submissions:
        print(vars(i)) # member variables
        if i.stickied:
            continue
        text += '<pre>%s: <a href="%s">%s</a> </pre>' % (str(n), i.url, i.title)
        text += '<pre>upvotes:  %s </pre>' % (i.score)
        text += '<pre>comments: %s </pre>' % (i.num_comments)        
        text += '<pre>age:      %s </pre>' % (get_age(i.created_utc))
        text += '-------------------------------------------------------------------------------------------------------------' + '<br/>' # my phone is pretty wide tbh
        n += 1
        
    return text

def get_age(utc_then):
    age_str = ''
    age = int(time.time()) - int(utc_then)
    days = int(age / 86400)
    hours = int((age % 86400) / 3600)
    minutes = int((age % 3600) / 60)
    
    if days >= 1:
        age_str ='%s days, %s hours, %s minutes' % (days, hours, minutes)
    elif days == 0 and hours >= 1:
        age_str = '%s hours, %s minutes' % (hours, minutes)
    else:
        age_str = '%s minutes' % (minutes)
        
    return age_str
