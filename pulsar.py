from pulsar.apps import wsgi

def hello(environ, start_response):
    data = b'Hello World!\n'
    response_headers = [('Content-type','text/plain'), ('Content-Length', str(len(data)))]
    start_response('200 OK', response_headers)
    return [data]

if __name__ == '__main__':
    wsgi.WSGIServer(callable=hello).start()
