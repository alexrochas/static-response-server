# Static Response Server
> Serving static files for http requests.

[![Build Status](https://travis-ci.org/alexrochas/static-response-server.svg?branch=master)](https://travis-ci.org/alexrochas/static-response-server)

So, yeah...after seeing the project [Canned](https://github.com/sideshowcoder/canned), I thinked -"Hey, I already done this two or three times, but never publish, I probably should done this. But different from this guy, I gonna do in Python!".

That's the history behind this project. For now, I've probably used the most heavy weight of the light weight web frameworks for python, [Flask](http://flask.pocoo.org/), used basicly a gist from one Flask developer and that's it. Not cover all the cases Canner cover, not even 10%. But if you think, is the best scenario to contribute and understand what is happening.

Glad you are reading this and enjoy.

## Installation

Linux:

```sh
pip3 install -r requirements.txt
```


## Usage example

After start server with
```bash
python3 main.py
```
Made requests to http://127.0.0.1 like
```
Accept: text/html
GET /index.html
```
And you will be served from the file ```/app/index.html.get``` with content
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Static page</title>
    </head>
    <body>
        <h1>Static Response Server</h1>
        <p>This page is a response GET</p>
    </body>
</html>
```



## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

## Release History

* 0.0.1
    * Work in progress


## Meta

Alex Rocha - [about.me](about.me/alex.rochas)