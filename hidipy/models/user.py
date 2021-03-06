from flask_security import UserMixin, RoleMixin
from flask_security.utils import encrypt_password
from .meta import db


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id'), index=True),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'), index=True)
)


class User(db.Model, UserMixin):
    """ User Representation
    Relationships:
    -   A user can have potentially many posts (Specified on `Post` class)
    -   Can comment on many posts. (Specified on `Comment` class)
    -   Has potentially many roles.
    """

    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), index=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(), nullable=True)
    active = db.Column(db.Boolean(), default=False, nullable=False)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    fob_id = db.Column(db.String(), unique=True)

    def __init__(self, username, password, roles=None, active=None, confirmed_at=None):
        self.username = username
        self.password = encrypt_password(password)
        if roles:
            self.roles = roles
        self.active = active
        self.confirmed_at = confirmed_at

    def __repr__(self):
        return self.username


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, index=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
