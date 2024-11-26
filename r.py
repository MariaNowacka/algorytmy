import os
p=r'c:\\Users\\lenovo\\Desktop\\maria\\l2_z6_dir\\dir1'
a=list(p.split('\\'))[0:-2]
#a=list(a)
#a=a[0:-2]
print(a)
b='\\'.join(a)
print(b)
# if list(path)==path:
#            p = list(path.split("\\"))[0:-2]
#            b = "\\".join(p)
#            return find(b, filename)