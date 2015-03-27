from bottle import route, run, template

@route('/')
def index():
    return '<b>Hello <b>'

run(host='0.0.0.0', port=80)
