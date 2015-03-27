from bottle import route, run, template
import os

@route('/')
def index():
    return '<b>Hello <b>'

run(host='localhost', port=os.environ['PORT'])
