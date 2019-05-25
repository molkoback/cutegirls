from cutegirls.booru import *
from cutegirls.boorus import Gelbooru

from datetime import datetime

class Rule34(Gelbooru):
	def __init__(self):
		super().__init__()
		self.name = "Rule34"
		self.url = "https://rule34.xxx/index.php"
