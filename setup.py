from setuptools import setup

# The text of the README file
README = open("README.md").read()

# This call to setup() does all the work
setup(
    name="codePost-tools",
    version="1.0.1",
    description="Command line tools to manage codePost from the comfort of your terminal!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/codepost-io/codePost-tools",
    author="codePost",
    author_email="team@codepost.io",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=[],
    scripts=["bin/upload-to-codePost"],
    install_requires=[
        "codePost-api",
        "PyYAML",
        "requests"
    ],
    include_package_data=True,
)
