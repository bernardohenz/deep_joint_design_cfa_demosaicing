#!/bin/bash

cd datasets/

fileid="1lnFhEnEv6rAF8apVj5issvA9lDxXq8T1"
filename="datasets.zip"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}

unzip datasets.zip

rm -rf datasets.zip
rm -rf cookie

cd ..
