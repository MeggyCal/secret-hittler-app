#!/usr/bin/python3

from os import getenv
from json import dumps

print("Content-type: application/json")
print()

f=open("data","r")
num=int(f.read())
f.close()
if getenv('REQUEST_METHOD')=='POST':
    f=open("data","w")
    f.write(str(num+1))
    f.close()
    print(dumps([num+1,getenv('QUERY_STRING')]))
else:
    print(dumps([num]))
