import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ebrains-atlascore",
    version="0.0.4.dev1",
    author="Vadim Marcenko",
    author_email="v.marcenko@fz-juelich.de",
    description="Core functionality for the atlas viewer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HumanBrainProject/atlas-core-lib.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
