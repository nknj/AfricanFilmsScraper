# Python Web scraper
This is a simple web scraper for the [Films of Africa](http://www.filmsofafrica.com/) website.

## Features
- Scrape pages for information on the name, description, director, genre and length of the movie
- Interactively move on to the next or the previous movie on the website

## Installation
1. Clone this repository into your project
2. Install requirements using the `requirements.txt` file
3. Configure your SQLAlchemy database in `settings.py`

## Usage
To run the program you need to create a `Scraper` object with a valid URL

```python
from scraper import scraper
s = scraper.Scraper('http://www.filmsofafrica.com/Ethiopia/Adwa.htm')

# The command above scrapes the given URL
# You can access the movie using the movie attribute
print(s.movie)

# To save the movie to the database use the save method
s.movie.save()

# To move to the next page, use the next property
# To move to the previous page, use the previous property
next_page = s.next
prev_page = s.prev

next_page.movie.save()
prev_page.movie.save()
```

To retrieve the movies from the database, use the `MovieManager` class

```python
from scraper.models import MovieManager
m = MovieManager()

all_movies = m.get_all()        # get all the movies in the database
m.get(uid=8)                    # get the movie with the uid: 8
m.get(name='Journey To Lasta')  # get the movie with the name: Journey To Lasta
```

## Known Issues
- This has only been tested for the sites under `http://www.filmsofafrica.com/Ethiopia/`
