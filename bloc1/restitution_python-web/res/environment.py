import wsgiserver

def my_app(environ, start_response):
    status = '200 OK'
    hello = 'WSGIserver is running!'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    return hello

server = wsgiserver.WSGIServer(my_app)
server.start()
