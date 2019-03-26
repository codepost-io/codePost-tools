# codePost Terminal Tools

The codePost Terminal Tools provides a set of tools to control your codePost course from the comfort of your terminal or shell scripts. These tools are built in Python 3.x using our codePost API Python bindings, which can also be installed from PyPi.

## Installation

You can install the codePost Terminal Tools in your path using pip:

```
pip install --upgrade codePost-tools
```

## Usage

To use the functions available in this library, you must have a codePost API key. As of March 2019, to retrieve a codePost API key, you must be a administrator of a course on codePost. It will then be accessible from https://codepost.io/settings.

# Configuration

For convenience, it is also possible to specify a default course name, course period and codePost API key, by providing these in a configuration file. This configuration file can be called `codepost-config.yaml` or `.codepost-config.yaml` and be located in the root of the local user's home directory.

```
api_key: "<API KEY HERE>" # https://codepost.io/settings
course_name: "<COURSE NAME HERE>"
course_period: "<COURSE PERIOD HERE>"
```

## Command Line Syntax

```
> ./upload-to-codePost --help
usage: upload-to-codePost [-h] [-api_key API_KEY] [-course_name COURSE_NAME]
                          [-course_period COURSE_PERIOD]
                          [-assignment_name ASSIGNMENT_NAME]
                          [-students STUDENTS] [-files FILES [FILES ...]]
                          [--extend] [--overwrite]

optional arguments:
  -h, --help                            show this help message and exit
  -api_key API_KEY                      the API key to authenticate upload
  -course_name COURSE_NAME              the name of the course to upload to (e.g. COS126)
  -course_period COURSE_PERIOD          the period of the course to upload to (e.g. S2019)
  -assignment_name ASSIGNMENT_NAME      the name of the assignment to upload to (e.g. Loops)
  -students STUDENTS                    comma-separated list of student emails
  -files FILES [FILES ...]              comma-separated list of file paths
  --extend                              If submission already exists, add new files to it and
                                        replace old files if the code has changed.
  --overwrite                           If submission already exists, overwrite it.
```

# Related Repositories

- Princeton University has variants of this tool which integrates specifically in its Tigerfile submission platform: https://github.com/PrincetonUniversity/codePost-tools
