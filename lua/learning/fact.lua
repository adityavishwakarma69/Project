function fact (num)
  if num <= 1 then
    return 1
  else
    return num * fact(num - 1)
  end
end

print(fact(5))
