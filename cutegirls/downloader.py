import requests
import xml.etree.ElementTree
import hashlib

_TIMEOUT = 10

class DownloaderException(Exception):
	pass

class Downloader:
	""" Downloads shit. """
	def _create_url(self, url, params):
		if params:
			url += "?" + "&".join(
				[k + "=" + v for k, v in params.items()]
			)
		return url
	
	def _get(self, url, params):
		r = requests.get(
			self._create_url(url, params),
			timeout=_TIMEOUT,
		)
		if not r.ok:
			raise DownloaderException(
				"HTTP status code %d: %s"  % (
					r.status,
					r.reason
				)
			 )
		return r
	
	def get_text(self, url, params={}):
		return self._get(url, params).text
	
	def get_json(self, url, params={}):
		return self._get(url, params).json()
	
	def get_xml(self, url, params={}):
		r = self._get(url, params)
		return xml.etree.ElementTree.fromstring(r.text)
	
	def _check_md5(self, path, md5):
		with open(path, "rb") as fp:
			check = hashlib.md5()
			for chunk in iter(lambda: fp.read(check.block_size*16), b""):
				check.update(chunk)
		return check.hexdigest() == md5
	
	def save_content(self, url, path, md5=""):
		""" Downloads and saves content from the given url. """
		with open(path, "wb") as fp:
			r = requests.get(
				url,
				timeout=_TIMEOUT,
				stream=True
			)
			for chunk in r.iter_content(chunk_size=128):
				fp.write(chunk)
		
		if md5:
			if not self._check_md5(path, md5):
				raise DownloaderException("MD5 check failed")
