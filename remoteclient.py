import ftplib
import os
def download(ftp,directory,file):
    ftp.cwd(directory)
    f = open(file,"wb")
    ftp.retrbinary("RETR " + file,f.write)
    f.close()
contype = raw_input('[l]an or [e]xternal:')
if contype == "e":
	ftp = ftplib.FTP("ftserver")
	ftp.login("user", "passwd")
	computer = raw_input('Enter computer name follow by .remotecomputer:')
	download(ftp, "/", computer)
	fo = open(computer, "rw+")
	ip_computer = fo.readline()
if contype == "l":
		ip_computer = raw_input('The lan ip of the computer:')
print "The computer ip is :"
print (ip_computer)
user = raw_input('Enter username:')
comand = "ssh "
comand += user
comand += "@"
comand += ip_computer
print (comand)
os.system(comand)