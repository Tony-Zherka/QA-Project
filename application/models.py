from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(40), nullable=False)
    developer = db.Column(db.String(50), nullable=False)
    reviews = db.relationship('Review', backref='game')

class GameForm(FlaskForm):
    title = StringField('Enter the game title')
    genre = StringField('Enter the game genre')
    developer = StringField('Enter the game developers')
    submit = SubmitField('submit')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(4000), nullable=False)
    time = db.Column(db.DateTime)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)


class ReviewForm(FlaskForm):
    name = StringField('Enter your name')
    content = StringField('Enter your review')
    submit = SubmitField('submit')