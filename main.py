from sanic import Sanic
from sanic.response import json 

app = Sanic(__name__)

@app.route("/hello")
async def test(request):
    return json({"hello": "world"})

import requests

@app.route("/call")
async def call(request):
    url = 'https://jsonplaceholder.typicode.com/posts/1/comments'
    r = requests.get(url)
    return json(r)

app.run(host="0.0.0.0", port=8000, debug=True, workers=12)
