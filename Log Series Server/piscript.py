import ftplib
import os
import time;
import subprocess
from requests import get

localtime = time.asctime( time.localtime(time.time()) )

a = open("sitelog.txt", "w")
a.write("<li><a><span alt=\"highlight\" class=\"important\">&#215;</span><span class=\"tag\">"+localtime+"</span></a></li>"+os.linesep)

def getCPUtemperature():

        res = os.popen('vcgencmd measure_temp').readline()


        return("Temperature :" + res.replace("temp=","")[:-1])
a.write("<li><a><span alt=\"highlight\" class=\"important\">&#215;</span><span class=\"tag\">"+getCPUtemperature()+"</span></a></li>"+os.linesep)


def boot_info():
     item = {'start_time': 'Na','running_since':'Na'}
     try:
         item['running_duration'] = subprocess.check_output(['uptime -p'], shell=True)
         item['start_time'] = subprocess.check_output(['uptime -s'], shell=True)
     finally:
         return "Running Since :" + str(item['running_duration'][:-2]) + "|| Started on :" + str(item['start_time'][:-2])
a.write("<li><a><span alt=\"highlight\" class=\"important\">&#215;</span><span class=\"tag\">"+boot_info()+"</span></a></li>"+os.linesep)



ip = "Ext ip : " + get('https://api.ipify.org').text
a.write("<li><a><span alt=\"highlight\" class=\"important\">&#215;</span><span class=\"tag\">"+ip+"</span></a></li>"+os.linesep)


for path, subdirs, files in os.walk(r'/home/pi/complete'):
        a.write("<li><a><span>"+str(path)[18:] +"</span></a></li>"+ os.linesep)
a.close()


filename = "pilog.txt"
ftp = ftplib.FTP('***webhost.com')
ftp.login("***","***")
ftp.cwd('/public_html')
ftp.retrlines('LIST')
myfile = open('/home/pi/Desktop/sitelog.txt','rb')
ftp.storbinary('STOR pilog.txt', myfile)
ftp.quit()
