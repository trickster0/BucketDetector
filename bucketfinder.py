#!/usr/bin/python
import urllib2
import urllib
import sys
import ssl
import socket

bucket = []
print "[+] S3 AWS Bucket Detector."
print "Author Thanasis Tserpelis aka trickster0\r\n"
if len(sys.argv) < 2:
	print "\nUsage: " + sys.argv[0] + " websitelist\n"
	sys.exit()

print "=============================================="
print "[*]Stage 1: Check headers for buckets."
print "[*]Stage 2: Check source code for buckets."
print "==============================================\r\n"
y = str(sys.argv[1])
def http(x):
    global bucket
    print "[+] Trying HTTP...\r\n"
    try:
        url = "http://" + x
        response = urllib2.urlopen(url,timeout = 10)
        html = response.read()
        finder = html.find("amazonaws.com")
        if finder > -1:
            print "\033[91m[+] Possibly using amazon bucket.\033[00m\r\n"
	    bucket.append(x) 
        else:
            print "[+] Sorry try another site.\r\n"
    except urllib2.URLError,e:
        print "[+] Website doesn't exist or doesn't support HTTP\r\n"
    except socket.timeout,e:
        print "[+] Socket timeout.\r\n"
    except socket.error,e:
        print "[+] Socket.error.\r\n"
    except ssl.SSLError,e:
        print "[+] SSL error.\r\n"
    except ssl.CertificateError,e :
        print "[+] Cert Error.\r\n"


def https(x):
    global bucket
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    print "[+] Trying HTTPS...\r\n"
    try:
        url = "https://" + x
        response = urllib2.urlopen(url, timeout =  10 , context=ctx)
        html = response.read()
        finder = html.find("amazonaws.com")
        if finder > -1:
            print "\033[91m[+] Possibly using amazon bucket.\033[00m\r\n"
	    bucket.append(x)
        else:
            print "[+] Sorry try another site.\r\n"
    except urllib2.URLError,e :
        print "[+] Website doesn't exist or doesn't support HTTPS!\r\n"
    except socket.timeout,e:
        print "[+] Socket.timeout.\r\n"
    except socket.error,e:
        print "[+] Socket.error.\r\n"
    except ssl.SSLError,e:
        print "[+] SSL error.\r\n"
    except ssl.CertificateError,e :
        print "[+] Cert Error.\r\n"


def http_header(x):
    global bucket
    print "[+] Trying HTTP header...\r\n"
    try:
        url = "http://" + x
        response = urllib2.urlopen(url, timeout = 10)
        html = str(response.info().headers)
        finder = html.find("amazonaws.com")
        if finder > -1:
            print "\033[91m[+] Possibly using amazon bucket.\033[00m\r\n"
	    bucket.append(x)
	    print html
        else:
            print "[+] Sorry wait for the next header.\r\n"
    except urllib2.URLError,e:
        print "[+] Website doesn't exist or doesn't support HTTP!\r\n"
    except socket.timeout,e:
        print "[+] Socket.timeout.\r\n"
    except socket.error,e:
        print "[+] Socket.error.\r\n"
    except ssl.SSLError,e:
        print "[+] SSL error.\r\n"
    except ssl.CertificateError,e :
        print "[+] Cert Error.\r\n"


def https_header(x):
    global bucket
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    print "[+] Trying HTTPS header...\r\n"
    try:
        url = "https://" + x
        response = urllib2.urlopen(url, timeout = 10, context=ctx)
        html = str(response.info())
        finder = html.find("amazonaws.com")
        if finder > -1:
            print "\033[91m[+] Possibly using amazon bucket.\033[00m\r\n"
	    bucket.append(x)
	    print html
        else:
            print "[+] Sorry wait for the next header.\r\n"
    except urllib2.URLError,e :
        print "[+] Website doesn't exist or doesn't support HTTPS!\r\n"
    except socket.timeout,e:
	print "[+] Socket.timeout.\r\n"
    except socket.error,e:
	print "[+] Socket.error.\r\n"
    except ssl.SSLError,e:
	print "[+] SSL error.\r\n"
    except ssl.CertificateError,e :
        print "[+] Cert Error.\r\n"

print "--------------------------------------------------------------------------\r\n"
print "\r\n[*] Initiating Stage 1.\r\n\r\n"
with open(y,"r") as ins:
    content = ins.read().splitlines()
    for line in content:
        print "--------------------------------------------------------------------------\r\n"
        print "[+] Trying " + line + "\r\n"
        http_header(line)
        https_header(line)
print "--------------------------------------------------------------------------\r\n"
print "\r\n[*] Initiating Stage 2.\r\n\r\n"
with open(y,"r") as ins:
    content = ins.read().splitlines()
    for line in content:
        print "--------------------------------------------------------------------------\r\n"
        print "[+] Trying " + line + "\r\n"
        http(line)
        https(line)


print "Printing Possible Buckets That Have Been Found!\r\n"
print '. '.join(bucket)
