def aa(a,v=0):
    if a ==0:
        return v
    e=a%10
    if e>v:
        v=e
    return aa(a//10,v)
print(aa(15243))