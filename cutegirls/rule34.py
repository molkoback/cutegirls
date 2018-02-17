from .booru import *
from .util import months

from datetime import datetime

_API = "https://rule34.xxx/index.php"

class Rule34(Booru):
	def _rule34_params(self, tags, limit, page):
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
	
	def _rule34_date(self, date_str):
		# TODO localtime maybe?
		dt = date_str.split()
		t = dt[3].split(":")
		return datetime(
			int(dt[5]), months[dt[1]], int(dt[2]),
			int(t[0]), int(t[1]), int(t[2])
		)
	
	def _rule34_add_post(self, post_xml):
		self._add_post(
			id=int(post_xml.attrib["id"]),
			file_url=post_xml.attrib["file_url"],
			sample_url=post_xml.attrib["sample_url"],
			preview_url=post_xml.attrib["preview_url"],
			tags=post_xml.attrib["tags"].split(),
			date=self._rule34_date(post_xml.attrib["created_at"]),
			width=int(post_xml.attrib["width"]),
			height=int(post_xml.attrib["height"]),
			score=int(post_xml.attrib["score"]),
			rating=self._rating(post_xml.attrib["rating"]),
			md5=post_xml.attrib["md5"],
			source=post_xml.attrib["source"]
		)
	
	def search(self, tags=[], limit=50, page=0):
		params = self._rule34_params(tags, limit, page)
		xml = self._dl.get_xml(_API, params)
		self._new_results(
			tags=tags,
			page=page,
			limit=limit,
			total=int(xml.attrib["count"])
		)
		
		for post_xml in xml:
			self._rule34_add_post(post_xml)
		
		return self.results
