# Urls change all the fucking time so just check for HTTP errors

from cutegirls import *

import unittest
import requests
from datetime import datetime

class TestCuteGirls(unittest.TestCase):
	def check_url(self, url):
		return requests.get(url).ok
	
	def test_gelbooru_post(self):
		cg = CuteGirls("gelbooru")
		r = cg.search(["kafuu_chino", "solo", "swimsuit", "screencap"])
		post = r.posts[-1]
		
		self.assertTrue(self.check_url(post.file_url))
		self.assertTrue(self.check_url(post.sample_url))
		self.assertTrue(self.check_url(post.preview_url))
		
		self.assertEqual(post.id, 2284423)
		self.assertEqual(post.file_ext, "jpg")
		self.assertEqual(post.sample_ext, "jpg")
		self.assertEqual(post.preview_ext, "jpg")
		self.assertTrue(type(post.tags) is list)
		self.assertTrue(type(post.date) is datetime)
		self.assertEqual(str(post.date), "2014-06-03 19:05:04-05:00")
		self.assertEqual(post.width, 1252)
		self.assertEqual(post.height, 1827)
		self.assertTrue(type(post.score) is int)
		self.assertEqual(post.rating, "s")
		self.assertEqual(post.rating_long, "safe")
		self.assertEqual(post.md5, "2ec2f08e3a6a0e81e9085acffdb9a39e")
		self.assertEqual(post.source, "")
	
	def test_danbooru_post(self):
		cg = CuteGirls("danbooru")
		r = cg.search(["kafuu_chino", "watermelon_hair_ornament"])
		post = r.posts[-1]
		
		self.assertTrue(self.check_url(post.file_url))
		self.assertTrue(self.check_url(post.sample_url))
		self.assertTrue(self.check_url(post.preview_url))
		
		self.assertEqual(post.id, 1699467)
		self.assertEqual(post.file_ext, "jpg")
		self.assertEqual(post.sample_ext, "jpg")
		self.assertEqual(post.preview_ext, "jpg")
		self.assertTrue(type(post.tags) is list)
		self.assertTrue(type(post.date) is datetime)
		self.assertEqual(str(post.date), "2014-05-31 07:06:18-04:00")
		self.assertEqual(post.width, 4091)
		self.assertEqual(post.height, 5937)
		self.assertTrue(type(post.score) is int)
		self.assertEqual(post.rating, "s")
		self.assertEqual(post.rating_long, "safe")
		self.assertEqual(post.md5, "451e8121d497c6982eb51c0a102467a2")
		self.assertEqual(post.source, "Megami #170")
	
	def test_yandere_post(self):
		cg = CuteGirls("yande.re")
		r = cg.search(["kafuu_chino", "bikini", "okuda_yousuke"])
		post = r.posts[-1]
		
		self.assertTrue(self.check_url(post.file_url))
		self.assertTrue(self.check_url(post.sample_url))
		self.assertTrue(self.check_url(post.preview_url))
		
		self.assertEqual(post.id, 279590)
		self.assertEqual(post.file_ext, "jpg")
		self.assertEqual(post.sample_ext, "jpg")
		self.assertEqual(post.preview_ext, "jpg")
		self.assertTrue(type(post.tags) is list)
		self.assertTrue(type(post.date) is datetime)
		self.assertEqual(str(post.date), "2014-02-01 00:56:00")
		self.assertEqual(post.width, 5946)
		self.assertEqual(post.height, 4086)
		self.assertTrue(type(post.score) is int)
		self.assertEqual(post.rating, "q")
		self.assertEqual(post.rating_long, "questionable")
		self.assertEqual(post.md5, "b135d4b665fd08131d3a8ed1973b4aa0")
		self.assertEqual(post.source, "")
	
	def test_konachan_post(self):
		cg = CuteGirls("konachan")
		r = cg.search(["kafuu_chino", "sanotsuki"])
		post = r.posts[-1]
		
		self.assertTrue(self.check_url(post.file_url))
		self.assertTrue(self.check_url(post.sample_url))
		self.assertTrue(self.check_url(post.preview_url))
		
		self.assertEqual(post.id, 184190)
		self.assertEqual(post.file_ext, "png")
		self.assertEqual(post.sample_ext, "jpg")
		self.assertEqual(post.preview_ext, "jpg")
		self.assertTrue(type(post.tags) is list)
		self.assertTrue(type(post.date) is datetime)
		self.assertEqual(str(post.date), "2014-06-10 14:12:04")
		self.assertEqual(post.width, 1200)
		self.assertEqual(post.height, 900)
		self.assertTrue(type(post.score) is int)
		self.assertEqual(post.rating, "s")
		self.assertEqual(post.rating_long, "safe")
		self.assertEqual(post.md5, "24d9eb020b1b7913aacde097fa5111e3")
		self.assertEqual(post.source, "http://i2.pixiv.net/img26/img/sntk/43994418.png")
	
	def test_rule34_post(self):
		cg = CuteGirls("rule34")
		r = cg.search(["kafuu_chino", "sasai_saji", "star"])
		post = r.posts[-1]
		
		self.assertTrue(self.check_url(post.file_url))
		self.assertTrue(self.check_url(post.sample_url))
		self.assertTrue(self.check_url(post.preview_url))
		
		self.assertEqual(post.id, 2537985)
		self.assertEqual(post.file_ext, "jpg")
		self.assertEqual(post.sample_ext, "jpg")
		self.assertEqual(post.preview_ext, "jpg")
		self.assertTrue(type(post.tags) is list)
		self.assertTrue(type(post.date) is datetime)
		self.assertEqual(str(post.date), "2017-10-22 04:10:05+00:00")
		self.assertEqual(post.width, 900)
		self.assertEqual(post.height, 1185)
		self.assertTrue(type(post.score) is int)
		self.assertEqual(post.rating, "e")
		self.assertEqual(post.rating_long, "explicit")
		self.assertEqual(post.md5, "b9fa83a3e8bec47d2ccd53a06e2fce1b")
		self.assertEqual(post.source, "https://i.pximg.net/img-original/img/2017/10/08/19/03/58/65341103_p0.jpg")
