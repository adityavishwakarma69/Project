#!/bin/bash

read -p "ENTER THE SUBNET : " SUBN

for N in $(seq 1 254); do 
  ping -c 1 ${SUBN}.${N}
done
