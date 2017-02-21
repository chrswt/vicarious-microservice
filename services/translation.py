from flask import Flask, make_response, request
import re


app = Flask(__name__)

def translate_word(word):
    """Translates a single word to Pig Latin"""
    VOWELS = {'a', 'e', 'i', 'o', 'u'}

    # Handle punctuations
    if not word.isalpha():
        return word

    # Handle capitalized words
    if word[0].isupper():
        return translate_word(word.lower()).capitalize()

    # Case: word begins with a vowel
    if word[0].lower() in VOWELS:
        return word.lower() + 'yay'

    # Case: word begins with a consonant        
    else:
        for index, char in enumerate(word):
            if char.lower() in VOWELS:
                return word[index:].lower() + word[:index].lower() + 'ay'

    # Case: word contains no vowels
    return word + 'ay'

def translate_sentence(sentence):
    # Split sentences into words and punctuation (hyphenated words, etc.
    # are treated as two separate words, per Pig Latin convention).
    # https://docs.python.org/3/library/re.html#re.split
    words = re.split('(\W)', sentence)
    return ''.join([translate_word(x) for x in words])

@app.route('/api/translate', methods=['POST'])
def on_post():
    """Handles API route for English -> Pig Latin translation"""
    data = request.stream.read().decode('utf-8')

    if not data:
        response = make_response('Error: POST requests for translations '
                                 'must contain at least one word.')
        response.status_code = 406 # Not Acceptable
        return response

    response = make_response(translate_sentence(data))
    response.status_code = 200 # OK
    response.content_type = 'text/plain'
    return response

if __name__ == '__main__':
    app.run(port=80, debug=True)