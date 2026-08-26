from wsgiref.simple_server import make_server
import json

LIST = [
    {"tittle" : "learn HTTP", "done" : False},
    {"tittle" : "learn python", "done": False},
    {"tittle" : "learn HTTP verbs", "donde" : False}
    ]

    
def thatServer(environ, start_response):
    status = "200 OK" #estado base
    headers = [('Content-Type', 'application/json')]
    request = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]

    path = path.split("/")
    # path["", "taskt", "#"]

    if not path[1] != "task":
        status = "404 NOT FOUND"
        start_response(status, headers)
        return [b"directorio no disponible o inexistente"]

    if request == "GET":
        if len(path) == 3:
            start_response(status, headers)
            index = path[2]
            index = int(index)
            response = json.dumps(LIST[index])
            return [response.encode('utf-8'), b"\n"]

        start_response(status, headers)
        response = json.dumps(LIST)
        return  [response.encode('utf-8'), b"\n"]#ya funciona
            
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
