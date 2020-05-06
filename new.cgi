#!/usr/bin/python3

from os import getenv
from urllib.parse import unquote_plus as unquote
from urllib.parse import quote
import utils
import sys
import codecs
import os
import json


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

utils.printcgiheader("text/html")


try:
    name = unquote(utils.parseurl(getenv("QUERY_STRING"))["name"])
    for ch in name:
        if not ch.isalnum() and not (ch in "ěščřžýáíéďťňůúĚŠČŘŽÝÁÍÉĎŤŇÚŮ_ "): #FIXME Can this be done in a better way? I am open to allowing more characters, but also feel like we shouldn't alow everything. At least javascript, python and json special characters should be banned, but I would like to keep czech characters
            raise Exception(name)
    f=open("gamecount","r")#get new game ID. Possible race condition
    num=int(f.read())
    f.close()
    f=open("gamecount","w")
    f.write(str(num+1))
    f.close()
    f=open("games/"+str(num),"x")
    f.write(json.dumps({"phase":"lobby","players":[name]}))
    f.close()
    utils.redirect("lobby.cgi?game={}&name={}".format(str(num),quote(name)))
except Exception as e:
    utils.redirect("errorcreating.html")
    raise #so that they end up in error log if there is something wrong FIXME it seems to not be there anyway
    
