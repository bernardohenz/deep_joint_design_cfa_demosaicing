#!/bin/bash

cd datasets/

wget -N http://inf.ufrgs.br/~bhenz/datasets.zip

unzip datasets.zip

rm -rf datasets.zip

cd ..