#!Python

#enable debugging
import cgitb
cgitb.enable()

import cgi

# Tell the browser that it is an html document
print "Content-type: text/html"
print #end headers by printing an empty line

#choose the backgroundcolor from ini
fo = open("backgroundcolor.ini", "r")
background = fo.read();
fo.close()

#set title
print """
<head>
	<title>BreadPage!</title>
</head>"""

#start body and set background
print "<body bgcolor='",background,"'></body>"

#center everything beyond this point
print "<center>"

#put the text and picture a bit further down by cheating using <br>
print "<br><br><br><br><br><br>"

#insert the under development text
print "<img src='img/textUnderDevelopment.png'><br>"


print "</html>"