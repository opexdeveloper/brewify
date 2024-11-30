from setuptools import setup, find_packages

setup(
    name="brewify",
    version="0.1.0",  # Specify the version of your package
    packages=find_packages(),
    author="OPEX",
    author_email="opexclaqz@gmail.com",
    url="https://github.com/yourusername/brewify",  
    keywords=['discord', 'utility', 'socials', 'info', 'api', 'wrapper'],
    description="A Python library for interacting with various APIs including Google Search, IMDb, and Discord.",
    long_description=open("README.rst").read(),  
    long_description_content_type="text/x-rst",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Specify the license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
    install_requires=[  
        "requests",  
        "pydantic",
        "fastapi"

    ],
)