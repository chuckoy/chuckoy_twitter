import twitter
import unittest

from datetime import datetime, timedelta
from threading import Timer

from chuckoy_twitter import ChuckoyTwitter
from tokens import (CONSUMER_KEY,
                    CONSUMER_SECRET,
                    ACCESS_TOKEN_KEY,
                    ACCESS_TOKEN_SECRET)



@unittest.skipIf(not CONSUMER_KEY and not CONSUMER_SECRET, "No tokens provided")
class SchedulerTest(unittest.TestCase):
    """
    Test if app can successfully schedule functions
    """

    def setUp(self):
        self._chuckoyTwitter = ChuckoyTwitter()

    def testCalculateDelay():
        print 'Testing calculateDelay'
        now = datetime.today()
        future = (now + timedelta(days=1))
        secs = self._chuckoyTwitter.calculateDelay(future, now)
        self.assertEqual(24 * 60 * 60, secs)

    def testRecurringTweet(self):
        print 'Testing recurringTweet'
        update = 'Test tweet; ignore'
        time = [8, 30, 0]

        t = self._chuckoyTwitter.recurringTweet(update, time)

        now = datetime.today()
        future = (now + timedelta(days=1)).replace(hour=time[0], minute=time[1], second=time[2])
        secs = self._chuckoyTwitter.calculateDelay(future, now)

        t.cancel
        self.assertEqual(t.interval, secs)

if __name__ == '__main__':
    unittest.main()
