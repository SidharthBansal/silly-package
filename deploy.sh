#!/usr/bin/env bash

if [[ "$TRAVIS_TAG" =~ main ]]; then
    cd master
    python setup.py sdist
    ls dist/
    twine upload --repository-url DEV_PYPI dist/*
elif [[ "$TRAVIS_TAG" =~ secondary ]]; then
    cd secondary
    python setup.py sdist
    ls dist/
    twine upload --repository-url DEV_PYPI dist/*
else
    echo "no tag"
fi
