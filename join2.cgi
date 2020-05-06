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

game=""
name=""
dic={}
try:
    dic=utils.parseurl(getenv("QUERY_STRING"))
    game=dic["game"]
    try:
        name = unquote(utils.parseurl(getenv("QUERY_STRING"))["name"])
        for ch in name:
            if not ch.isalnum() and not (ch in "ěščřžýáíéďťňůúĚŠČŘŽÝÁÍÉĎŤŇÚŮ_ "):
                raise Exception(name)
        f=open("games/"+game,"r")
        data=json.load(f)
        f.close
        if name in data["players"]:
            raise Exception("Name taken")
        data["players"].append(name)
        f=open("games/"+game,"w")
        f.write(json.dumps(data))
        f.close()
        utils.redirect("lobby.cgi?game={}&name={}".format(game,quote(name)))
    except Exception as e:
        utils.redirect("errorjoin.cgi?game="+game)
except:
    utils.redirect("error.html")
