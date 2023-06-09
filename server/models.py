from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from flask_login import UserMixin
from config import bcrypt, db
import re

class User(db.Model, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    _password_hash = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    access_code = db.Column(db.Integer)
    admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))

    # @validates('username')
    # def validate_username(self, key, username):
    #     usernames = [user.username for user in User.query.all()]
    #     if not username:
    #         raise ValueError('Username must be provided')
    #     elif username in usernames:
    #         raise ValueError('This username is already registered to an account - please log in.')
    #     return username

    @validates('password')
    def validate_password(self, key, password):
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long.')
        elif not re.search('[!@#$%^&*]', password):
            raise ValueError('Password must contain at least one special character.')
        return password

class PortfolioGrid(db.Model, SerializerMixin):
    __tablename__ = 'portfolio_grids'

    id = db.Column(db.Integer, primary_key=True)
    highlight_image = db.Column(db.String)
    title = db.Column(db.String)
    preview = db.Column(db.String)

    project_details = db.relationship('ProjectDetail', back_populates='portfolio_grid')

    serialize_rules = ('-project_details',)

class ProjectDetail(db.Model, SerializerMixin):
    __tablename__ = 'project_details'

    id = db.Column(db.Integer, primary_key=True)
    grid_id = db.Column(db.Integer, db.ForeignKey('portfolio_grids.id'))
    title = db.Column(db.String)
    description = db.Column(db.String)
    images = db.Column(db.String)

    portfolio_grid = db.relationship('PortfolioGrid', back_populates='project_details')

    serialize_rules = ('-portfolio_grid',)