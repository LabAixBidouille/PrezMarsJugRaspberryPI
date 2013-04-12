import serial, sys, time

SERIALPORT="/dev/ttyUSB0"
TIMETOWAIT=5

print "Verification de la connexion du port serie"
print "--- Connexion ---"
try:
	ser = serial.Serial(SERIALPORT, 9600)
	print "    Connexion effectuee"
except serial.SerialException:
	print "    Connexion echouee"
	sys.exit()

print "--- Envoi message ---"
print "    Signal 'Nouveau message'"
ser.write("1")

sys.stdout.write("        Wait " + str(TIMETOWAIT) + " sec : ") 
for i in range(0,TIMETOWAIT):
	sys.stdout.write('.')
	sys.stdout.flush()
	time.sleep(1)

print ""
print "    Signal 'Aucun nouveau message'"
ser.write("0")


sys.stdout.write("        Wait " + str(TIMETOWAIT) + " sec : ") 
for i in range(0,TIMETOWAIT):
	sys.stdout.write('.')
	sys.stdout.flush()
	time.sleep(1)

print ""
