#!/bin/bash

# create conda env
read -rp "Enter environment name (recommended: wsd-hard-benchmark): " env_name
read -rp "Enter python version (recommended: 3.8): " python_version
conda create -yn "$env_name" python="$python_version"
eval "$(conda shell.bash hook)"
conda activate "$env_name"

# install python requirements
pip install -r requirements.txt
