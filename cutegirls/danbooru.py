from .booru import *

from datetime import datetime

_API = "http://danbooru.donmai.us"

class DanbooruException(Exception):
	pass

class Danbooru(Booru):
	def __init__(self, login="", api_key=""):
		super().__init__()
		self.login = login
		self.api_key = api_key
	
	def _danbooru_params(self, tags, limit, page):
		params = {
			"page": str(page+1),
			"limit": str(limit)
		}
		if self.login and self.api_key:
			params["login"] = self.login
			params["api_key"] = self.api_key
		if tags:
			if len(tags) > 2:
				raise DanbooruException(
					"Danbooru doesn't support more than 2 tags"
				)
			params["tags"] = "+".join(tags)
		return params
	
	def _danbooru_url(self, url):
		if url[:4] == "http":
			return url
		return _API + url
	
	def _danbooru_date(self, date_str):
		# TODO localtime maybe?
		tmp = date_str.split("T")
		d = tmp[0].split("-")
		t = tmp[1].split(":")
		return datetime(
			int(d[0]), int(d[1]), int(d[2]),
			int(t[0]), int(t[1]), int(t[2].split(".")[0])
		)
	
	def _danbooru_add_post(self, post_json):
		self._add_post(
			id=post_json["id"],
			file_url=self._danbooru_url(post_json["file_url"]),
			sample_url=self._danbooru_url(post_json["large_file_url"]),
			preview_url=self._danbooru_url(post_json["preview_file_url"]),
			tags=post_json["tag_string"].split(),
			date=self._danbooru_date(post_json["created_at"]),
			width=post_json["image_width"],
			height=post_json["image_height"],
			score=post_json["score"],
			rating=self._rating(post_json["rating"]),
			md5=post_json["md5"],
			source=post_json["source"]
		)
	
	def search(self, tags=[], limit=50, page=0):
		params = self._danbooru_params(tags, limit, page)
		json = self._dl.get_json(_API + "/counts/posts.json", params)
		self._new_results(
			tags=tags,
			page=page,
			limit=limit,
			total=json["counts"]["posts"]
		)
		
		json = self._dl.get_json(_API + "/posts.json", params)
		for post_json in json:
			# TODO fix this shit
			# seriously the fuck?
			try:
				self._danbooru_add_post(post_json)
			except:
				pass
		
		return self.results
