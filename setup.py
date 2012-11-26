from setuptools import setup, find_packages

version = '0.0.1-ALPHA'

long_desc = """
cqlengine is a Cassandra CQL ORM for Python in the style of the Django orm and mongoengine

[Documentation](https://github.com/bdeggleston/cqlengine/wiki/Documentation)

[Report a Bug](https://github.com/bdeggleston/cqlengine/issues)

[Users Mailing List](https://groups.google.com/forum/?fromgroups#!forum/cqlengine-users)

[Dev Mailing List](https://groups.google.com/forum/?fromgroups#!forum/cqlengine-dev)

**NOTE: cqlengine is in alpha and under development, some features may change (hopefully with notice). Make sure to check the changelog and test your app before upgrading**
"""

setup(
    name='cqlengine',
    version=version,
    description='Cassandra CQL ORM for Python in the style of the Django orm and mongoengine',
    long_description=long_desc,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Environment :: Plugins",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='cassandra,cql,orm',
    author='Blake Eggleston',
    author_email='bdeggleston@gmail.com',
    url='https://github.com/bdeggleston/cqlengine',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
)

