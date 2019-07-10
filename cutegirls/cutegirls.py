from cutegirls.boorus import __ids__

def CuteGirls(name="gelbooru", **kwargs):
	""" 
	Creates a new Booru instance. Raises KeyError if the given name was
	invalid.
	"""
	namel = name.lower()
	if not namel in __ids__:
		raise KeyError("Booru not found: '{}'".format(name))
	return __ids__[namel](**kwargs)

def boorulist():
	""" Lists all the available booru sites. """
	return list(__ids__.keys())
