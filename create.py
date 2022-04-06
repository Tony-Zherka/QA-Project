from application import db
from application.models import Game, Review
from datetime import datetime

db.drop_all()
db.create_all()

game1 = Game(title = "Destiny 2" , genre = "First Person Shooter", developer = "Bungie")
db.session.add(game1)
db.session.commit()
review1 = Review(name = "Greg", content = "Amazing game, loved the looting part and the multiplayer aspec", time = datetime.today(), game_id = game1.id)
db.session.add(review1)
db.session.commit()