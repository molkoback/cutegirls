from .gelbooru import Gelbooru
from .danbooru import Danbooru
from .yandere import Yandere

_boorus = {
	"gelbooru": Gelbooru,
	"danbooru": Danbooru,
	"yande.re": Yandere,
	"yandere": Yandere
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
	return [key for key in _boorus.keys()]
