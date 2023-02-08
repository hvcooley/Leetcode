#Add in binary

#Example: a:"1010", b: "1011"

#  1010
#  1011

# 10101

# res = "0101"


#  1110
#  1101

# 11011

def addBinary(a: str, b: str) -> str:
    if len(a) > len(b):
  	numZeroes = len(a) - len(b)
    for i in range(numZeroes):
    	b = "0" + b
    #END for
  #END if
  elif len(b) > len(a):
  	numZeroes = len(b) - len(a)
    for i in range(numZeroes):
    	a = "0" + a
    #END for
  #END elif
  res = ""
  carry = False
  for j in range(len(a)-1,-1,-1):
  	if a[j] == "0" and b[j] == "0":
    	if carry:
      	res = "1" + res
        carry = False
      else:
      	res = "0" + res
    #END if both 0s
    elif a[j] == "1" and b[j] == "1":
    	if carry:
      	res = "1" + res
      else:
      	res = "0" + res
        carry = True
    #END if both 1s
    else:
    	if carry:
      	res = "0" + res
      else:
      	res = "1" + res
    #END else case for 1 and 0 or 0 and 1
  #END for j
  if carry == True:
  	res = "1" + res
#END addBinary
  
  
  
  


#END addBinary