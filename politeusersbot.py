#Polite Users Bot created by Kooldawgstar

import praw
from time import sleep
import random

USERNAME = "USERNAME"
PASSWORD = "PASSWORD"
LIMIT = 100
RESPONSES = ["Thanks for being a nice user and thanking people for help!",
             "Thank you for being a nice user and thanking people for help!",
            ]

responded = set()

r = praw.Reddit(user_agent="Enter in Useragent here")
r.login(USERNAME, PASSWORD)
subreddit = r.get_subreddit("Polite_Users_Bot")

def meets_criteria(responded, comment):
    #add whatever criteria/logic you want here
    return (not str(comment.author) == USERNAME) and (not comment.id in responded)  and ("thanks" , "thx" , "thank you" , "thank u" in comment.body.lower())

def generate_response(comment):
    #generate whatever response you want, you can make it specific to a comment by checking for various conditions
    return random.choice(RESPONSES)

while True:
    for comment in subreddit.get_comments(limit=LIMIT):
        if meets_criteria(responded, comment):
            print (comment.body)
            print (comment.id)
            print (str(comment.author))
            while True: #continue to try responding to the comment until it works, unless something unknown occurs
                try:
                    comment.reply(generate_response(comment))
                    print ("Breaking out after responding, and adding to the list")
                    responded.add(comment.id)
                    break
                except praw.errors.RateLimitExceeded:
                    print ("Sleeping, rate limit :(")
                    sleep(10*60) #sleep for 10 minutes, that's the timer limit
                except:
                    print ("Some unknown error has occurred, bail out...")
                    break
            print ("---------------------------------------\n\n")
    print ("sleeping")
    sleep(60) #sleep for a minute for new comments to show up
