from config.database import DB
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(DB.Model):
    id = DB.Column(UUID(as_uuid=True), primary_key=True, nullable=False, unique=True)
    facebookId = DB.Column(DB.String(64), nullable=False, unique=True)
    facebookToken = DB.Column(DB.String(64), nullable=False, unique=True)
    email = DB.Column(DB.String(128), nullable=False, unique=True)
    name = DB.Column(DB.String(128), nullable=False)
    pic = DB.Column(DB.String(256), nullable=False)

    def __init__(self, facebook_id, email, name, pic, facebook_token):
        self.id = uuid.uuid4()
        self.facebookId = facebook_id
        self.email = email
        self.name = name
        self.pic = pic
        self.facebookToken = facebook_token

    def create(self):
        DB.session.add(self)
        DB.session.commit()
