from .booru import *
from .util import boorutime

from datetime import datetime

_API = "https://gelbooru.com/index.php"

class Gelbooru(Booru):
	def _gelbooru_params(self, tags, limit, page):
		params = {
			"page": "dapi",
			"s": "post",
			"q": "index",
			"pid": str(page),
			"limit": str(limit)
		}
		if tags:
			params["tags"] = "+".join(tags)
		return params
	
	def _gelbooru_url(self, url):
		return "http://" + url[url.find("gelbooru.com"):]
	
	def _gelbooru_add_post(self, post_xml):
		self._add_post(
			id=int(post_xml.attrib["id"]),
			file_url=self._gelbooru_url(post_xml.attrib["file_url"]),
			sample_url=self._gelbooru_url(post_xml.attrib["sample_url"]),
			preview_url=self._gelbooru_url(post_xml.attrib["preview_url"]),
			tags=post_xml.attrib["tags"].split(),
			date=boorutime(post_xml.attrib["created_at"]),
			width=int(post_xml.attrib["width"]),
			height=int(post_xml.attrib["height"]),
			score=int(post_xml.attrib["score"]),
			rating=self._rating(post_xml.attrib["rating"]),
			md5=post_xml.attrib["md5"],
			source=post_xml.attrib["source"]
		)
	
	def search(self, tags=[], limit=50, page=0):
		params = self._gelbooru_params(tags, limit, page)
		xml = self._dl.get_xml(_API, params)
		self._new_results(
			tags=tags,
			page=page,
			limit=limit,
			total=int(xml.attrib["count"])
		)
		
		for post_xml in xml:
			self._gelbooru_add_post(post_xml)
		
		return self.results
