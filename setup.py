from setuptools import setup, find_packages

setup(name="american_dialect_identification",
      version="0.1",
      packages=find_packages(where="src"),
      package_dir={"": "src"})
