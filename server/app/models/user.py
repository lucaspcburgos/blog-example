from config.database import DB
from sqlalchemy.dialects.postgresql import UUID
import uuid
from werkzeug.security import generate_password_hash, check_password_hash


class User(DB.Model):
    id = DB.Column(UUID(as_uuid=True), primary_key=True, nullable=False, unique=True)
    email = DB.Column(DB.String(128), nullable=False, unique=True)
    username = DB.Column(DB.String(128), nullable=False)
    password = DB.Column(DB.String(256), nullable=False)

    def __init__(self, email, username, password):
        self.id = uuid.uuid4()
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)

    def create(self):
        DB.session.add(self)
        DB.session.commit()
