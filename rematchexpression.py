from re import *
a1="^[A-Za-z0-9]b.t[0-9]$"
a2="Bbat7"
a3=match(a1,a2)
print(a3)
"""
.=this defines the space between starting and ending letter
[]=this is used for giving character set
"""