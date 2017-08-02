from bottle import route, run, template
from subprocess import call

@route('/test')
def index():
    call(["mkdir", "/tmp/stream"])
    call(["raspistill", "-w", "320", "-h", "240", "-q", "5", "-o", "/tmp/stream/pic.jpg", "-tl", "250", "-t", "9999999", "-th", "0:0:0"])
    return template('<div>Starting...</div>')

run(host='192.168.88.183', port=8081)
