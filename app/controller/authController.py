from flask import Blueprint, request, jsonify
from app.service.authService import registerUser, authenticate
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from app.repository.userRepository import getUserById

authBp = Blueprint('auth', __name__, url_prefix='/auth')

@authBp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = data.get("user", None)
    password = data.get("password", None)
    email = data.get("email", None)

    if not(user and password and email):
        return jsonify(
            {
                "message": "All fields are required",
            }
        ), 400
    try:
        user = registerUser(user, email, password)
        return jsonify(
            {
                "message": "User created successfully",
                "user": user.toDict()
            }
        ), 201
    except ValueError as e:
        return jsonify({
            "message": str(e),
        }), 409
    except Exception as e:
        return jsonify({
            "message": str(e),
        }), 500

@authBp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email", None)
    password = data.get("password", None)
    if not(email and password):
        return jsonify({
            "message": "All fields are required",
        }), 400
    user = authenticate(email, password)
    if not user:
        return jsonify({
            "message": "Invalid credentials",
        }), 401

    additionalClaims = {
        "name": user.name,
    }
    access_token = create_access_token(identity=user.id, additional_claims=additionalClaims)
    return jsonify(
        {
            "message": "Login successful",
            "access_token": access_token,
        }
    ), 200

@authBp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    userId = get_jwt_identity()
    user = getUserById(userId)
    if not user:
        return jsonify({
            "message": "User does not exist",
        }), 404
    return jsonify(
        {
            "message": "Profile Found",
            "user": user.toDict()
        }
    ), 200