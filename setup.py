from setuptools import setup, find_packages
setup(
    name="pybuilder-external-plugin-demo",
    version="0.2",
    packages=find_packages(),
    package_dir = {'': 'src/main/python'}
)
