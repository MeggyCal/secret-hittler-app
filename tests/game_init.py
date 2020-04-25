#!/usr/bin/python3
from random import randint
from os import getenv
from json import dumps

print("Content-type: application/json")
print()

game_id = 0
with open('data', 'w') as f:
    #  game_id is random to provide at least some "privacy"
    #  it is also a kind of password
    #  here will be something like main.init_game
    game_id = randint(0, 10**20)
    # TODO: do we want to run more games in parallel?
#    dup = True
#    while(dup):
#        dup = False
#        for s in f.readlines():
#            if(int(s) == game_id):
#                game_id = randint(0, 10**20)
#                dup = True
    f.write("%d\n" % game_id)

if getenv('REQUEST_METHOD')=='POST':
    print(dumps([game_id,getenv('QUERY_STRING')]))
else:
    print("%d" % game_id)
