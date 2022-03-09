from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

groups = db.Table('groups',
    db.Column('group_id', db.Integer, db.ForeignKey('group.id'), primary_key=True),
    db.Column('contact_id', db.Integer, db.ForeignKey('contact.id'), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(80), unique=False, nullable=False)
    phone = db.Column(db.String(80), unique=False, nullable=False)
    groups = db.relationship('Group', secondary=groups, lazy='subquery',
        backref=db.backref('contact', lazy=True))

    def __repr__(self):
        return '<Contact %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email":self.email,
            "address": self.address,
            "phone": self.phone
            # do not serialize the password, its a security breach
        }



class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    contacts = db.relationship('Contact', secondary=groups, lazy='subquery',
        backref=db.backref('group', lazy=True))
    

    def __repr__(self):
        return '<Group %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

