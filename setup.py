import setuptools
from mxl import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qztr_mxl", 
    version=__version__,
    author="qztr",
    author_email="vladiska777@gmail.com",
    description="matrix calculation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qztr/mxl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)