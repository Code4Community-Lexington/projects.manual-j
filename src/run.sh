#!/usr/bin/env bash
set -euo pipefail

ENTRYPOINT="${1:-./app.py}"

# create venv if it does not exist
[[ -d venv ]] || python -m venv venv

# ensure venv is activated and dependencies are installed
source venv/bin/activate
pip install -r requirements.txt 1> /dev/null

# run program
python "$ENTRYPOINT"