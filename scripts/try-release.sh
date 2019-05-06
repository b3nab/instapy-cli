#!/bin/zsh
# Test the release of a new version of instapy-cli
# from build process

twine upload --repository-url https://test.pypi.org/legacy/ dist/*