import unittest
import requests


class TranslationTests(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1/api/translate'

    def test_given_words(self):
        test_words = ['pig', 'banana', 'trash', 'happy', 'duck', 'glove',
                      'eat', 'omelet', 'are']
        expected_words = ['igpay', 'ananabay', 'ashtray', 'appyhay', 'uckday',
                          'oveglay', 'eatyay', 'omeletyay', 'areyay']

        responses = [requests.post(self.url, x).text for x in test_words]
        self.assertEqual(responses, expected_words, 'Responses should match')


if __name__ == '__main__':
    unittest.main()