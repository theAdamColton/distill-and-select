from setuptools import setup

# Basic information about the package
name = 'distill-and-select'
version = '0.0.1'
description = 'DnS: Distill-and-Select for Efficient and Accurate Video Indexing and Retrieval'

# Long description of the package (usually from a README file)
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["distill_and_select"],
)
