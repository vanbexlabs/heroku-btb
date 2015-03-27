from bottle import route, run, template
import os

@route('/')
def index():
    return '<b>Hello <b>'

run(host='0.0.0.0', port=os.environ['PORT'])
