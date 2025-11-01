from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ANIME-RECOMMENDER",
    version="0.1",
    author="Sudhanshu",
    packages=find_packages(), # finds all the local packages
    install_requires = requirements,
)