from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
from functools import wraps


# Import our models and services
from models.user import UserModel
from models.review import ReviewModel
from factories.movie_provider_factory import MovieProviderFactory

load_dotenv()

app = Flask(__name__)
app.secret_key = '11dsd215e16e'
app.config["MONGO_URI"] = "mongodb+srv://simrn204:Ottawa2004@simran1993.rc2c4.mongodb.net/MovieTable"
try:
    mongo = PyMongo(app)
    print("MongoDB connected:", mongo.db)
except Exception as e:
    print("Failed to connect to MongoDB:", e)
    mongo = None


if mongo.db is not None:  # Explicitly check if the database object is not None
    from models.user import UserModel
    from models.review import ReviewModel
    from factories.movie_provider_factory import MovieProviderFactory

    user_model = UserModel(mongo.db)
    review_model = ReviewModel(mongo.db)
    movie_provider = MovieProviderFactory.get_provider(
    'omdb',  # Specify the provider type
    'b24150c3'  # Your OMDB API Key
)
else:
    print("Error: MongoDB is not initialized. Models cannot be created.")



@app.route('/')
def index():
    return render_template('index.html')


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login first', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        existing_user = user_model.find_by_username(username)
        
        if existing_user is None:
            user_model.create_user(
                username=username,
                email=request.form['email'],
                password=request.form['password']
            )
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        
        flash('Username already exists!', 'error')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = user_model.find_by_username(request.form['username'])
        
        if user and user_model.verify_password(user, request.form['password']):
            session['user_id'] = str(user['_id'])
            session['username'] = user['username']
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
            
        flash('Invalid username/password combination', 'error')
    return render_template('login.html')

@app.route('/search', methods=['POST'])
@login_required
def search_movie():
    movie_title = request.form.get('movie_title')
    movie_data = movie_provider.search_movie(movie_title)
    
    if movie_data.get('Response') == 'True':
        return render_template('movie_details.html', movie=movie_data)
    else:
        flash('Movie not found!', 'error')
        return redirect(url_for('index'))

@app.route('/movie/<movie_id>')
@login_required
def movie_details(movie_id):
    movie_data = movie_provider.get_movie_details(movie_id)
    reviews = review_model.find_by_movie(movie_id)
    return render_template('movie_details.html', movie=movie_data, reviews=reviews)

@app.route('/review/<movie_id>', methods=['POST'])
@login_required
def add_review(movie_id):
    review_model.create_review(
        movie_id=movie_id,
        user_id=session['user_id'],
        username=session['username'],
        rating=int(request.form.get('rating')),
        comment=request.form.get('comment')
    )
    flash('Review added successfully!', 'success')
    return redirect(url_for('movie_details', movie_id=movie_id))

@app.route('/review/edit/<review_id>', methods=['GET', 'POST'])
@login_required
def edit_review(review_id):
    review = review_model.find_by_id(review_id)
    
    if review['user_id'] != session['user_id']:
        flash('You can only edit your own reviews!', 'error')
        return redirect(url_for('movie_details', movie_id=review['movie_id']))
    
    if request.method == 'POST':
        review_model.update_review(
            review_id=review_id,
            rating=int(request.form.get('rating')),
            comment=request.form.get('comment')
        )
        flash('Review updated successfully!', 'success')
        return redirect(url_for('movie_details', movie_id=review['movie_id']))
    
    return render_template('edit_review.html', review=review)

@app.route('/review/delete/<review_id>', methods=['POST'])
@login_required
def delete_review(review_id):
    review = review_model.find_by_id(review_id)
    
    # Check if the review exists and if the logged-in user is the owner of the review
    if review is None:
        flash('Review not found!', 'error')
        return redirect(url_for('index'))
    
    if review['user_id'] != session['user_id']:
        flash('You can only delete your own reviews!', 'error')
        return redirect(url_for('movie_details', movie_id=review['movie_id']))

    # Proceed to delete the review
    review_model.delete_review(review_id)
    flash('Review deleted successfully!', 'success')
    return redirect(url_for('movie_details', movie_id=review['movie_id']))

@app.route('/logout')
@login_required  # Optional: only allow logged-in users to log out
def logout():
    # Clear the session to log out the user
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login')) 

if __name__ == '__main__':
    app.run(debug=True)
