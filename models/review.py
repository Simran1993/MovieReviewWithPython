from .base import BaseModel
from datetime import datetime

class ReviewModel(BaseModel):
    def get_collection(self):
        return self.db.reviews

    def create_review(self, movie_id, movie_title,movie_poster , user_id, username, rating, comment):
        review_data = {
            'movie_id': movie_id,
            'movie_title': movie_title,
            'movie_poster': movie_poster ,
            'user_id': user_id,
            'username': username,
            'rating': rating,
            'comment': comment,
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow()
        }
        return self.create(review_data)

    def update_review(self, review_id, rating, comment):
        update_data = {
            'rating': rating,
            'comment': comment,
            'updated_at': datetime.utcnow()
        }
        return self.update(review_id, update_data)

    def find_by_movie(self, movie_id):
        return self.collection.find({'movie_id': movie_id})

    def find_by_user(self, user_id):
        return self.collection.find({'user_id': user_id})

    def get_all_reviews(self):
        return list(self.collection.find())  # Convert the cursor to a list for easy iteration
