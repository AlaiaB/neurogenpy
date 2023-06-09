from setuptools import setup, find_packages

# Read requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Read README for the long description
with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='neurogenpy',
    author='Computational Intelligence Group (CIG), Universidad Politécnica de Madrid',
    description='A library for estimating GRNs with Bayesian networks.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    version='0.1.0',
    url='https://github.com/javiegal/neurogenpy',
    packages=find_packages(),
    classifiers=[],
    install_requires=requirements
)