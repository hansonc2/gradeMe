#!/bin/bash
pip install -r requirements.txt

CUR_DIR = $(pwd)

echo 'export PATH=GRADEME_SCRIPT_DIR=$CURDIR' >> ~/.bash_profile

source ~/.bash_profile

cp .gradeMe.sh ~/
chmod +x ~/.gradeMe.sh
./gradeMe.sh

