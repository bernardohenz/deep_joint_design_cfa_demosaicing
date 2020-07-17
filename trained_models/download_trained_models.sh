#!/bin/bash

cd trained_models/


fileid="1IamcP_p058wC7XwrvyWOfwoWjSPV94_t"
filename="trained_models.zip"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}

#wget -N http://inf.ufrgs.br/~bhenz/trained_models.zip

unzip trained_models.zip

rm -rf trained_models.zip
rm -rf cookie

cd ..
