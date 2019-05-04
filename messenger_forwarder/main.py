# -*- coding: UTF-8 -*-

import os

from ListenBot import ListenBot
from fbchat.models import *
import pickle

try:
    username = os.environ['FBCHAT_USERNAME']
except:
    print("Please specify FBCHAT_USERNAME in fbchat.env, and source fbchat.env")
    exit(-1)

try:
    password = os.environ['FBCHAT_PASSWORD']
except:
    print("Please specify FBCHAT_PASSWORD in fbchat.env, and source fbchat.env")
    exit(-1)

try:
    with open('fbchat_session', 'rb') as f:
        session_cookies = pickle.load(f)
except FileNotFoundError:
    session_cookies = None

try:
    if session_cookies:
        client = ListenBot(username, password, session_cookies=session_cookies, user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36")
    else:
        client = ListenBot(username, password, user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36")
except FBchatException:
    print("Failed to login to Facebook. Please check internet connection, username/password in fbchat.env etc")
    exit(-2)

with open('fbchat_session', 'wb') as f:
    pickle.dump(client.getSession(), f)

client.listen()