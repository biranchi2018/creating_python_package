
## Creating Python Package

Following the below steps for creating python package


### 1. Folder structure:

    Project-Folder
	- Package-Name
		- __init__.py
		- module.py
	- __init__.py
	- setup.py
	- README.md
	
	
### 2. Create Virtual Environment:
	python -m venv env
	. env/bin/activate
	
	
### 3. Install wheel package:

	pip install wheel
	
	
### 4. Create setup.py file:

```python3
from setuptools import setup, find_packages

setup(
	include_package_data=True,
	name='biranchi',
	version='0.0.1',
	description='biranchi python module',
	url='http://www.biranchi.com/',
	author_email='biranchi125@gmail.com',
	packages=find_packages(),
	install_requires=['pandas', 'pytest'],
	long_description='biranchi python modules',
	long_description_content_type="text/markdown",
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent"
	]
)
```

### 5. Create Python Package:
	python setup.py bdist_wheel





Example :
==========

1. Create "biranchi" folder with the following:

   ```shell
    __.init__.py
    calculator.py
   ```
	
2. Install the package

   ```shell
   pip install .
   or 
   python setup.py bdist_wheel
   pip install dist/biranchi-0.0.1-py3-none-any.whl
   ```
   
3. Open Terminal and python cli:

   ```python
   from biranchi.calculator import add, sub, mul, div
	
   print(add(2,3))
   ```

