s1 , s2 = "xx", "yy"
xy, yx = 0,0
for c1, c2 in zip(s1 , s2):
    print(c1 , c2 )
    if c1 == c2 : continue
    if c1 == 'x' : xy+=1
    else:
        yx +=1
print(xy , yx)
def convert_bin(n):
    if n>1 :
        return n//2

print(convert_bin(xy) , convert_bin((yx)))
