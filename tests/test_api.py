import twitter
import unittest

from tokens import (CONSUMER_KEY,
                     CONSUMER_SECRET,
                     ACCESS_TOKEN_KEY,
                     ACCESS_TOKEN_SECRET)


@unittest.skipIf(not CONSUMER_KEY and not CONSUMER_SECRET, "No tokens provided")
class ApiTest(unittest.TestCase):
    """
    Test if app can successfully post tweet
    """

    def setUp(self):
        api = twitter.Api(consumer_key=CONSUMER_KEY,
                          consumer_secret=CONSUMER_SECRET,
                          access_token_key=ACCESS_TOKEN_KEY,
                          access_token_secret=ACCESS_TOKEN_SECRET,
                          cache=None)
        self._api = api

    def testPostTweetAndDelete(self):
        print 'Testing post Tweet and delete test Tweet'
        status = self._api.PostUpdate(u'Test Update'.encode('utf8'))
        self.assertEqual(status.text, 'Test Update')
        status_2 = self._api.DestroyStatus(status.id)
        self.assertEqual(status.id, status_2.id)

if __name__ == '__main__':
    unittest.main()
