import ftplib
import os
import easygui as eg
ftphost = "uzbox.altervista.org"
ftpuser = "uzbox"
ftppass = "annepasswd"
def download(ftp,directory,file):
    ftp.cwd(directory)
    f = open(file,"wb")
    ftp.retrbinary("RETR " + file,f.write)
    f.close()
contype = raw_input('[l]an or [e]xternal:')
if contype == "e":
	msg = "Extarnal Connection Login"
	title = "PyRemote Client"
	fieldNames = ["ComputerName", "User", "Password"]
	fieldValues = []
	fieldValues = eg.multenterbox(msg,title, fieldNames)
	ftp = ftplib.FTP(ftphost)
	ftp.login(ftpuser, ftppass)
	while 1:
	    if fieldValues == None: break
	    errmsg = ""
	    for i in range(len(fieldNames)):
	        if fieldValues[i].strip() == "":
	            errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
	    if errmsg == "": 
	        break 
	    else:
	        fieldValues = eg.multpasswordbox(errmsg, title, fieldNames, fieldValues)

	print ("Reply was:", fieldValues)
	computer = fieldValues[0]
	download(ftp, "/", computer)
	fo = open(computer, "rw+")
	ip_computer = fo.readline()
	user = fieldValues[1]
	passwd = fieldValues[2]
	comand = "sshpass -p "
	comand += passwd
	comand += " ssh "
	comand += user
	comand += "@"
	comand += ip_computer
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