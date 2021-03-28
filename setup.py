import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='directionfinder',
    version='0.1',
    #scripts=['directions'] ,
    author="Aayush Pokharel",
    author_email="rockmanpokharel@yahoo.com",
    description="A small custom made Library that gives various directory.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AayushPokharel/directions_pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
