def maxnum(*nums):
  maxvalue = -float("inf")
  for num in nums :
      if (num > maxvalue) : maxvalue = num
  return maxvalue

print(maxnum(1,2,3,4,6))
