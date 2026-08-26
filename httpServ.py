
from wsgiref.simple_server import make_server
import json

LIST = []
ID = 1;

def thatServer(environ, start_response):
    global ID
    global LIST

    request = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]
    status = "200 OK"
    headers = [('Content-Type', 'application/json')]
    path = path.split("/")
    # path["", "taskt", "#"]

    if path[1] != "tasks":
        status = "404 Not Found"
        start_response(status, headers)
        return [b"Not Found"]

    if request == "GET":
        if len(path) == 3:
            start_response(status, headers)
            key = path[2]
            key = int(key)
            flag = 0
            for i in range(0, len(LIST)):
                if(LIST[i]["id"] == key):
                    response = json.dumps(LIST[i])
                    flag = 1
                    break
            
            if flag == 1:
                return [response.encode('utf-8'), b"\n"]
            else:
                status = "404 Not Found"
                start_response(status, headers)
                return [b"tarea inexistente"]
        else:
            start_response(status, headers)
            response = json.dumps(LIST)
            return  [response.encode('utf-8'), b"\n"]#ya funciona
        
    elif request == "POST" :
        x = int(environ.get('CONTENT_LENGTH', 0))
        body = environ['wsgi.input'].read(x)
        
        tarea = json.loads(body)

        tarea["id"] = ID
        ID += 1

        LIST.append(tarea)
        status = "201 Created"
        start_response(status, headers)

        response = json.dumps(tarea)
        return [response.encode('utf-8'), b"\n"]

    elif request == "PATCH":
        start_response(status, headers)
        return [b"no implementado"]
    elif request == "DELETE":
        if len(path) == 3 and len(LIST) >= 1:
            start_response(status, headers)
            index = path[2]
            index = int(index)
            for i in range (0, len(LIST)):
                if(LIST[i][id] == index):
                    del LIST[index]
                    return [b"la tarea fue eliminada con exito"]
        else:
            status = "404 Not Found"
            start_response(status, headers)
            return [b"no existe tal elemento"]

        



with make_server("", 9292, thatServer) as server:
    print("running on port 9292")
    server.serve_forever()
