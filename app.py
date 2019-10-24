
from bottle import route, run, default_app

@route('/')
def index():
    return "<h1> hello OpenShift V3 Ninja</h1>"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)

app = default_app()
