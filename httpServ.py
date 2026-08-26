from wsgiref.simple_server import make_server
import json

def thatServer(environ, start_response):
    status = "200 OK" #estado base
    headers = [('Content-Type', 'text/plain')]
    request = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]
    

    if not path.startsWith("/task") :
        status = "404 NOT FOUND"
        start_response(status, headers)
        return [b"directorio no disponible"]
    if request == "GET":
        if path == "/task" or path == "/task/":
            start_response(status, headers)
            return [b"funcionando plenamente"]
        else:
            start_response(status, headers)
            return [b"funcionando plenamente"]
    elif request == "POST" :
        start_response(status, headers)
        return [b"no implementado"]
    elif request == "PATCH":
        start_response(status, headers)
        return [b"no implementado"]
    elif request == "DELETE":
        start_response(status, headers)
        return [b"no implementado"]


        


with make_server("", 9292, thatServer) as server:
    print("running on port 9292")
    server.serve_forever()
