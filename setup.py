import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kinopoiskhd",
    version="0.0.1",
    author="RAINGM",
    author_email="",
    description="Get films info from api: https://kinopoiskapiunofficial.tech",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)