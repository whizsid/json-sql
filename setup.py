from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="json-sql",
    version="0.0.1",
    author="WhizSid",
    author_email="whizsid@aol.com",
    description="Thi package will convert your json arrays with nested objects to a SQL relational schema.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/whizsid/json-sql/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: MIT",
    ],
)