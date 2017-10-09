from .booru import *

from datetime import datetime

_API = "https://yande.re/post.xml"

class Yandere(Booru):
	def _yandere_params(self, tags, limit, page):
		params = {
			"page": str(page+1),
			"limit": str(limit)
		}
		if tags:
			params["tags"] = "+".join(tags)
		return params
	
	def _yandere_date(self, date_str):
		# TODO localtime maybe?
		return datetime.fromtimestamp(int(date_str))
	
	def _yandere_add_post(self, post_xml):
		self._add_post(
			id=int(post_xml.attrib["id"]),
			file_url=post_xml.attrib["file_url"],
			sample_url=post_xml.attrib["sample_url"],
			preview_url=post_xml.attrib["preview_url"],
			tags=post_xml.attrib["tags"].split(),
			date=self._yandere_date(post_xml.attrib["created_at"]),
			width=int(post_xml.attrib["width"]),
			height=int(post_xml.attrib["height"]),
			score=int(post_xml.attrib["score"]),
			rating=self._rating(post_xml.attrib["rating"]),
			md5=post_xml.attrib["md5"],
			source=post_xml.attrib["source"]
		)
	
	def search(self, tags=[], limit=50, page=0):
		params = self._yandere_params(tags, limit, page)
		xml = self._dl.get_xml(_API, params)
		self._new_results(
			tags=tags,
			page=page,
			limit=limit,
			total=int(xml.attrib["count"])
		)
		
		for post_xml in xml:
			self._yandere_add_post(post_xml)
		
		return self.results
