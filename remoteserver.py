import ftplib
import urllib2
import time
while True : 
	my_ip = urllib2.urlopen('http://ip.42.pl/raw').read()
	out_file = open("uzhome.remotecomputer","w")
	out_file.write(my_ip)
	out_file.close()
	session = ftplib.FTP('ftp server','user','passwd')
	file = open('computername.remotecomputer','rb')                  # file to send
	session.storbinary('STOR computername.remotecomputer', file)     # send the file
	file.close()                                    # close file and FTP
	session.quit()
	print "update ip !!"
	time.sleep(1200)