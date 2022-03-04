import sys
import time
import visa

visa = visa.ResourceManager()
#print(visa.list_resources())
HP3458 = visa.open_resource('GPIB0::22::INSTR',send_end=True, read_termination= None, write_termination=None)
HP3458.write("PRESET NORM;OFORMAT ASCII;INBUF ON;TARM AUTO;TRIG AUTO;NPLC 10;MFORMAT 1;MEM OFF;NDIG 8;END ON")
print ''
HP3458.timeout = 25000
HP3458.clear()
HP3458.write('QFORMAT ALPHA')
print (HP3458.query('END ON;ID?'))[:8]
HP3458.write('FUNC 1') # DCV
HP3458.write('NPLC 200; NDIG 8') 
#time.sleep(5)

HP3245 = visa.open_resource('GPIB0::9::INSTR',send_end=True, read_termination= None, write_termination=None)
HP3245.write("MEM OFF;END ON")
print ''
HP3245.clear()
HP3245.timeout = 25000

HP3245.write('OFORMAT ASCII')
HP3245.write('RESET')
HP3245.write('INBUF ON')
HP3245.write('OUTBUF ON')
HP3245.write('APPLY DCV 10')

print (HP3245.query('END ON;IDN?'))
print (HP3245.query('CALNUM?'))
print (HP3245.query('CALSTR?'))
print (HP3245.query('CALEN?'))

HP3245.write('RESET')
HP3245.write('USE 0')
calAmps = raw_input('Want to also calibrate Amps? [Y} (any other ke for NO)')
if calAmps == "Y":
    HP3245.write('CAL')
    print ("Now calibrating Volts mode, Amps will follow in about 18min . . .")

else:
    HP3245.write('CAL VOLTS')
    print ("Now calibrating Volts mode . . .")

time.sleep(20)

for x in range(1, 45):
    val = str(HP3458.query('')) 
    print ("Reading " + str(x) + " " + str(val)[:16])
    HP3245.write('CAL VALUE' + str(val))
    time.sleep(20)
    
x = 45
HP3458.write('RANGE 100') # set to 100V range
val = str(HP3458.query('')) 
print ("Reading " + str(x) + " " + str(val)[:16])
HP3245.write('CAL VALUE' + str(val))
time.sleep(20)
HP3458.write('ARANGE') # set to auto range


for x in range(46, 48):
    val = str(HP3458.query('')) 
    print ("Reading " + str(x) + " " + str(val)[:16])
    HP3245.write('CAL VALUE' + str(val))
    time.sleep(20)

if calAmps != "Y":
    sys.exit(0)
    
else:
    HP3458.write('FUNC 6') # DCI

    raw_input('Switch connection to Amps, anykey when done ')
    print ("Now calibrating Amps mode . . .")
    time.sleep(20)

    for x in range(48, 72):
        val = str(HP3458.query('')) 
        print ("Reading " + str(x) + " " + str(val)[:16])
        HP3245.write('CAL VALUE' + str(val))
        time.sleep(20)
