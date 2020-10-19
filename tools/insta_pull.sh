#!/bin/bash
#
# Initial the Categories/Tags pages and Lastmod for posts and then push to remote
#
# v2.0
# https://github.com/cotes2020/jekyll-theme-chirpy
# © 2019 Cotes Chung
# Published under MIT License

set -eu

WORK_DIR="$(dirname $(dirname $(realpath "$0")))"
echo $WORK_DIR

cd python
poetry install
poetry show
