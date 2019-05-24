import requests
import hashlib
from xml.etree import ElementTree

_TIMEOUT = 10

class DownloaderException(Exception):
	pass

class Downloader:
	""" Downloads shit. """
	def __init__(self):
		self._session = requests.Session()
	
	def _create_url(self, url, params):
		if params:
			url += "?" + "&".join(
				[k + "=" + v for k, v in params.items()]
			)
		return url
	
	def _request(self, **kwargs):
		r = self._session.request(
			**kwargs,
			timeout=_TIMEOUT,
			headers={"Connection": "close"}
		)
		if not r.ok:
			raise DownloaderException(
				"HTTP status code %d: %s" % (r.status_code, r.reason)
			 )
		return r
	
	def get(self, url, params={}):
		return self._request(
			method="get",
			url=self._create_url(url, params)
		)
	
	def get_json(self, url, params={}):
		return self.get(url, params).json()
	
	def get_xml(self, url, params={}):
		r = self.get(url, params)
		return ElementTree.fromstring(r.text)
	
	def post(self, url, params, data):
		return self._request(
			method="post",
			url=self._create_url(url, params),
			data=data
		)
	
	def _check_md5(self, path, md5):
		with open(path, "rb") as fp:
			check = hashlib.md5()
			for chunk in iter(lambda: fp.read(check.block_size*16), b""):
				check.update(chunk)
		return check.hexdigest() == md5
	
	def save_content(self, url, path, md5=""):
		""" Downloads and saves content from the given url. """
		with open(path, "wb") as fp:
			r = self._request(
				method="get",
				url=url,
				stream=True
			)
			for chunk in r.iter_content(chunk_size=128):
				fp.write(chunk)
		
		if md5:
			if not self._check_md5(path, md5):
				raise DownloaderException("MD5 check failed")
