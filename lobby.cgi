#!/usr/bin/python3

from os import getenv
from urllib.parse import unquote_plus as unquote
from urllib.parse import quote
import utils
import sys
import codecs
import os
import json

url = "http://vm.kam.mff.cuni.cz:14080/hitler/" #FIXME to be abstracted into constants.py, but constants.py has syntax errors at the moment

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

utils.printcgiheader("text/html")

dic=utils.parseurl(getenv("QUERY_STRING"))
game=dic["game"]#FIXME some try/catch, check if game is actually number and if not, fail, otherwise we have XSS vulnerability
url = url+"join.cgi?game="+game

print("""<!DOCTYPE html>
<html>
	<head>
			<meta charset="UTF-8">
				<title>Secret Hitler &ndash; Lobby</title>
	</head>
	<body>
					<h1> Lobby</h1>

					<p>Pošli tento odkaz přátelům, kteří se mají přidat ke hře: <a href="{}">{}</a></p>
	</body>
</html>
""".format(url,url))#TODO rozpoznávání vedení, výpis členů, tlačítko startu


