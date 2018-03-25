import smtplib
import time
import os
import subprocess

from requests import get
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "FromThis@gmail.com"
toaddr = "ToThis@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Log pi"

localtime = time.asctime( time.localtime(time.time()) )

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return("Temperature :" + res.replace("temp=","")[:-1])

def boot_info():
    item = {'start_time': 'Na','running_since':'Na'}
    try:
         item['running_duration'] = subprocess.check_output(['uptime -p'], shell=True)
         item['start_time'] = subprocess.check_output(['uptime -s'], shell=True)
    finally:
         return "Running Since :" + str(item['running_duration'][:-2]) + "|| Started on :" + str(item['start_time'][:-2])

ip = "Ext ip : " + get('https://api.ipify.org').text

bi = boot_info()
temperature = getCPUtemperature()
body = "\n".join([localtime,ip,bi,temperature])
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "auth.txt"
attachment = open("/home/pi/.../auth.txt", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "EmailPASSWORD")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

#https://www.afternerd.com/blog/how-to-send-an-email-using-python-and-smtplib/

#f = open("/var/log/auth.log")
#lines = f.readlines()
#print "".join(lines[-20:]).strip()
#a.write("<li><a><span>"+ "<br>".join(lines[-20:]).strip() +"</span></a></li>" )
#f.close()


