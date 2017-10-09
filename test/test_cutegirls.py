from cutegirls import *

import unittest
from datetime import datetime

class TestCuteGirls(unittest.TestCase):
	def test_gelbooru_post(self):
		cg = CuteGirls("gelbooru")
		r = cg.search(["kafuu_chino", "solo", "swimsuit", "screencap"])
		post = r.posts[-1]
		
		self.assertEqual(post.id, 2284423)
		self.assertEqual(post.file_url, "http://gelbooru.com/images/2e/c2/2ec2f08e3a6a0e81e9085acffdb9a39e.jpg")
		self.assertEqual(post.sample_url, "http://gelbooru.com/samples/2e/c2/sample_2ec2f08e3a6a0e81e9085acffdb9a39e.jpg")
		self.assertEqual(post.preview_url, "http://gelbooru.com/thumbnails/2e/c2/thumbnail_2ec2f08e3a6a0e81e9085acffdb9a39e.jpg")
		self.assertEqual(post.file_name, "2ec2f08e3a6a0e81e9085acffdb9a39e")
		self.assertEqual(post.file_ext, "jpg")
		self.assertEqual(post.sample_name, "sample_2ec2f08e3a6a0e81e9085acffdb9a39e")
		self.assertEqual(post.sample_ext, "jpg")
		self.assertEqual(post.preview_name, "thumbnail_2ec2f08e3a6a0e81e9085acffdb9a39e")
		self.assertEqual(post.preview_ext, "jpg")
		self.assertTrue(type(post.tags) is list)
		self.assertTrue(type(post.date) is datetime)
		#self.assertEqual(str(post.date), "2014-06-03 19:05:04")
		self.assertEqual(post.width, 1252)
		self.assertEqual(post.height, 1827)
		self.assertTrue(type(post.score) is int)
		self.assertEqual(post.rating, "safe")
		self.assertEqual(post.md5, "2ec2f08e3a6a0e81e9085acffdb9a39e")
		self.assertEqual(post.source, "")
	
	def test_danbooru_post(self):
		cg = CuteGirls("danbooru")
		r = cg.search(["kafuu_chino", "watermelon_hair_ornament"])
		post = r.posts[-1]
		
		self.assertEqual(post.id, 1699467)
		self.assertEqual(post.file_url, "http://danbooru.donmai.us/data/__hoto_cocoa_kafuu_chino_tedeza_rize_and_tippy_gochuumon_wa_usagi_desu_ka_and_megami_drawn_by_okuda_yousuke__451e8121d497c6982eb51c0a102467a2.jpg")
		self.assertEqual(post.sample_url, "http://danbooru.donmai.us/data/sample/__hoto_cocoa_kafuu_chino_tedeza_rize_and_tippy_gochuumon_wa_usagi_desu_ka_and_megami_drawn_by_okuda_yousuke__sample-451e8121d497c6982eb51c0a102467a2.jpg")
		self.assertEqual(post.preview_url, "http://danbooru.donmai.us/data/preview/451e8121d497c6982eb51c0a102467a2.jpg")
		self.assertEqual(post.file_name, "__hoto_cocoa_kafuu_chino_tedeza_rize_and_tippy_gochuumon_wa_usagi_desu_ka_and_megami_drawn_by_okuda_yousuke__451e8121d497c6982eb51c0a102467a2")
		self.assertEqual(post.file_ext, "jpg")
		self.assertEqual(post.sample_name, "__hoto_cocoa_kafuu_chino_tedeza_rize_and_tippy_gochuumon_wa_usagi_desu_ka_and_megami_drawn_by_okuda_yousuke__sample-451e8121d497c6982eb51c0a102467a2")
		self.assertEqual(post.sample_ext, "jpg")
		self.assertEqual(post.preview_name, "451e8121d497c6982eb51c0a102467a2")
		self.assertEqual(post.preview_ext, "jpg")
		self.assertTrue(type(post.tags) is list)
		self.assertTrue(type(post.date) is datetime)
		#self.assertEqual(str(post.date), "2014-06-03 19:05:04")
		self.assertEqual(post.width, 4091)
		self.assertEqual(post.height, 5937)
		self.assertTrue(type(post.score) is int)
		self.assertEqual(post.rating, "safe")
		self.assertEqual(post.md5, "451e8121d497c6982eb51c0a102467a2")
		self.assertEqual(post.source, "Megami #170")
	
	def test_yandere_post(self):
		cg = CuteGirls("yande.re")
		r = cg.search(["kafuu_chino", "loli", "bikini"])
		post = r.posts[-1]
		
		self.assertEqual(post.id, 279590)
		self.assertEqual(post.file_url, "https://files.yande.re/image/b135d4b665fd08131d3a8ed1973b4aa0/yande.re%20279590%20bikini%20cleavage%20feet%20gochuumon_wa_usagi_desu_ka%3F%20hoto_cocoa%20kafuu_chino%20loli%20okuda_yousuke%20swimsuits%20tedeza_rize.jpg")
		self.assertEqual(post.sample_url, "https://files.yande.re/sample/b135d4b665fd08131d3a8ed1973b4aa0/yande.re%20279590%20sample%20bikini%20cleavage%20feet%20gochuumon_wa_usagi_desu_ka%3F%20hoto_cocoa%20kafuu_chino%20loli%20okuda_yousuke%20swimsuits%20tedeza_rize.jpg")
		self.assertEqual(post.preview_url, "https://assets.yande.re/data/preview/b1/35/b135d4b665fd08131d3a8ed1973b4aa0.jpg")
		self.assertEqual(post.file_name, "yande.re%20279590%20bikini%20cleavage%20feet%20gochuumon_wa_usagi_desu_ka%3F%20hoto_cocoa%20kafuu_chino%20loli%20okuda_yousuke%20swimsuits%20tedeza_rize")
		self.assertEqual(post.file_ext, "jpg")
		self.assertEqual(post.sample_name, "yande.re%20279590%20sample%20bikini%20cleavage%20feet%20gochuumon_wa_usagi_desu_ka%3F%20hoto_cocoa%20kafuu_chino%20loli%20okuda_yousuke%20swimsuits%20tedeza_rize")
		self.assertEqual(post.sample_ext, "jpg")
		self.assertEqual(post.preview_name, "b135d4b665fd08131d3a8ed1973b4aa0")
		self.assertEqual(post.preview_ext, "jpg")
		self.assertTrue(type(post.tags) is list)
		self.assertTrue(type(post.date) is datetime)
		#self.assertEqual(str(post.date), "2014-02-01 00:56:00")
		self.assertEqual(post.width, 5946)
		self.assertEqual(post.height, 4086)
		self.assertTrue(type(post.score) is int)
		self.assertEqual(post.rating, "questionable")
		self.assertEqual(post.md5, "b135d4b665fd08131d3a8ed1973b4aa0")
		self.assertEqual(post.source, "")
if __name__ == "__main__":
	unittest.main()
