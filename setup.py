import pathlib
import setuptools
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()



VERSION = '0.1.1'

setuptools.setup(
    name="sympan",
    version=VERSION,
    author="Alem Memic",
    author_email="memicalem@gmail.com",
    description="Python library for downloading anything from AWS S3",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/alem88/sympan",
    packages=["sympan"],
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=[
        "boto3==1.15.18",
        "joblib==1.0.1"
    ]
)
