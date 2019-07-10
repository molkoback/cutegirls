from cutegirls.booru import *

from datetime import datetime

class Gelbooru(Booru):
	def __init__(self, **kwargs):
		super().__init__(name="Gelbooru", url="https://gelbooru.com/index.php", **kwargs)
	
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
	
	def _gelbooru_datetime(self, date_str):
		return datetime.strptime(date_str[4:], "%b %d %H:%M:%S %z %Y")
	
	def _gelbooru_add_post(self, post_xml):
		self._add_post(
			id=int(post_xml.attrib["id"]),
			file_url=post_xml.attrib["file_url"],
			sample_url=post_xml.attrib["sample_url"],
			preview_url=post_xml.attrib["preview_url"],
			tags=post_xml.attrib["tags"].split(),
			date=self._gelbooru_datetime(post_xml.attrib["created_at"]),
			width=int(post_xml.attrib["width"]),
			height=int(post_xml.attrib["height"]),
			score=int(post_xml.attrib["score"]),
			rating=post_xml.attrib["rating"],
			md5=post_xml.attrib["md5"],
			source=post_xml.attrib["source"]
		)
	
	def _search(self, tags, limit, page):
		params = self._gelbooru_params(tags, limit, page)
		xml = self._dl.get_xml(self.url, params)
		self._new_results(
			tags=tags,
			page=page,
			limit=limit,
			total=int(xml.attrib["count"])
		)
		for post_xml in xml:
			self._gelbooru_add_post(post_xml)
