from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='gest_form_or_gestform',
    version='1.0.0',
    description='A random numbers generator and divisibility based translator',
    long_description=readme,
    author='Benjamin Destruhaut',
    author_email='benjamin.destruhaut@outlook.fr',
    url='https://github.com/stbenus/gest-form-or-gestform',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)