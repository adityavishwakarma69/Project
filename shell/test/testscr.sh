#!/bin/bash

#read -p "ENTER A DIRECTORY : " DIR

#if [ -d $DIR ];
#then
#  echo "DIRECTIORY EXISTS"
#else
#  echo "DIRECTIORY DOES NOT EXISTS"
#fi

read -p "ENTER PATH OF A FILE : " FPATH

if [ -e $FPATH ];
then
  echo "FILE EXISTS"
else
  echo "FILE DOES NOT EXISTS"
fi
