from cutegirls.downloader import Downloader

import os

class Post:
	""" Booru post. """
	def __init__(self, downloader, **kwargs):
		self._dl = downloader
		
		self.id = kwargs.get("id")
		self.file_url = kwargs.get("file_url")
		self.sample_url = kwargs.get("sample_url")
		self.preview_url = kwargs.get("preview_url")
		
		_, self.file_name, self.file_ext = self._split_url(self.file_url)
		_, self.sample_name, self.sample_ext = self._split_url(self.sample_url)
		_, self.preview_name, self.preview_ext = self._split_url(self.preview_url)
		
		self.tags = kwargs.get("tags")
		self.date = kwargs.get("date")
		self.width = kwargs.get("width")
		self.height = kwargs.get("height")
		self.score = kwargs.get("score")
		self.rating = kwargs.get("rating")
		self.md5 = kwargs.get("md5")
		self.source = kwargs.get("source")
	
	def __repr__(self):
		return "<Post id={}>".format(self.id)
	
	@property
	def rating_long(self):
		ratings = {
			"s": "safe",
			"q": "questionable",
			"e": "explicit"
		}
		return ratings[self.rating]
	
	def _split_url(self, url):
		base, file = url.rsplit("/", 1)
		name, ext = file.rsplit(".", 1)
		return base, name, ext
	
	def save_file(self, dir=".", name=None):
		""" Downloads and saves the file. """
		if name is None:
			name = self.file_name + "." + self.file_ext
		self._dl.save_content(self.file_url, os.path.join(dir, name), md5=self.md5)
	
	def save_sample(self, dir=".", name=None):
		""" Downloads and saves the file sample. """
		if name is None:
			name = self.sample_name + "." + self.sample_ext
		self._dl.save_content(self.sample_url, os.path.join(dir, name))
	
	def save_preview(self, dir=".", name=None):
		""" Downloads and saves the file preview. """
		if name is None:
			name = self.preview_name + "." + self.preview_ext
		self._dl.save_content(self.preview_url, os.path.join(dir, name))

class SearchResults:
	""" Booru search results. """
	def __init__(self, **kwargs):
		self.tags = kwargs.get("tags", [])
		self.page = kwargs.get("page", 0)
		self.limit = kwargs.get("limit", 0)
		self.total = kwargs.get("total", 0)
		self.posts = kwargs.get("posts", [])
	
	def __repr__(self):
		return "<SearchResult tags={}>".format(self.tags)
	
	def __next__(self):
		pass

class Booru:
	""" Superclass for booru site implementations. """
	def __init__(self, name="Booru", url=""):
		self.name = name
		self.url = url
		
		self._dl = Downloader()
		self.results = SearchResults(
			posts=[],
			tags=[],
			page=0,
			limit=0,
			total=0
		)
	
	def __repr__(self):
		return "<%s>".format(self.name)
	
	def _new_results(self, **kwargs):
		self.results = SearchResults(posts=[], **kwargs)
	
	def _add_post(self, **kwargs):
		self.results.posts.append(Post(self._dl, **kwargs))
	
	def _search(tags, limit, page):
		raise NotImplemented()
	
	def search(self, tags=[], limit=50, page=0):
		""" Search for posts. """
		self._search(tags, limit, page)
		return self.results
	
	def posts(self, tags=[], page=0):
		""" Search for posts using a generator. """
		while True:
			res = self.search(tags=tags, page=page)
			if not res.posts:
				break
			for post in res.posts:
				yield post
			page += 1
