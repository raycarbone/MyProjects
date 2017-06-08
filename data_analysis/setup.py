from setuptools import setup, find_packages

setup(
	name='data_analysis',
	version='0..0.1',
	url='',
	license='',
	author='R.Carbone',
	packages=find_packages(),
	install_requires=['PyQt5', 
			'pandas', 
			'sqlalchemy', 
			'nltk', 
			'numpy', 
			'jupyter', 
			'pthon-twitter'],
	entry_points={},
	extra_requires={'dev': ['flakes',]},
	)

