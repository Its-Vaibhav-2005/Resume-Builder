from app.model.DataBaseConfig import db
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    passwordHash = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def setPassword(self, password):
        self.passwordHash = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.passwordHash, password)

    def toDict(self):
        return {
            "id":self.id,
            "name":self.name,
            "email":self.email,
            "createdAt":self.createdAt.isoformat(),
        }