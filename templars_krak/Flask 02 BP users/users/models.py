from uuid import uuid4
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db
from app import login


# intermediate table
user_role = db.Table('user_roles',
    db.Column('user_id', db.String(36), db.ForeignKey('user.id')),
    db.Column('role_id', db.String(36), db.ForeignKey('role.id')),
    db.UniqueConstraint('user_id', 'role_id', name="unique_constraint"),
)

class Role(db.Model):
    """Roles are used for permissions"""
    id = db.Column(db.String(36), primary_key=True, default=str(uuid4()))
    name = db.Column(db.String(64), nullable=False, unique=True, index=True)

    def __repr__(self) -> str:
        return f"<Role: {self.name}>"

    @classmethod
    def get_name(cls, name):
        role = Role.query.filter_by(name=name).first()
        if role is None:
            raise Exception(f"Role '{name}' does not exists.")
        return role


class User(UserMixin, db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid4()))
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    last_seen = db.Column(db.DateTime, default=datetime.utcnow())


    roles = db.relationship(
        'Role', secondary=user_role,
        backref=db.backref('users', lazy='dynamic'), lazy='dynamic'
    )

    def __repr__(self):
        return f"<User: {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def add_role(self, role: str):
        if self.has_role(role):
            return
        role = Role.get_name(role)
        self.roles.append(role)

    def remove_role(self, role: str):
        role = Role.get_name(role)
        self.roles.remove(role)

    def has_role(self, role: str):
        role = Role.get_name(role)
        if role in self.roles.all():
            return True
        else:
            return False



@login.user_loader
def load_user(id):
    return User.query.get(str(id))
