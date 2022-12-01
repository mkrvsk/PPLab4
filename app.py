__version__ = '0.1.0'
from flask import Flask, Response
from waitress import serve

from state import state
from moderator import moderator
from user import user
from article import article
from updatedArticle import updatedArticle

app = Flask(__name__)
app.register_blueprint(state)
app.register_blueprint(moderator)
app.register_blueprint(user)
app.register_blueprint(article)
app.register_blueprint(updatedArticle)


@app.route('/api/v1/hello-world-12')
def myendpoint():
    return   Response(status=200, response="Hello World 12")


serve(app, port='5000')