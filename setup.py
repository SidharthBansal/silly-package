import setuptools



import os
from pathlib import Path
import shutil
import subprocess

from setuptools import setup, find_packages, Extension

setuptools.setup(
    name="mainpackage-sidharthbansal",
    version="0.0.11",
    author="Luke Petschauer",
    author_email="lukewrites@github.com",
    description="A primary example package that is silly.",
    long_description="A primary example package that is silly.",
    url="https://github.com/lukewrites/silly-package/primary",
    packages=find_packages("main"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
