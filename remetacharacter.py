from re import *
a="hi how are you"
tt=search("^hi.*you$",a)
if tt:
    print("true")
else:
    print("false")
"""META CHARACTERA
^=IS USED TO CHECK WHETHER THE GIVEN SUBSTRING IS THE STARTING POINT OF STRING
$=IS USED TO CHECK WHETHER THE GIVEN SUBSTRING IS THE ENDING POINT OF STRING"""