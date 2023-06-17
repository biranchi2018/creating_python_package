
## Creating Python Package

Following the below steps for creating python package


### 1. Folder structure:

    Project-Folder
	- Package-Name
		- __init__.py
		- module.py
	- __init__.py
	- setup.py
  	- LICENSE.txt
	- README.md
	
	
### 2. Create Virtual Environment:
	python -m venv env
	. env/bin/activate
	
	
### 3. Install Dependent Pip packages:

	pip install setuptools wheel twine
	

### 4. Add LICENSE.txt :
Copy the License content from (https://opensource.org/license/mit/)[https://opensource.org/license/mit/]



### 5. Create setup.py file:

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


### 6. Create Python Package:
	python setup.py bdist_wheel




Example :
==========

1. Create "biranchi" folder with the following:

   ```shell
    __.init__.py
    calculator.py
   ```
	
2. Build the package

   ```shell
   python setup.py bdist_wheel
   ```

2. Install the package

   ```shell
   pip install .
   or 
   pip install dist/biranchi-0.0.1-py3-none-any.whl
   ```
   
3. Using the Package :

   ```python
   from biranchi.calculator import add, sub, mul, div
	
   print(add(2,3))
   ```


### 7. Uploading the package to Pypi:

Create an account at Pypi (https://pypi.org/account/register/)

Run the below command to upload the package:

  ```cmd
   twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
  ```
