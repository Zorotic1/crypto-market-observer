#!/bin/bash
# Micro-diagnostic script for automated testing
echo "Initializing Python code quality checks..."
pip install flake8
flake8 api/ py_code/ --count --select=E9,F63,F7,F82 --show-source --statistics