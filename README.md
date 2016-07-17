# Static Response Server
> Serving static files for http requests.

[![Build Status](https://travis-ci.org/alexrochas/static-response-server.svg?branch=master)](https://travis-ci.org/alexrochas/static-response-server)

So, yeah...after seeing the project [Canned](https://github.com/sideshowcoder/canned), I thinked -"Hey, I already done this two or three times, but never publish, I probably should done this. But different from this guy, I gonna do in Python!".

That's the history behind this project. For now, I've probably used the most heavy weight of the light weight web frameworks for python, [Flask](http://flask.pocoo.org/), used basicly a gist from one Flask developer and that's it. Not cover all the cases Canner cover, not even 10%. But if you think, is the best scenario to contribute and understand what is happening.

Glad you are reading this and enjoy.

## Installation

Linux:

```sh
pip3 install static_response_server
```


## Usage example

After start server with
```bash
static_response_server -a path/to/your/app
```
Made requests to http://127.0.0.1 like
```
Accept: text/html
GET /index.html
```
And you will be served from the file ```<path/to/your/app>/index.html.get``` with content
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
Make requests to http://127.0.0.1/person/123/contact from a route with format ```/person/:id/contact``` and you will be served from a index file inside directory named **any**. So, the folder path that this request will access is ```<path/to/your/app>/person/any/contact/index.html.get``` (in case the request be GET).

## Development

Install dependencies
```
pip3 install -r requirements.txt
```
Run tests with nose tests
```
nosetests
```
Run server in local app path
```
python3 server/__init__.py 
```

## Release History

* 0.0.1
    * Work in progress
    * Add support to routes with wildcards
* 0.0.2
    * Add to pypi 
    * Add console script


## Meta

Alex Rocha - [about.me](http://about.me/alex.rochas)