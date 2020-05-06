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
    gameid = utils.parseurl(getenv("QUERY_STRING"))["game"]
    page="""<!DOCTYPE html>
    <html>
        <head>
	    <meta charset="UTF-8">
	    <title>Secret Hitler &ndash; Přidej se k již založené hře</title>
	</head>
	<body>
	    <h1> Secret Hitler &ndash; Přidej se ke hře!</h1>
                
            <form action="join2.cgi">
	        <label for="name">Jméno: </label><br>
	        <input type="text" id="name" name="name"><br>
	        <label for="game">Hra: </label><br>
	        <input type="text" id="game" name="game" value="{}" readonly><br>
                <input type="submit" value="Potvrdit">
            </form> 
	</body>
    </html>
    """.format(gameid)
    print(page)
except:
    utils.redirect("error.html")
    raise
