#!/bin/bash
set -e

echo "Doing pythonic things"
pushd ../python
poetry run embed_skip.py "${ENV_INSTA_TOKEN}"
popd

echo "As you were"
