import unittest
import requests


class TranslationTests(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1/api/translate'

    def test_given_words(self):
        """Should pass for the basic test cases provided"""
        test_words = ['pig', 'banana', 'trash', 'happy', 'duck', 'glove',
                      'eat', 'omelet', 'are']
        expected_words = ['igpay', 'ananabay', 'ashtray', 'appyhay', 'uckday',
                          'oveglay', 'eatyay', 'omeletyay', 'areyay']

        responses = [requests.post(self.url, x).text for x in test_words]
        self.assertEqual(responses, expected_words, 
                         'Should pass for the basic test cases provided')

    def test_capitalization(self):
        """Should preserve capitalization in words"""
        test_words = ['Capitalized', 'Words', 'Should', 'Work']
        expected_words = ['Apitalizedcay', 'Ordsway', 'Ouldshay', 'Orkway']

        responses = [requests.post(self.url, x).text for x in test_words]
        self.assertEqual(responses, expected_words,
                         'Words should preserve their capitalization')

    def test_sentences(self):
        """Should translate sentences with preserved punctuation"""
        test_sentence = ('Long sentences should retain their capitalization, '
                        'as well as punctuation - hopefully!!')
        expected_result = ('Onglay entencessay ouldshay etainray eirthay '
                           'apitalizationcay, asyay ellway asyay unctuationpay'
                           ' - opefullyhay!!')

        response = requests.post(self.url, test_sentence).text
        self.assertEqual(response, expected_result,
                         'Should translate sentences accurately')

    def test_edge_cases(self):
        """Should be able to handle words with no vowels"""
        test_word = 'sky'
        expected_result = 'skyay'

        response = requests.post(self.url, test_word).text
        self.assertEqual(response, expected_result,
                         'Should be able to translate words without vowels')

    def test_error_cases(self):
        """Should return errors for invalid input"""
        self.assertEqual(requests.post(self.url, '').status_code, 406,
                         'Should return HTTP/406 for empty strings')

    def test_long_paragraphs(self):
        """Should translate long paragraphs with new lines intact"""
        self.maxDiff = None
        expected_result = ''
        test_paragraph = ''

        with open('tests/lorem_ipsum.txt') as input_paragraph:
            test_paragraph = input_paragraph.read()
        with open('tests/lorem_ipsum_translated.txt') as expected:
            expected_result = expected.read()

        response = requests.post(self.url, test_paragraph).text
        self.assertEqual(response, expected_result,
                         'Should translate long paragraphs accurately')


if __name__ == '__main__':
    unittest.main()