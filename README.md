# Vicarious Pig Latin Microservice
This is a microservice built on the Flask Python microframework. This microservice can be used to translate requested strings into [Pig Latin](https://en.wikipedia.org/wiki/Pig_Latin), with the following specifications:
  - Listens on port 80, accepts a string that contains at least one word, but potentially entire paragraphs.
  - Convert the words to Pig Latin and return the results in the HTTP message body.
  - Preserve all of the punctuation in the original string.

## Dependencies
- [Python](https://www.python.org/) 3.5
- [Flask](http://flask.pocoo.org/) 0.12
- [Requests](http://docs.python-requests.org/en/master/) 2.13.0
- [Setuptools](https://pypi.python.org/pypi/setuptools) 20.10.1

## Setup

### Install all dependencies
Install `virtualenv` using [pip](https://pypi.python.org/pypi/pip) if you do not already have it installed, `pip install virtualenv`.
  - Troubleshooting: If you have Anaconda installed, it is likely that your `virtualenv` PATH will not work for this particular implementation, this can be fixed by installing `virtualenv` with the built-in version of Python like so: `/usr/local/bin/pip3.5 install virtualenv`

To install all the dependencies required to run this microservice, use the command `make install`.

### Launching the server
To run the server, use the command `sudo make launch`
  - Troubleshooting: because we are running on a protected port, `sudo` permissions must be used, either use `sudo -s` to activate `sudo` permissions for your current Terminal session, or execute the command using `sudo make launch`). This launches a `virtualenv` with the dependencies installed previously.

### Running tests
To run the included unit tests, use the command `make test` (note that this must be run after the server has been launched).

### Shutdown and cleanup
To shutdown the microservice, use the command `make shutdown`. If you want to clean up all the build files and virtual environment files created, use the command `make clean`.

## Using the API
The API can be interacted with at the `127.0.0.1/api/translate` endpoint. For example, we can [cURL](https://curl.haxx.se/) this resource with the following command:

`curl -d "Query string here" -i -X POST 127.0.0.1/api/translate`

The API accepts `Content-Type: text/plain` or `Content-Type: application/x-www-form-urlencoded` (it will also attempt to read from any `json` stream) and returns `Content-Type: text/plain`.

## Resources
- Requirements generated using [pipreqs](https://github.com/bndr/pipreqs)
- Setup structure inspired by umermansoor's [microservices](https://github.com/umermansoor/microservices)
- Lorem Ipsum test paragraph generated from [loripsum](http://loripsum.net/)
- Testing framework: [unittest](https://docs.python.org/2/library/unittest.html)