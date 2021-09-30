from typing import Optional

import fastapi
import uvicorn

# creating an instance of the api
api =  fastapi.FastAPI()


# defining a function to display the home page
@api.get('/')
def index():
    body = "<html>" \
           "<body style='padding: 10px;'>" \
           "<h1>Welcome to the API</h1>" \
           "<div>" \
           "Try sum: <a href='/api/calculate/sum?x=7&y=11'>/api/calculate?x=7&y=11</a>" \
           "<div>" \
           "Try subtraction: <a href='/api/calculate/subtract?x=7&y=11'>/api/calculate?x=7&y=11</a>" \
           "<div>" \
           "Try multiply: <a href='/api/calculate/multiply?x=7&y=11'>/api/calculate?x=7&y=11</a>" \
           "<div>" \
           "Try divide: <a href='/api/calculate/divide?x=7&y=11'>/api/calculate?x=7&y=11</a>" \
           "</div>" \
           "</body>" \
           "</html>"
    
    return fastapi.responses.HTMLResponse(content=body)


# defining x and y query params as concrete types which are required
# z is Optional Value which can be omitted but if passed should be an Integer
@api.get('/api/calculate/sum')
def sum(x: int, y: int, z: Optional[int] = None):
    result = (x + y)
    if z is not None:
        result += z
    return {
        'x': x,
        'y': y,
        'z': z,
        'result': result
    }


# defining x and y query params as concrete types which are required
# z is Optional Value which can be omitted but if passed should be an Integer
@api.get('/api/calculate/subtract')
def subtract(x: int, y: int, z: Optional[int] = None):
    result = (x - y)
    if z is not None:
        result -= z
    return {
        'x': x,
        'y': y,
        'z': z,
        'result': result
    }

# defining x and y query params as concrete types which are required
# z is Optional Value which can be omitted but if passed should be an Integer
@api.get('/api/calculate/multiply')
def multiply(x: int, y: int, z: Optional[int] = None):
    result = (x * y)
    if z is not None:
        result *= z
    return {
        'x': x,
        'y': y,
        'z': z,
        'result': result
    }


@api.get('/api/calculate/divide')
def divide(x: int, y: int):
    # returning 400 status code and json response in case use makes bad request by sending y or z as 0 
    if y == 0:
        return fastapi.responses.JSONResponse(content={"Error": "y cannot be 0"}, status_code=400)

    result = (x / y)
    return {
        'x': x,
        'y': y,
        'result': result
    }


# running application via uvicorn server
uvicorn.run(api)