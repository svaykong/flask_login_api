import json

from flask import Blueprint, request, Response

from ..models.user import User
from ..schema.user_schema import UserSchema

auth = Blueprint('auth', __name__)

# Initialize the schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)


def __make_json_response(output: dict, status: int) -> Response:
    try:
        return Response(json.dumps(output), mimetype='application/json', status=status)
    except Exception as e:
        print(f'make json response exception: {e}')


@auth.route('/login', methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        res_obj = {
            "message": "invalid header",
            "success": False
        }
        return __make_json_response(res_obj, status=400)

    # getting json request body and convert to dictionary
    payload = dict(request.json)
    username = payload.get("username")
    password = payload.get("password")

    if not (username and password):
        res_obj = {
            "message": "invalid request body",
            "success": False
        }
        return __make_json_response(res_obj, status=400)

    all_users = User.query.all()
    result = users_schema.dump(all_users)

    return __make_json_response(result, status=200)


@auth.route('/signup', methods=['POST'])
def signup():
    # create user object
    # user = User(username="johndoe", email="johndoe@email.com", pwd="123")

    # add user object to db session object
    # db_session.add(user)

    # commit to db session
    # db_session.commit()
    return 'Signup is being progress'


@auth.route('/logout', methods=['POST'])
def logout():
    return 'Logout is being progress'
