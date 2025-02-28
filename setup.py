from setuptools import find_packages, setup
from os.path import abspath, dirname, join

ROOT_DIR = abspath(dirname(__file__))

with open(join(ROOT_DIR, "README.md"), encoding="utf-8") as f:
    readme = f.read()

setup(
    name="tap-amazon-sp",
    version="0.1.6",
    description="Singer ETL tap for extracting data from the Amazon Selling Partner API",
    long_description=readme,
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_amazon_sp"],
    install_requires=["backoff==2.2.1", "singer-python==6.1.0", "python-amazon-sp-api==1.9.12"],
    entry_points="""
    [console_scripts]
    tap-amazon-sp=tap_amazon_sp:main
    """,
    packages=find_packages(exclude=["tests"]),
    package_data={"schemas": ["tap_amazon_sp/schemas/*.json"]},
    include_package_data=True,
)
