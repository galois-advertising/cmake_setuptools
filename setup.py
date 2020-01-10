from setuptools import setup, find_packages
from cmake_setup import __version__

with open('README.md') as f:
    long_description = f.read()

setup(name='cmake_setup',
      description='Provides some usable cmake related build extensions',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Ray Douglass',
      url='https://github.com/galois-advertising/cmake_setup',
      version=__version__,
      install_requires=['setuptools'],
      license="Apache 2.0",
      packages=find_packages(),
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Build Tools'
      ])
