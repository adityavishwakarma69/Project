#!/usr/bin/env lua

A = {} --like dict in python

A['a'] = 1
A['b'] = 2

--print(A['a'])
--print(A.b) -- same as A['b']


--psuedo array

arr = {}

for i = 1, 10 do
  arr[i] = i*10
end

for i, value in ipairs(arr) do
  print(i..":"..value)
end

for value in pairs(arr) do
  print(arr[value])
end
