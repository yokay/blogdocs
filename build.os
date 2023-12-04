# .readthedocs.yaml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Set the version of Python and other tools you might need
build:
  os: ubuntu-22.04
  tools:
    python: 3.11

# Build documentation in the docs/ directory with Sphinx
sphinx:
  configuration: conf.py

# We recommend specifying your dependencies to enable reproducible builds:
# https://docs.readthedocs.io/en/stable/guides/reproducible-builds.html
python:
    install:
    - requirements: requirements.txt
