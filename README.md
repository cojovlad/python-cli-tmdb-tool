# python-cli-tmdb-tool
A simple CLI app that fetches movie data from The Movie Database (TMDB) API, parses JSON responses, and displays the results in the terminal. This project demonstrates API integration, JSON handling, and building interactive command line tools.

To use the app you have to get an API-key from https://developer.themoviedb.org/docs/getting-started. After that, you have to create a .env file in your application with the variable name TMDB_API_KEY='(your api kei)'

 python main.py --type popular
 python main.py --type playing
 python main.py --type top
 python main.py --type upcoming

 The above are commands used to get data from the api.
