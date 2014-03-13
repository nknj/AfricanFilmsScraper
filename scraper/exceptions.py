class ScraperException(Exception):
    def __init__(self):
      Exception.__init__(self, 'HTML Format Error, ' +\
          'The HTML structure of this page is not recognised by this scraper')