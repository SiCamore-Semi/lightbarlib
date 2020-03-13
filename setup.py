import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="lightbar",
    version="0.0.1",
    author="Colin Suckow",
    author_email="csuckow@sicamoresemi.com",
    description="Easily control Sicamore Semi animated lightbars",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=setuptools.find_packages(),
    python_requires='>=3.6'
)