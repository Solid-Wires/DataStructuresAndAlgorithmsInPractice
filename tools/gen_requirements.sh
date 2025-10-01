#!/bin/bash
# Linux shell script
# Pip chill doesn't remove all unnecessary dependencies
# This tool script ensures some deps are trimmed from reqs.txt

# Ensures that we’re in the project root and in the venv
cd "$(dirname "$0")"
. ../.venv/bin/activate

# Generate requirements, filter out unnecessary ones
pip-chill --no-version --no-chill \
| grep -v '^backports\.tarfile$' \
| grep -v '^importlib-metadata$' \
| grep -v '^jaraco\.collections$' \
| grep -v '^platformdirs$' \
> ../requirements.txt

echo "requirements.txt successfully updated"
