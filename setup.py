from cutegirls import __version__

from setuptools import setup, find_packages

with open("README.md") as fp:
	readme = fp.read()

with open("requirements.txt") as fp:
	requirements = fp.read().splitlines()

setup(
	name="cutegirls",
	version=__version__,
	packages=find_packages(),
	
	install_requires=requirements,
	
	author="molko",
	author_email="molkoback@gmail.com",
	description="Grab posts from some *booru sites",
	long_description=readme,
	url="https://github.com/molkoback/cutegirls",
	license="WTFPL",
	
	classifiers=[
		"Intended Audience :: Developers",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3",
		"Topic :: Internet",
		"Topic :: Software Development :: Libraries"
	]
)
