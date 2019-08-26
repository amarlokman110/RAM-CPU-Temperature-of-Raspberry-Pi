# ---------------------------------------------------------
# ADD MODULES
# ---------------------------------------------------------
import time
import re, commands
import requests
import psutil
import os
import datetime

# ---------------------------------------------------------
# CHECK CPU TEMPERATURE
# ---------------------------------------------------------
def check_CPU_temp():
    temp = None
    err, msg = commands.getstatusoutput('vcgencmd measure_temp')
    if not err:
        m = re.search(r'-?\d\.?\d*', msg)
        try:
            temp = float(m.group())
        except:
            pass
    return temp, msg

temp, msg = check_CPU_temp()

# ---------------------------------------------------------
# MAIN FUNCTION
# ---------------------------------------------------------
if __name__ ==     '__main__':
    try:
        while True:
            dist = distance()
            ram = psutil.virtual_memory() #phymem_usage()
            ram_percent_used = ram.percent
            
            now = datetime.datetime.now()
            time_dict = now.strftime('%Y-%m-%d %H:%M:%S')
            print "RAM = ", ram.percent, "CPU = ", psutil.cpu_percent(), "Temp = ", temp 
            print "TIME: ", time_dict 
           
    except KeyboardInterrupt:
        print("Ending Script Coding")
