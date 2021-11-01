
from setuptools import setup

setup(
    name='bipscan',
    version='0.0.1',
    description='My private package from private github repo',
    url='git+ssh://git@github.com/estaar/bipscan.git',
    author='John Esther',
    author_email='estaarjohn@gmail.com',
    license='unlicense',
    packages=['bipscan'],
    zip_safe=False
)
