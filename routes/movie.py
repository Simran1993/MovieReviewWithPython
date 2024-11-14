from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from routes.auth import login_required
from flask import current_app
import requests


movie_bp = Blueprint('movie', __name__)

MOVIE_API_URL = 'http://www.omdbapi.com/?apikey=b24150c3'

@movie_bp.route('/')
@login_required
def index():
    return render_template('index.html')

@movie_bp.route('/search', methods=['GET'])
@login_required
def search_movie():
    # Get search query from URL parameters, default to 'Shin Chan'
    search_query = request.args.get('query', 'Shin Chan')  
    response = requests.get(f'{MOVIE_API_URL}&s={search_query}')
    
    # Parse API response and fetch list of movies
    if response.status_code == 200:
        movies = response.json().get('Search', [])
        if movies:
            return render_template('search_results.html', movies=movies)
        else:
            flash('No related movies found!', 'error')
    else:
        flash('Error fetching data from the movie API!', 'error')
    
    return redirect(url_for('movie.index'))



@movie_bp.route('/movie/<movie_id>')
def movie_details(movie_id):
    movie_data = current_app.movie_provider.get_movie_details(movie_id)
    reviews = current_app.review_model.find_by_movie(movie_id)
    return render_template('movie_details.html', movie=movie_data, reviews=reviews)
