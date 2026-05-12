#Instagram bot to unfollow certain number of users from your IG account:
#Need to install instapy using libraries
#Everything about this library instapy is here: https://pypi.org/project/instapy/0.1.0/
#sleep_delay: Sleep delay sets the time it will sleep after every
# ~10 unfollows (default delay is ~10 minutes). Below we are using
#60 seconds delay Amount = 6 implies how many to unfollow.
#We can change it 100 or 80 or 300. Let’s assume we want to unfollow
# 6 users (or 10 or 100). We use the code below:
from instapy import InstaPy
session = InstaPy(username = "Put your IG username here", password = "Put your IG
password here”)
session.login()
session.unfollow_users(amount=6, allFollowing=True,sleep_delay=60)
session.end()