from werkzeug.security import generate_password_hash, check_password_hash
from .base import BaseModel

class UserModel(BaseModel):
    def get_collection(self):
        return self.db.users

    def create_user(self, username, email, password):
        user_data = {
            'username': username,
            'email': email,
            'password': generate_password_hash(password)
        }
        return self.create(user_data)

    def find_by_username(self, username):
        return self.collection.find_one({'username': username})

    def verify_password(self, user, password):
        return check_password_hash(user['password'], password)
