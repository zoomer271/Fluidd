from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fluidd-package",
    version="0.0.1",
    author="Fluidd",
    author_email="fluidd.llc@gmail.com",
    description="A package for using Fluidd Chat API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zoomer271/fluidd-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
       "apscheduler",
       "sqlite3",
       "aiohttp",
    ],
)