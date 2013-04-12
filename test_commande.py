import serial, sys

SERIALPORT="/dev/ttyUSB0"

print "Verification de la connexion du port serie"
print "--- Connexion ---"
try:
	ser = serial.Serial(SERIALPORT, 9600)
	print "    Connexion effectuee"
except serial.SerialException:
	print "    Connexion echouee"
	sys.exit()

while 1:
	token = raw_input("Information : ")
	if token == "EOF" or token == "eof":
		break;

	ser.write(token)
	#ret = ser.read(8)
	#print "Retour : " + ret + "\n"

print "Bye bye !"
ser.close()
