import twitter

from datetime import datetime, timedelta
from threading import Timer

from tokens import (CONSUMER_KEY,
                    CONSUMER_SECRET,
                    ACCESS_TOKEN_KEY,
                    ACCESS_TOKEN_SECRET)


class ChuckoyTwitter():
    """
    Main class
    """

    def __init__(self):
        api = twitter.Api(consumer_key=CONSUMER_KEY,
                          consumer_secret=CONSUMER_SECRET,
                          access_token_key=ACCESS_TOKEN_KEY,
                          access_token_secret=ACCESS_TOKEN_SECRET,
                          cache=None)
        self._api = api
        self.startTweeting('mealreminders')

    def postStatus(self, update):
        if isinstance(update, basestring):
            status = self._api.PostUpdate(update)
            print 'Tweet posted: \"' + status.text + '\"'

    def startTweeting(self, mode):
        if mode == 'mealreminders':
            update = '@chuckoy, eat breakfast!'
            time = [8, 30, 0]
            now = datetime.today()
            future = (now + timedelta(days=1)).replace(hour=time[0], minute=time[1], second=time[2])
            secs = self.calculateDelay(future, now)
            Timer(secs, recurringTweet(update, time)).start()

            update = '@chuckoy, eat lunch!'
            time = [12, 30, 0]
            now = datetime.today()
            future = (now + timedelta(days=1)).replace(hour=time[0], minute=time[1], second=time[2])
            secs = self.calculateDelay(future, now)
            Timer(secs, recurringTweet(update, time)).start()

            update = '@chuckoy, eat dinner!'
            time = [18, 30, 0]
            now = datetime.today()
            future = (now + timedelta(days=1)).replace(hour=time[0], minute=time[1], second=time[2])
            secs = self.calculateDelay(future, now)
            Timer(secs, recurringTweet(update, time)).start()

    def recurringTweet(self, update, time):
        self.postStatus(update)
        now = datetime.today()
        future = (now + timedelta(days=1)).replace(hour=time.0, minute=time.1, second=time.2)
        secs = self.calculateDelay(future, now)
        t = Timer(secs, recurringTweet(update, time))
        t.start()
        return t

    def calculateDelay(self, future, now):
        delta_t = future - now
        return delta_t.seconds + 1