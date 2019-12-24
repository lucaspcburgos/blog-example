from config.database import DB


class Test(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.Text)
