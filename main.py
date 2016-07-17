import os
import argparse
from flask import Flask, request
from functools import wraps

app = Flask(__name__)
BASE_DIR = os.path.dirname(__file__)


def parse_args():
    parser = argparse.ArgumentParser(description="Static Response Server")
    parser.add_argument('-a', '--appHome', help='home for you app files', default='app/')
    args, unkown = parser.parse_known_args()
    return args

app_home = parse_args().appHome


def file_not_found_error_handling(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            return open(BASE_DIR + '/' + app_home + 'error/404.html').read(), 404
    return func_wrapper


def sanitize_path(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        path = kwargs['path']
        for s in str.split(path, '/'):
            if not os.path.exists(BASE_DIR + '/' + app_home + s + '/') \
                    and not os.path.isfile(BASE_DIR + '/' + app_home + s + '.' + request.method.lower()):
                path = path.replace(s, "any")
        path = path + 'index.html' if not path else path
        path = path + 'index.html' if path.endswith('/') else path
        path = path + '/index.html' if '.' not in path else path
        kwargs.update({'path': path})
        return func(*args, **kwargs)
    return func_wrapper


# From http://flask.pocoo.org/snippets/57/
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@file_not_found_error_handling
@sanitize_path
def catch_all(path):
    response = open(BASE_DIR + '/' + app_home + path + '.' + request.method.lower()).read()
    return response


if __name__ == '__main__':
    app.run()
