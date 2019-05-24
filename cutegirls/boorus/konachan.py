from cutegirls.booru import *

from datetime import datetime

_SITE = "http://konachan.com"
_API = _SITE + "/post.xml"

class Konachan(Booru):
	def __init__(self):
		super().__init__("Konachan", _SITE)
	
	def _konachan_params(self, tags, limit, page):
		params = {
			"page": str(page),
			"limit": str(limit)
		}
		if tags:
			params["tags"] = "+".join(tags)
		return params
	
	def _konachan_date(self, date_str):
		return datetime.utcfromtimestamp(int(date_str))
	
	def _konachan_add_post(self, post_xml):
		self._add_post(
			id=int(post_xml.attrib["id"]),
			file_url=post_xml.attrib["file_url"],
			sample_url=post_xml.attrib["sample_url"],
			preview_url=post_xml.attrib["preview_url"],
			tags=post_xml.attrib["tags"].split(),
			date=self._konachan_date(post_xml.attrib["created_at"]),
			width=int(post_xml.attrib["width"]),
			height=int(post_xml.attrib["height"]),
			score=int(post_xml.attrib["score"]),
			rating=post_xml.attrib["rating"],
			md5=post_xml.attrib["md5"],
			source=post_xml.attrib["source"]
		)
	
	def _search(self, tags, limit, page):
		params = self._konachan_params(tags, limit, page)
		xml = self._dl.get_xml(_API, params)
		self._new_results(
			tags=tags,
			page=page,
			limit=limit,
			total=int(xml.attrib["count"])
		)
		for post_xml in xml:
			self._konachan_add_post(post_xml)
