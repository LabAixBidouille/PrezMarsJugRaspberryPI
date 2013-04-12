import serial, sys, feedparser

USERNAME="labaixbidouille"
PASSWORD="ceciestunmotdepassetoutnul"
PROTO="https://"
SERVER="mail.google.com"
PATH="/gmail/feed/atom"

SERIALPORT="/dev/ttyUSB0"

try:
	ser = serial.Serial(SERIALPORT, 9600)
	print "Ca marche"
except serial.SerialException:
	print "Port n'est pas dispo..."
	sys.exit()

nbrMail = int(feedparser.parse(PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH)["feed"]["fullcount"])
#nbrMail = 0

if nbrMail > 0:
	print "Des mails"
	ser.write("1")
else:
	print "Pas de mail, mais que fait le JUG ?"
	ser.write("0")

ser.close()








