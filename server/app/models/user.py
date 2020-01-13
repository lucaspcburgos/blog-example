from config.database import DB
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(DB.Model):
    id = DB.Column(UUID(as_uuid=True), primary_key=True, nullable=False, unique=True)
    email = DB.Column(DB.String(128), nullable=False, unique=True)
    name = DB.Column(DB.String(128), nullable=False)
    pic = DB.Column(DB.String(256), nullable=False)

    def __init__(self, facebook_id, email, name, pic):
        self.id = uuid.uuid4()
        self.email = email
        self.name = name
        self.pic = pic

    def create(self):
        DB.session.add(self)
        DB.session.commit()
