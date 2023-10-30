import re
list=["test get","test give","test selenium"]
for element in list:
    z=re.match("(g\w+)\W(g\w+)",element)
if z:
    print((z.groups()))

patterns=["software testing","test"]
text='software testing is fun?'
for pattern in patterns:
    print('Looking for "%s" in "%s"->'%(pattern,text),end='')
    if re.search(pattern,text):
        print('found a match')
else:
    print('no match')
abc='abc@google.com, def@gmail.com, ghi@hotmail.com'
