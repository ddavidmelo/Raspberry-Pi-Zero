import ftplib
import os
import time
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


#for path, subdirs, files in os.walk(r'/media/pi/disk_D/complete'):
#        a.write("<li><a><span>"+str(path)[26:] +"</span></a></li>"+ os.linesep)

path = '/media/pi/disk_D/complete'
name_list = os.listdir(path)
full_list = [os.path.join(path,i) for i in name_list]
time_sorted_list = sorted(full_list, key=os.path.getmtime, reverse=True)

for pathF in time_sorted_list:
    stat = os.stat(pathF)
    a.write("<li><a><span>"+time.ctime(stat.st_mtime)[4:] + " -- " +pathF[26:]+"</span></a></li>"+ os.linesep)

a.close()


filename = "pilog.txt"
ftp = ftplib.FTP('files.000webhost.com')
ftp.login("WEBHOST_USER","WEBHOST_PASS")
ftp.cwd('/public_html')
ftp.retrlines('LIST')
myfile = open('/home/pi/Desktop/sitelog.txt','rb')
ftp.storbinary('STOR pilog.txt', myfile)
ftp.quit()
