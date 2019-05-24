from cutegirls.boorus import __ids__

def CuteGirls(name="gelbooru"):
	""" 
	Creates a new Booru instance. Raises KeyError if the given name was
	invalid.
	"""
	namel = name.lower()
	if not namel in __ids__:
		raise KeyError("Booru not found: '%s'" % name)
	return __ids__[namel]()

def boorulist():
	""" Lists all the available booru sites. """
	return list(__ids__.keys())
