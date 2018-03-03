from .booru import *

from datetime import datetime, timedelta

_SITE = "http://danbooru.donmai.us"

class DanbooruException(Exception):
	pass

class Danbooru(Booru):
	def __init__(self, login="", api_key=""):
		super().__init__("Danbooru", _SITE)
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
		return _SITE + url
	
	def _danbooru_date(self, date_str):
		tmp = date_str.split("T")
		dl = tmp[0].split("-")
		tl = tmp[1].split(":", 2)
		tl[2], z = tl[2].split(".")
		
		dt = datetime(
			int(dl[0]), int(dl[1]), int(dl[2]),
			int(tl[0]), int(tl[1]), int(tl[2])
		)
		
		# Timezone
		sign = z[3]
		hours = int(z[4:6])
		mins = int(z[7:9])
		delta = timedelta(hours=hours, minutes=mins)
		return dt-delta if sign=="+" else dt+delta
	
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
			rating=post_json["rating"],
			md5=post_json["md5"],
			source=post_json["source"]
		)
	
	def _search(self, tags, limit, page):
		params = self._danbooru_params(tags, limit, page)
		json = self._dl.get_json(_SITE + "/counts/posts.json", params)
		self._new_results(
			tags=tags,
			page=page,
			limit=limit,
			total=json["counts"]["posts"]
		)
		json = self._dl.get_json(_SITE + "/posts.json", params)
		for post_json in json:
			# TODO fix this shit
			# seriously the fuck?
			try:
				self._danbooru_add_post(post_json)
			except:
				pass
