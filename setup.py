"""
Setup configuration for PySTL package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="pystl",
    version="1.0.0",
    author="PySTL Contributors",
    author_email="",
    description="Python Standard Template Library - C++ STL-style data structures for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pystl",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    keywords="stl, data structures, stack, queue, vector, set, map, priority queue, c++",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/pystl/issues",
        "Source": "https://github.com/yourusername/pystl",
    },
)
