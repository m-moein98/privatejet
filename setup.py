"""
Setup file for the package.
"""

from setuptools import find_packages, setup


classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Operating System :: Microsoft :: Windows :: Windows 11",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.11",
]
with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()
with open("CHANGELOG.txt", "r", encoding="utf-8") as fh:
    change_log = fh.read()
setup(
    name="privatejet",
    version="0.0.3",
    description="",
    long_description=readme + "\n\n" + change_log,
    long_description_content_type="text/markdown",
    url="https://privatejet.readthedocs.io/en/latest/",
    author="m-moein-98",
    author_email="moein1475963.mmz@gmail.com",
    license="OSI Approved :: MIT License",
    classifiers=classifiers,
    keywords="python backend framework private-jet-framework",
    packages=find_packages(),
    install_requires=[""],
)
