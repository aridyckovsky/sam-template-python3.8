from setuptools import setup, find_packages

setup(
    name = {{cookiecutter.project_slug}},
    packages = find_packages("src"),
    package_dir = {"": "src"} 
)
