
from setuptools import setup, find_packages


with open("README.md", "r") as f:
	long_description = f.read()

setup(
	include_package_data=True,
	name='biranchi',
	version='0.0.1',
	description='biranchi python module',
	url='http://www.biranchi.com/',
	author_email='biranchi125@gmail.com',
	packages=find_packages(),
	install_requires=['pandas', 'pytest'],
	long_description=long_description,
	long_description_content_type="text/markdown",
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent"
	]
)