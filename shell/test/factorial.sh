#!/bin/bash

read -p "ENTER A NUMBER : " N
SUM=1
for I in $(seq $N); do 
  SUM=$((SUM*$I))
done

echo "FACTORIAL OF ${N} is ${SUM}"
