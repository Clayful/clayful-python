from setuptools import setup

setup(
	name             = 'clayful-python',
	version          = '0.0.0',
	description      = 'Python SDK for Clayful API',
	long_description = open('README.md').read(),
	author           = 'Daeik Kim',
	author_email     = 'daeik.kim@clayful.io',
	url              = 'https://github.com/Clayful/clayful-python',
	keywords         = 'eCommerce clayful',
	license          = 'MIT',
	packages         = ['clayful'],
	install_requires = [
		'requests>2.1,<3'
	],
	extras_require   = {
		'test': ['httpretty>0.8']
	}
)