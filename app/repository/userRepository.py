from app.model.Models import User
from app.model.DataBaseConfig import db

def getUserByEmail(email):
    return User.query.filter_by(email=email).first()

def getUserById(id):
    return User.query.filter_by(id=id).first()

def createUser(name, email, password):
    user = User(name=name, email=email)
    user.setPassword(password)
    db.session.add(user)
    db.session.commit()
    return user