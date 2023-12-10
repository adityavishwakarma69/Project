#!/bin/bash

read -p "Enter the length of the password : " PASSLEN

for P in $(seq 1 5); do 
  openssl rand -base64 48 | cut -c1-${PASSLEN}
done
