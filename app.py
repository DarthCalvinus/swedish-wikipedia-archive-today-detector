import os

def application(environ, start_response):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    path = 'index.html'
    if os.path.exists(path):
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
        with open(path, 'rb') as f:
            return [f.read()]
    else:
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'404 Not Found']

app = application
