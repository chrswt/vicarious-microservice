from flask import Flask, make_response, request


app = Flask(__name__)

def translate_word(word):
    """Translates a single word to Pig Latin"""
    vowels = 'aeiou'

    # Case: word begins with a vowel
    if word[0] in vowels:
        return word + 'yay'

    # Case: word begins with a consonant        
    else:
        for index, char in enumerate(word):
            if char in vowels:
                return word[index:] + word[:index] + 'ay'

    # Case: word contains no vowels
    return word + 'ay'

@app.route('/api/translate', methods=['POST'])
def on_post():
    """Handles API route for English -> Pig Latin translation"""
    data = request.stream.read().decode('utf-8')

    if not data:
        response = make_response('Error: POST requests for translations '
                                 'must contain at least one word.')
        response.status_code = 406 # Not Acceptable
        return response

    elif type(data) is not str:
        response = make_response('Error: POST requests for translations must'
                                 'be provided in the "text/plain" format.')
        response.status_code = 415 # Unsupported Media Type
        return response

    response = make_response(translate_word(data))
    response.status_code = 200 # OK
    response.content_type = 'text/plain'
    return response

if __name__ == '__main__':
    app.run(port=80, debug=True)