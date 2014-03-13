import requests
from lxml import html
from urlparse import urljoin

import utils
import settings as s
from models import Movie
from exceptions import ScraperException


class Scraper(object):
	def __init__(self, url):
		self.url = url
		self._page = requests.get(self.url)
		self._tree = html.fromstring(self._page.text)

	@property
	def movie(self):
		try:
			director = utils.get_text(self._tree, s.XPATH_DIRECTOR)
			genre = utils.get_text(self._tree, s.XPATH_GENRE)
			length = utils.get_text(self._tree, s.XPATH_LENGTH)
		except IndexError:
			try:
				director = utils.get_text(self._tree, s.XPATH_DIRECTOR_2)
				genre = utils.get_text(self._tree, s.XPATH_GENRE_2)
				length = utils.get_text(self._tree, s.XPATH_LENGTH_2)
			except IndexError:
				raise ScraperException()

		name_desc = utils.get_text(self._tree, s.XPATH_NAME_DESC).splitlines()
		cleaned_name_desc = utils.clean_name_and_desc(name_desc)
		name = cleaned_name_desc[0]
		desc = ''.join(cleaned_name_desc[1:])

		return Movie(name=name, desc=desc, director=director, genre=genre, length=length)

	@property
	def next(self):
		try:
			url = urljoin(self.url, self._tree.xpath(s.XPATH_NEXT)[0].get('href'))
		except IndexError:
			try:
				url = urljoin(self.url, self._tree.xpath(s.XPATH_NEXT_2)[0].get('href'))
			except IndexError:
				raise ScraperException()
		return Scraper(url)

	@property
	def previous(self):
		try:
			url = urljoin(self.url, self._tree.xpath(s.XPATH_PREVIOUS)[0].get('href'))
		except IndexError:
			try:
				url = urljoin(self.url, self._tree.xpath(s.XPATH_PREVIOUS_2)[0].get('href'))
			except IndexError:
				raise ScraperException()
		return Scraper(url)

	def __repr__(self):
		return "Scraper @ {url}".format(url=self.url)
