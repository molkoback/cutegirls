from .downloader import Downloader

_DEFAULT_SAVE_PATH = "."

class Post:
	""" Booru post. """
	def __init__(self, downloader, **kwargs):
		self._dl = downloader
		
		self.id = kwargs.get("id")
		self.file_url = kwargs.get("file_url")
		self.sample_url = kwargs.get("sample_url")
		self.preview_url = kwargs.get("preview_url")
		
		self.file_name, self.file_ext = self._parse_url(
			self.file_url
		)
		self.sample_name, self.sample_ext = self._parse_url(
			self.sample_url
		)
		self.preview_name, self.preview_ext = self._parse_url(
			self.preview_url
		)
		
		self.tags = kwargs.get("tags")
		self.date = kwargs.get("date")
		self.width = kwargs.get("width")
		self.height = kwargs.get("height")
		self.score = kwargs.get("score")
		self.rating = kwargs.get("rating")
		self.md5 = kwargs.get("md5")
		self.source = kwargs.get("source")
	
	def __repr__(self):
		return "<Post id=%d>" % self.id
	
	def _parse_url(self, url):
		tmp = url.rsplit("/", 1)[-1].rsplit(".", 1)
		return tmp[0], tmp[1]
	
	def save_file(self, path=_DEFAULT_SAVE_PATH):
		""" Downloads and saves the file. """
		path += ("/" + self.file_name + "." + self.file_ext)
		self._dl.save_content(self.file_url, path, md5=self.md5)
	
	def save_sample(self, path=_DEFAULT_SAVE_PATH):
		""" Downloads and saves the file sample. """
		path += ("/" + self.sample_name + "." + self.sample_ext)
		self._dl.save_content(self.sample_url, path)
	
	def save_preview(self, path=_DEFAULT_SAVE_PATH):
		""" Downloads and saves the file preview. """
		path += ("/" + self.preview_name + "." + self.preview_ext)
		self._dl.save_content(self.preview_url, path)

class SearchResults:
	""" Booru search results. """
	def __init__(self, **kwargs):
		self.tags = kwargs.get("tags")
		self.page = kwargs.get("page")
		self.limit = kwargs.get("limit")
		self.total = kwargs.get("total")
		self.posts = kwargs.get("posts")
	
	def __repr__(self):
		return "<SearchResult tags=%s>" % self.tags

class Booru:
	""" Superclass for booru site implementations. """
	def __init__(self):
		self._dl = Downloader()
		self.results = SearchResults(
			posts=[],
			tags=[],
			page=0,
			limit=0,
			total=0
		)
	
	def _rating(self, letter):
		ratings = {
			"s": "safe",
			"q": "questionable",
			"e": "explicit"
		}
		return ratings[letter]
	
	def _new_results(self, **kwargs):
		self.results = SearchResults(posts=[], **kwargs)
	
	def _add_post(self, **kwargs):
		self.results.posts.append(Post(self._dl, **kwargs))
	
	def search(self, tags=[], limit=50, page=0):
		""" Search method template. """
		raise NotImplementedError()
