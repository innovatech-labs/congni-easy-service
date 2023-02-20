#!/bin/bash

pip install -t lib -r requirements.txt
(cd lib; zip ../lambda_function.zip -r .)
zip lambda_function.zip -u *.py
zip lambda_function.zip -u .env