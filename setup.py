from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup_requires = [
    'spacy',
    'jupyter',
    'numpy',
    'matplotlib',
]

setup(
    name="nlp-in-10-lines",
    version="0.0.1",
    author="Cytora",
    maintainer_email='andraz@cytora.com',
    description='Natural Language Processing in 10 lines of code.',
    long_description=long_description,
    packages=find_packages(),
    setup_requires=setup_requires
)
