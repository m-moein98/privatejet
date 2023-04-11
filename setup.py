from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.11'
]

setup(
  name='privatejet',
  version='0.0.2',
  description='',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type="text/markdown",
  url='https://privatejet.readthedocs.io/en/latest/',  
  author='m-moein-98',
  author_email='moein1475963.mmz@gmail.com',
  license='OSI Approved :: MIT License', 
  classifiers=classifiers,
  keywords='python backend framework private-jet-framework', 
  packages=find_packages(),
  install_requires=[''] 
)