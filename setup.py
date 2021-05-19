import setuptools

VERSION = '0.1.0'

setuptools.setup(
    name="sympan",
    version=VERSION,
    author="Alem Memic",
    author_email="memicalem@gmail.com",
    description="",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),

    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: I hope it is going to be useful",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "boto3==1.15.18",
        "joblib==1.0.1"
    ]
)
