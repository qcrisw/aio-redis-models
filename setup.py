import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
    name="aioredis-models",
    version="1.2.0",
    description="Model Redis data structures",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/qcrisw/aioredis-models",
    author="QCRI Software Group",
    author_email="qcriswgroup@hbku.edu.qa",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords = ['redis', 'asyncio', 'data-structures', 'models'],
    packages=find_packages(exclude=("tests",)),
    install_requires=["aioredis==1.3.1"],
)
