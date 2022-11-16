__version__ = '0.1.0'
from flask import Flask, Response
from waitress import serve

from moderator import moderator
from user import user
from state import state
# from mod import moderator
from article import article
from updatedArticle import updatedArticle

app = Flask(__name__)
app.register_blueprint(state)
app.register_blueprint(moderator)
app.register_blueprint(user)
app.register_blueprint(article)
app.register_blueprint(updatedArticle)


@app.route("/")
def index():
    return "<span style = 'color: red'>Wrong page</span>"


@app.route("/api/v1/hello-world-12")
def HelloWorld():
    return "<h1>Hello World 12</h1>"

# session = Session()
# @app.route('/api/v1/article', methods=['POST'])
# def create_article():
#     # Get data from request body
#     data = request.get_json()

#     # Validate input data
#     try:
#         ArticleSchema().load(data)
#     except ValidationError as err:
#         return jsonify(err.messages), 400

#     # Check if article already exists
#     exists = session.query(Article.article_id).filter_by(name=data['name']).first()
#     if exists:
#         return Response(status=403, response='article with such number already exists.')

#     # Create new article
#     new_article = Article(name=data['name'], body=data['body'], version=data['version'])

#     # Add new article to db
#     session.add(new_article)
#     session.commit()

#     return Response(response='New audience was successfully created!')


if __name__ == '__main__':
    app.run(debug=True)
    # serve(app)
