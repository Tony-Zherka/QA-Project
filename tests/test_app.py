from flask import url_for
from flask_testing import TestCase
from application.models import Game, Review, GameForm, ReviewForm
from application import app, db

class  TestApp(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            DEBUG = True,
            WTF_CSRF_ENABLED = False
        )
        return app
        

    def setUp(self):
        db.create_all()
        test_review1 = Review(name="test_name", content="test_content", game_id=1)
        test_game1 = Game(title="test_game", developer="test_developer", genre="test_genre")
        db.session.add(test_game1)
        db.session.add(test_review1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestRead(TestApp):
    def test_read_game(self):
        response = self.client.get(url_for('read_game'))
        assert 'test_game'in response.data.decode()
        assert 'test_developer'in response.data.decode()
        assert 'test_genre'in response.data.decode()
        
class TestCreate(TestApp):
    def test_create_game(self):
        response = self.client.post(url_for('create_game'), data=dict(title="test_game", developer="test_developer", genre="test_genre"), follow_redirects=True)
        assert 'Enter A Game'in response.data.decode()
        

class TestUpdate(TestApp):
    def test_update_game(self):
        response = self.client.post(url_for('update_game', id=1), data=dict(title="test_game", developer="test_developer", genre="test_genre"), follow_redirects=True)
        assert 'test_game'in response.data.decode()
        assert 'test_developer'in response.data.decode()
        assert 'test_genre'in response.data.decode()

class TestDelete(TestApp):
    def test_delete_review(self):
        response = self.client.get(
            url_for('delete_review', id=1),   
            follow_redirects=True   
        )
        response1 = self.client.get(
            url_for('delete_game', id=1),   
            follow_redirects=True   
        )
        assert "Review List" in response.data.decode()
        assert "Games List" in response1.data.decode()

class TestCreateReview(TestApp):
    def test_create_review(self):
        response = self.client.post(url_for('create_review'), data=dict(name="test_name", content="test_content", game_id=1), follow_redirects=True)
        assert 'Enter A Review'in response.data.decode()

class TestReadReview(TestApp):
    def test_read_review(self):
        response = self.client.get(url_for('read_review'))
        assert 'test_name'in response.data.decode()
        assert 'test_content'in response.data.decode()
        assert '1'in response.data.decode()

class TestUpdateReview(TestApp):
    def test_update_review(self):
        response = self.client.post(url_for('update_review', id=1), data=dict(name="test_name", content="test_content", game_id=1), follow_redirects=True)
        assert 'test_name'in response.data.decode()
        assert 'test_content'in response.data.decode()
        assert '1'in response.data.decode()

class TestDeleteReview(TestApp):
    def test_delete_review(self):
        response = self.client.get(
            url_for('delete_review', id=1),   
            follow_redirects=True   
        )
        response1 = self.client.get(
            url_for('delete_game', id=1),   
            follow_redirects=True   
        )
        assert "Review List" in response.data.decode()
        assert "Games List" in response1.data.decode()
        




class TestViews(TestApp):

    def test_home_page(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page1(self):
        response = self.client.get(url_for('home1'))
        self.assertEqual(response.status_code, 200)

    def test_create_game(self):
        response = self.client.get(url_for('create_game'))
        self.assertEqual(response.status_code, 200)
      
    def test_update_game(self):
        response = self.client.get(url_for('update_game', id=1))
        self.assertEqual(response.status_code, 200)

    def test_create_review(self):
        response = self.client.get(url_for('create_review', id=1))
        self.assertEqual(response.status_code, 200)
        
    def test_read_review(self):
        response = self.client.get(url_for('read_review', id=1))
        self.assertEqual(response.status_code, 200)

    def test_update_review(self):
        response = self.client.get(url_for('update_review', id=1))
        self.assertEqual(response.status_code, 200)

       
      

