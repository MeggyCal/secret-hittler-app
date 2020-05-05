
def printfile(f):
    data = open(f,"r")
    print(data.read())
    data.close()

def printcgiheader(content):
    print("Content-type: "+content)
    print()

def redirect(target):
    s="""<!DOCTYPE html>
    <html>
       <head>
          <title>HTML Meta Tag</title>
          <meta http-equiv = "refresh" content = "0; url = {}" />
       </head>
       <body>
           <p>Probíhá přesměrování. Pokud se nic nestane, klikněte <a href="{}">sem</a>.</p>
       </body>
    </html>""".format(target,target)
    print(s)

def parseurl(s):
    dic = {}
    for item in s.split("&"):
        info=item.split("=")
        dic[info[0]]=info[1]
    return dic


