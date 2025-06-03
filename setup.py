from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Circle-ci",
    version="0.1",
    author="Prateek",
    packages=find_packages(),
    install_requires = requirements,
)