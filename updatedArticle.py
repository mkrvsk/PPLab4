from flask import Blueprint, Response, request, jsonify
from marshmallow import ValidationError
from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth
from dbmodel import Moderator, UpdatedArticle, Session, User, Article
from validation_schemas import UpdatedArticleSchema

updatedArticle = Blueprint('updatedArticle', __name__)
bcrypt = Bcrypt()

session = Session()
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    try:
        user = session.query(User).filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
    except:
        return None


@updatedArticle.route('/api/v1/updateArticle', methods=['POST'])
@auth.login_required
def create_updatedArticle():
    # Get data from request body
    data = request.get_json()
    current = auth.current_user()
    if current.user_id != data['user_id']:
        return Response(status=403, response='Access denied')

    # Validate input data
    try:
        UpdatedArticleSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check if supplied ArticleId correct
    db_user = session.query(Article).filter_by(article_id=data['article_id']).first()
    if not db_user:
        return Response(status=404, response='A article_id with provided not ok.')
    # Create new article
    new_updatedArticle = UpdatedArticle(article_id=data['article_id'], user_id=data['user_id'],
                                        moderator_id=data['moderator_id'], state_id=data['state_id'],
                                        article_body=data['article_body'], date=data['date'])

    # Add new article to db
    session.add(new_updatedArticle)
    session.commit()

    return Response(response='New updatedArticle was successfully created!')


# Get article by id