from flask import Flask, make_response, request


app = Flask(__name__)

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

    response = make_response(data)
    response.status_code = 200 # OK
    response.content_type = 'text/plain'
    return response

if __name__ == '__main__':
    app.run(port=80, debug=True)