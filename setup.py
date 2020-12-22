import setuptools
from mxl import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

#with open("README.md", "r") as fh:
#   long_description = fh.read()

setuptools.setup(
    name="qztr_mxl", # Replace with your own username
    version=__version__,
    author="qztr",
    author_email="vladiska777@gmail.com",
    description="matrix calculation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)