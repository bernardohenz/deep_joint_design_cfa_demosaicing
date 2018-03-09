#!/bin/bash

cd trained_models/

wget -N http://inf.ufrgs.br/~bhenz/trained_models.zip

unzip trained_models.zip

rm -rf trained_models.zip

cd ..