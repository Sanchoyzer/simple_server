from setuptools import setup


setup(
    name='simple_server',
    version='0.0',
    description='return sha512',
    install_requires=['aiohttp', 'aiofiles'],
    py_modules=['main'],
)