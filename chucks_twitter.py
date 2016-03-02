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
        self.postStatus("Gising na si yaya!")
        self.startTweeting('mealreminders')

    def postStatus(self, update):
        if isinstance(update, basestring):
            status = self._api.PostUpdate(update.encode('utf8'))
            print 'Tweet posted: \"' + status.text + '\"'

    def startTweeting(self, mode):
        print 'Scheduling tweets...'
        if mode == 'mealreminders':
            update = u'@chuckoy, eat breakfast!'
            time = [0, 30, 0]
            now = datetime.today()
            future = (now + timedelta(days=1)).replace(hour=time[0], minute=time[1], second=time[2])
            secs = self.calculateDelay(future, now)
            Timer(secs, self.recurringTweet, [update, time]).start()

            update = u'@chuckoy, eat lunch!'
            time = [4, 30, 0]
            now = datetime.today()
            future = (now + timedelta(days=1)).replace(hour=time[0], minute=time[1], second=time[2])
            secs = self.calculateDelay(future, now)
            Timer(secs, self.recurringTweet, [update, time]).start()

            update = u'@chuckoy, eat dinner!'
            time = [10, 30, 00]
            now = datetime.today()
            future = (now + timedelta(days=1)).replace(hour=time[0], minute=time[1], second=time[2])
            secs = self.calculateDelay(future, now)
            Timer(secs, self.recurringTweet, [update, time]).start()

            print '\tMeal tweets have been scheduled!'
        print 'All requested tweets have been scheduled!'

    def recurringTweet(self, update, time):
        self.postStatus(update)

        # recalculate the next day
        now = datetime.today()
        future = (now + timedelta(days=1)).replace(hour=time[0], minute=time[1], second=time[2])
        secs = self.calculateDelay(future, now)
        t = Timer(secs, self.recurringTweet, [update, time])
        t.start()

    def calculateDelay(self, future, now):
        delta_t = future - now
        return delta_t.total_seconds()

if __name__ == '__main__':
    chuckoyTwitter = ChuckoyTwitter()
