from flask import Flask, request

app = Flask(__name__)


# From http://flask.pocoo.org/snippets/57/
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    file_name = path.split('/')[-1]
    formatted_file_name = _format_file_name(file_name, request.method)
    response = open('app/' + formatted_file_name).read()
    return response


def _format_file_name(file_name, method):
    return file_name + '.' + method.lower()


if __name__ == '__main__':
    app.run()
