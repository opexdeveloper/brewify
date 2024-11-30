from setuptools import setup, find_packages

setup(
    name="brewify",
    version="0.1.0",  
    packages=find_packages(),
    author="OPEX",
    long_description=open("README.md").read(),
    author_email="opexclaqz@gmail.com",
    url="https://github.com/opexdeveloper/brewify",  
    keywords=['discord', 'utility', 'socials', 'info', 'api', 'wrapper'],
    description="A Python library for interacting with various APIs including Google Search, IMDb, and Discord.",
    long_description=open("README.rst").read(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
    install_requires=[  
        "requests",  
        "pydantic",
        "fastapi"

    ],
)