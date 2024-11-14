from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from routes.auth import login_required
from flask import current_app
import requests


movie_bp = Blueprint('movie', __name__)

MOVIE_API_URL = 'http://www.omdbapi.com/?apikey=b24150c3'

@movie_bp.route('/')
def index():
    # Fetch random movies (or use a fixed query as placeholder)
    response = requests.get(f'{MOVIE_API_URL}&s=batman')  # Replace "batman" with your placeholder
    movies = response.json().get('Search', []) if response.status_code == 200 else []
    return render_template('index.html', movies=movies)


@movie_bp.route('/search', methods=['POST'])
def search_movie():
    search_query = request.form.get('query', '').strip()
    if not search_query:
        flash('Please enter a movie name to search!', 'error')
        return redirect(url_for('movie.index'))
    return redirect(url_for('movie.search_results', query=search_query))

@movie_bp.route('/search_results', methods=['GET'])
def search_results():
    search_query = request.args.get('query', '')
    response = requests.get(f'{MOVIE_API_URL}&s={search_query}')
    movies = response.json().get('Search', []) if response.status_code == 200 else []
    return render_template('search_results.html', movies=movies, query=search_query)


@movie_bp.route('/movie/<movie_id>')
def movie_details(movie_id):
    movie_data = current_app.movie_provider.get_movie_details(movie_id)
    reviews = current_app.review_model.find_by_movie(movie_id)
    return render_template('movie_details.html', movie=movie_data, reviews=reviews)
