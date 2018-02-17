from setuptools import setup

with open("README.md") as fp:
	readme = fp.read()

with open("requirements.txt") as fp:
	requirements = fp.read().splitlines()

setup(
	name="cutegirls",
	author="molko",
	author_email="molkoback@gmail.com",
	url="https://github.com/molkoback/cutegirls",
	packages=["cutegirls"],
	version="0.3.1",
	license="WTFPL",
	description="Grab posts from some *booru sites",
	long_description=readme,
	install_requires=requirements,
	classifiers=[
		"Intended Audience :: Developers",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3",
		"Topic :: Internet",
		"Topic :: Software Development :: Libraries",
		"Topic :: Software Development :: Libraries :: Python Modules"
	]
)
