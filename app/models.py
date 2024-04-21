from . import db

class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String(500))
    model_output = db.Column(db.String(500))

    def __repr__(self):
        return '<UserData {}>'.format(self.user_input)
