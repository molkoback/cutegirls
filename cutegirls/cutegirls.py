from .gelbooru import Gelbooru
from .danbooru import Danbooru
from .yandere import Yandere
from .konachan import Konachan
from .rule34 import Rule34

_boorus = {
	"gelbooru": Gelbooru,
	"danbooru": Danbooru,
	"yande.re": Yandere,
	"yandere": Yandere,
	"konachan": Konachan,
	"rule34": Rule34
}

def CuteGirls(name="gelbooru"):
	""" 
	Creates a new Booru instance. Raises KeyError if the given name was
	invalid.
	"""
	namel = name.lower()
	if not namel in _boorus:
		raise KeyError("Booru not found: '%s'" % name)
	return _boorus[namel]()

def boorulist():
	""" Lists all the available booru sites. """
	return list(_boorus.keys())
