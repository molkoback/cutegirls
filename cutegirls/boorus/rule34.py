from cutegirls.boorus import Gelbooru

class Rule34(Gelbooru):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.name = "Rule34"
		self.url = "https://rule34.xxx/index.php"
