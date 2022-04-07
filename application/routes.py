from flask.templating import render_template
from application import app, db
from application.models import Game
from datetime import datetime, timedelta
from flask import redirect, url_for, request
from .models import Game, Review, GameForm, ReviewForm



@app.route('/', methods=['GET', 'POST'])
def home1():
    return render_template('home.html',)
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html',)



@app.route('/create_game', methods=['GET', 'POST'])
def create_game():
    form = GameForm()
    if form.validate_on_submit():
        new_game = Game(title=form.title.data, developer=form.developer.data, genre=form.genre.data)
        db.session.add(new_game)
        db.session.commit()
        return redirect(url_for('create_game'))
    return render_template('addgame.html', form=form)

@app.route('/read_game')
def read_game():
    all_games = Game.query.all()
    return render_template('gamelist.html', all_games=all_games)

    
@app.route('/update_game/<int:id>',methods = ['GET','POST'])
def update_game(id):
    form = GameForm()
    
    if request.method == 'POST':
        update_game = Game.query.filter_by(id=id).first()
        if update_game: 
            update_game.title = request.form['title']
            update_game.genre = request.form['genre']
            update_game.developer = request.form['developer']
            db.session.commit()
            return redirect(url_for('read_game'))
        return f"game with id = {id} Does not exist"
    else:
        return render_template('update_game.html', form=form, id=id)
           
    
@app.route('/delete_game/<int:id>', methods=['GET', 'POST'])
def delete_game(id):
    game = Game.query.filter_by(id=id).first()
    if game:
        db.session.delete(game)
        db.session.commit()
        return redirect(url_for('read_game'))
    return render_template('gamelist.html', id=id)
    
@app.route('/create_review', methods=['GET', 'POST'])
def create_review():
    form = ReviewForm()
    if form.validate_on_submit():
        new_review = Review(name=form.name.data, content=form.content.data, time=datetime.now())
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('create_review'))
    return render_template('addreview.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')