import setuptools

setuptools.setup(
    name="ligth-form-service",
    version="",
    author="Mustafa Paydaş",
    author_email="mustafapaydass@gmail.com",
    description="Mantis Appeal Form",
    url="https://github.com/mantis-software-company/ligth-form-service",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    platforms="all",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9"
    ],
    install_requires=['Django~=4.0.2', 'CryptICE`~=2.0','openpyxl~=3.0.9'],
    python_requires=">3.8.*, <4",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"}
)