from application import db
from application.models import Game, Review
from datetime import datetime

db.drop_all()
db.create_all()

game2 = Game(title = "Destiny" , genre = "First Person Shooter", developer = "Bungie")
db.session.add(game2)
db.session.commit()
review2 = Review(name = "Greg", content = "Amazing game, loved the looting part and the multiplayer aspec", time = datetime.today(), game_id = game1.id)
db.session.add(review2)
db.session.commit()