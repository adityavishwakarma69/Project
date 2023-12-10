#!/bin/bash

function hello(){
  echo hello
}

for S in $(seq 5); do 
  echo hello ${S}
done
