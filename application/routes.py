from flask.templating import render_template
from application import app, db
from application.models import Game
from datetime import datetime, timedelta
from flask import redirect, url_for, request
from .models import Game, Review, GameForm, ReviewForm




@app.route('/home', methods=['GET', 'POST'])
def home():
    games = Game.query.all()
    return render_template("main.html", games=games)


