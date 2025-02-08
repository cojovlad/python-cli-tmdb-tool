import argparse
import requests
import sys
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the TMDB API key from the environment variables
api_key = os.getenv('TMDB_API_KEY')
if not api_key:
    print("API key not found. Please set TMDB_API_KEY in the .env file.")
    sys.exit(1)


# Function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Fetch movie data from TMDB.")
    parser.add_argument('--type', required=True, choices=['playing', 'popular', 'top', 'upcoming'],
                        help='Type of movies to display: "playing", "popular", "top", or "upcoming".')
    return parser.parse_args()


# Function to build the API URL based on movie type
def get_api_url(movie_type, api_key):
    base_url = "https://api.themoviedb.org/3/movie/"
    endpoints = {
        'playing': 'now_playing',
        'popular': 'popular',
        'top': 'top_rated',
        'upcoming': 'upcoming'
    }
    # Returns the full API URL with the correct endpoint and API key
    return f"{base_url}{endpoints[movie_type]}?api_key={api_key}&language=en-US&page=1"


# Function to fetch movie data from TMDB API
def fetch_movies(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


# Function to display movie titles from the API response
def display_movies(movie_data):
    movies = movie_data.get('results', [])
    if not movies:
        print("No movies found.")
        return

    # Loops through the movies and prints their titles
    for idx, movie in enumerate(movies, start=1):
        print(f"{idx}. {movie.get('title')}")


# Main function to tie everything together
def main():
    args = parse_arguments()
    api_url = get_api_url(args.type, api_key)

    movie_data = fetch_movies(api_url)
    display_movies(movie_data)


# Entry point of the script
if __name__ == "__main__":
    main()

# Example usage:
# python main.py --type popular
# python main.py --type playing
# python main.py --type top
# python main.py --type upcoming
