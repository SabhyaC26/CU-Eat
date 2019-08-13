from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    netid = db.Column(db.String, nullable=False)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.netid = kwargs.get('netid', '')

    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'netid' : self.netid,
        }

class Food(db.Model):
    __tablename__ = 'food'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# TODO:
class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    # have a list of dining halls
    # have many menu entries for one day (best option for now!)


class Assignment(db.Model):
    __tablename__ = 'assignment'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    due_date = db.Column(db.Integer, nullable=False)
    class_id = db.Column(db.Intege, db.ForeignKey('class.id'), nullable=False)

    def __init__(self, **kwargs):
        self.description = kwargs.get('description', '')
        self.due_date = kwargs.get('due_date', 0)
        self.class_id = kwargs.get('class_id')

    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'due_date': self.due_date,
        }
