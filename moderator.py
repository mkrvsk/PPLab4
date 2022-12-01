from flask import Blueprint, Response, request, jsonify
from marshmallow import ValidationError
from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth
from dbmodel import User, Moderator, Session, UpdatedArticle
from validation_schemas import UserSchema, ModeratorSchema

moderator = Blueprint('moderator', __name__)
bcrypt = Bcrypt()

session = Session()
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(moderatorname, password):
    try:
        db = session.query(Moderator).filter_by(moderatorname=moderatorname).first()
        if db and bcrypt.check_password_hash(db.password, password):
            return db
    except:
        return None


@moderator.route('/api/v1/moderator', methods=['POST'])
def registerModerator():
    # Get data from request body
    data = request.get_json()

    # Validate input data
    try:
        ModeratorSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check if user already exists
    exists = session.query(Moderator.moderator_id).filter_by(moderatorname=data['moderatorname']).first()
    if exists:
        return Response(status=404, response='Moderator with such moderatorname already exists.')

    # Hash user's password
    hashed_password = bcrypt.generate_password_hash(data['password'])
    # Create new user
    new_moderator = Moderator(moderatorname=data['moderatorname'], firstname=data['firstname'], lastname=data['lastname'], email=data['email'], password=hashed_password, moderatorKey=data['moderatorKey'])

    # Add new user to db
    session.add(new_moderator)
    session.commit()

    return Response(status=200, response='New moderator was successfully created!')


@moderator.route('/api/v1/updateArticle/<int:ArticleId>', methods=['GET'])
@auth.login_required
def get_updatedArticle(ArticleId):
    # Check if supplied ArticleId correct
    if int(ArticleId) < 1:
        return Response(status=400, response='Invalid ArticleId supplied')
    # Check if aricle's versions exists
    db_all = session.query(UpdatedArticle).filter_by(article_id=ArticleId).all()
    if not db_all:
        return Response(status=404, response='A articles versions with provided ID was not found')
    # Return user data
    updatedArticle_data = {}
    i = 0
    for db_user in db_all:
        updatedArticle_data[i] = {'updated_article_id': db_user.updated_article_id, 'article_id': db_user.article_id,
                                  'user_id': db_user.user_id, 'moderator_id': db_user.moderator_id,
                                  'state_id': db_user.state_id, 'article_body': db_user.article_body,
                                  'date': db_user.date}
        i += 1
    return jsonify({"updatedArticle": updatedArticle_data})


# Delete article by id
@moderator.route('/api/v1/updateArticle', methods=['PUT'])
@auth.login_required
def put_article():
    data = request.get_json()
    if auth.username() != session.query(Moderator).filter_by(moderatorKey=data['ModeratorKey']).first().moderatorname:
       return Response(status=403, response='Access denied')

    # Check if supplied userId correct
    if data['ArticleId'] < 1:
        return Response(status=404, response='Invalid ArticleId supplied')

    # Check if user exists
    db_user = session.query(Moderator).filter_by(moderatorKey=data['ModeratorKey']).first()
    if not db_user:
        return Response(status=400, response='A bad moderator key supplied')

    db_user2 = session.query(UpdatedArticle).filter_by(updated_article_id=data['ArticleId']).first()
    if not db_user2:
        return Response(status=402, response='A bad article id was supplied')

    db_user2.state = "accepted"
    session.commit()

    return Response(status=200, response='Article was asccepted successfully')