from scraper import scraper
from scraper.models import MovieManager

def main():
  s = scraper.Scraper('http://www.filmsofafrica.com/Ethiopia/Adwa.htm')
  print('======== Created Scraper @ Ethiopia - Adwa ========')
  print('======== Saving Next 10 Movies ========')
  for i in range(10):
    movie = s.movie
    movie.save()
    print(movie)
    s = s.next
  print('======== DONE ========')

  s = scraper.Scraper('http://www.filmsofafrica.com/Ethiopia/Adwa.htm')
  print('======== Created Scraper @ Ethiopia - Adwa ========')
  print('======== Saving Previous 4 Movies ========')
  for i in range(4):
    movie = s.movie
    movie.save()
    print(movie)
    s = s.previous
  print('======== DONE ========')

  m = MovieManager()
  all_movies = m.get_all()
  print('NUMBER OF MOVIES: {num}'.format(num=len(all_movies)))

  print('======== Printing Movie UID=8 ========')
  print(m.get(uid=8))
  print('======== DONE ========')

  print('======== Printing Movie Name=Journey to Lasta ========')
  print(m.get(name='Journey To Lasta'))
  print('======== DONE ========')


if __name__ == '__main__':
  main()