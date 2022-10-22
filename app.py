from flask import Flask
from waitress import serve

app=Flask(__name__)

@app.route("/")
def index():
    return "<span style = 'color: red'>Wrong page</span>"


@app.route("/api/v1/hello-world-12")
def HelloWorld():
    return "<h1>Hello World 12</h1>"


if __name__ == '__app__':
    
    serve(app)
