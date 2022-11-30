def lesser_of_two_evens(a,b):
  if a%2 == 0 and b%2 ==0:
    #checking to see if both numbers are even
    if a < b:
      result = a
    else:
      result = b
  else:
    #if one or both numbers are odd
    if a > b:
      result = a
    else:
      result = b
  return result

print(lesser_of_two_evens(224,456))