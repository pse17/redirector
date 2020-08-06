import unittest
import json
import sys
import os
import squidRedirector as SR



sys.path.insert(0, os.path.dirname(__file__))

class RedirectorTests(unittest.TestCase):

    def setUp(self):
        SR.CONFIG_PATH = 'test.conf'
        test_rule = {'yandex.ru': 'google.com'}
        with open('test.conf', 'w') as test_conf:
            json.dump(test_rule, test_conf)

    def test_read_config(self):
        self.assertEqual(SR.read_config(), {'yandex.ru': 'google.com'})

    def test_check_url(self):
        test_url_check = 'zen.yandex.ru:443 127.0.0.1/localhost'
        #test_url_uncheck = 'https://python.org'

        self.assertEqual(SR.check_url(test_url_check), ("OK", '302:https://google.com'))
        # self.assertEqual(SR.check_url(test_url_uncheck), ("ERR", "") )
