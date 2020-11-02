#!/bin/bash
set -e

echo "Doing pythonic things"
pushd ../python
poetry run embed_skip.py "${ENV_INSTA_TOKEN}"
<<<<<<< Updated upstream
popd
=======

echo "Doing chirpy things"
pushd tools


>>>>>>> Stashed changes

echo "As you were"
