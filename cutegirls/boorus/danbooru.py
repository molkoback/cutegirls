from cutegirls.booru import *

from datetime import datetime, timedelta

class DanbooruException(Exception):
	pass

class Danbooru(Booru):
	def __init__(self, login="", api_key="", **kwargs):
		super().__init__(name="Danbooru", url="http://danbooru.donmai.us", **kwargs)
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
	
	def _danbooru_datetime(self, date_str):
		date_str = date_str[:19] + date_str[23:]
		return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")
	
	def _danbooru_add_post(self, post_json):
		self._add_post(
			id=post_json["id"],
			file_url=post_json["file_url"],
			sample_url=post_json["large_file_url"],
			preview_url=post_json["preview_file_url"],
			tags=post_json["tag_string"].split(),
			date=self._danbooru_datetime(post_json["created_at"]),
			width=post_json["image_width"],
			height=post_json["image_height"],
			score=post_json["score"],
			rating=post_json["rating"],
			md5=post_json["md5"],
			source=post_json["source"]
		)
	
	def _search(self, tags, limit, page):
		params = self._danbooru_params(tags, limit, page)
		json = self._dl.get_json(self.url + "/counts/posts.json", params)
		self._new_results(
			tags=tags,
			page=page,
			limit=limit,
			total=json["counts"]["posts"]
		)
		json = self._dl.get_json(self.url + "/posts.json", params)
		for post_json in json:
			# TODO fix this shit
			# seriously the fuck?
			try:
				self._danbooru_add_post(post_json)
			except:
				pass
