#!Python

#enable debugging
import cgitb
cgitb.enable()

import cgi

# Tell the browser that it is an html document
print "Content-type: text/html"
print #end headers by printing an empty line

background = "#FEDA86"

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

#insert the welcome text
print "<img src='img/textWelcomeToBreadPage.png'><br>"
#insert happy bread! with link to underdebelopment.py
print "<a href='underDevelopment.py'><img src='img/thehappybread.jpg'></a><br>"
#insert the click-to-enter text
print "<img src='img/textClickToEnter.png'>"

print "</html>"