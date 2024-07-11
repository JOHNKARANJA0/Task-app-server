#!/usr/bin/env python3

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    _password_hash = db.Column('password_hash', db.String(128), nullable=False)
    
    tasks = db.relationship('Task', backref='user', lazy=True)
    assignments = db.relationship('Assignment', backref='user', lazy=True)
    
    serialize_rules = ('-tasks.user', '-assignments.user', '-password_hash')

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email, "Invalid email format"
        return email
    
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


    def __repr__(self):
        return f"<User {self.name}>"

class Task(db.Model, SerializerMixin):
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    assignments = db.relationship('Assignment', backref='task', lazy=True)
    
    serialize_rules = ('-user.tasks', '-assignments.task', '-assignments.user')

    def __repr__(self):
        return f"<Task {self.title}>"

class Assignment(db.Model, SerializerMixin):
    __tablename__ = 'assignments'
    
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    
    serialize_rules = ('-task.assignments', '-user.assignments', '-task.user', '-user.tasks')

    def __repr__(self):
        return f"<Assignment {self.id} - Task {self.task_id} - User {self.user_id} - Status {self.status}>"