from main import resumeBuilder
from app.model.DataBaseConfig import db
app=resumeBuilder()
with app.app_context():
    db.create_all()
    print('tables created')