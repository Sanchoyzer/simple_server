from setuptools import setup

VERSION = '0.0'


setup(
    name='simple_server',
    version=VERSION,
    description='return sha512',
    author='noname',
    author_email='noname@nomame.no',
    platforms='any',
    install_requires=['aiohttp', 'aiofiles'],
    packages=['simple_server'],
)