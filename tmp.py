def f(s,x,base):
  sm = 0
  for c in s: 
    if '0' <= c <= '9':
      sm = sm * base + int(c)
    else:  #  c='x'
      sm = sm * base + x
  return sm

cnt = 0
for x in range(6,80):
  b1 = f("55113",x,x)
  b2 = f("7xx5",x,80)
  if abs(b1-b2)>1000000:
    print(x,b1,b2)
    cnt += 1
print(cnt)
