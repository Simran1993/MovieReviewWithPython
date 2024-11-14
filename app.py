from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

# Import blueprints
from routes.auth import auth_bp
from routes.movie import movie_bp
from routes.review import review_bp

# Import models and services
from models.user import UserModel
from models.review import ReviewModel
from factories.movie_provider_factory import MovieProviderFactory

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = '11dsd215e16e'
    app.config["MONGO_URI"] = "mongodb+srv://simrn204:Ottawa2004@simran1993.rc2c4.mongodb.net/MovieTable"
    
    # Initialize MongoDB
    mongo = PyMongo(app)
    
    # Initialize models and services
    app.user_model = UserModel(mongo.db)
    app.review_model = ReviewModel(mongo.db)
    app.movie_provider = MovieProviderFactory.get_provider(
        'omdb',
        'b24150c3'
    )
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(movie_bp)
    app.register_blueprint(review_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
