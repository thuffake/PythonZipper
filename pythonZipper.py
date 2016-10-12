import os
import re
import glob
import zipfile
import smtplib
from email import encoders
from email.message import Message
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


num1 = sum(1 for line in open('/python34/csc344/a1/assignment1'))
num2 = sum(1 for line in open('/python34/csc344/a2/assignment2'))
num3 = sum(1 for line in open('/python34/csc344/a3/assignment3'))
num4 = sum(1 for line in open('/python34/csc344/a4/assignment4'))
num5 = sum(1 for line in open('/python34/csc344/a5/assignment5'))
numl=[num1, num2, num3, num4,num5]
links=['a1/assignment1', 'a2/assignment2', 'a3/assignment3', 'a4/assignment4','a5/assignment5']
a1='/python34/csc344/a1'
a2='/python34/csc344/a2'
a3='/python34/csc344/a3'
a4='/python34/csc344/a4'
a5='/python34/csc344/a5'

n1='assignment1'
n2='assignment2'
n3='assignment3'
n4='assignment4'
n5='assignment5'

a=[a1,a2,a3,a4,a5]
n=[n1,n2,n3,n4,n5]
i=0

def clean_list(the_list):
    h = []
    for index in the_list:
	    if re.search('^[a-zA-Z]', index):
	    	h.append(index)					

    h = set(h)
    return h	

def parse():
    i=0
    for item in a:
        os.chdir(item)
        ch = ''
        lh = [];
        with open(n[i]) as f:
                while True:
                        c = f.read(1)
                        if not c:
                                break
                        if re.search("\w", c):
                                ch = ch + c
                        elif ch != '':
                                lh.append(ch)
                                ch = ''
        lh = clean_list(lh)

        with open('symbols', "w") as file_to_write:
                for index in lh:
                        file_to_write.write("[" + n[i] + ", " + index + "]\n")
        i = i + 1

def html():
    os.chdir('/python34/csc344/')
    html = open('csc344.html', '+w')
    html.write('<!doctype html')
    html.write('<html><head><title>CSC344 Assignments</title></head>')
    html.write('<body><h1>CSC344 Assignments</h1><hr />')
    b=0
    l=0
    for item in n:
            html.write('<h2>' + item + '</h2>')
            html.write('<p>Number of lines: ' + str(numl[b]) +'</p>')
            html.write('<p>Link:<a href="' +links[l]+'">' + links[l]+'</a></p>')
            b=b+1
            l=l+1
    html.write('</body>')
    html.write('</html>')
    html.close()

def con():
    sym1 ='/python34/csc344/a1/symbols'
    sym2 ='/python34/csc344/a2/symbols'
    sym3 ='/python34/csc344/a3/symbols'
    sym4 ='/python34/csc344/a4/symbols'
    sym5 ='/python34/csc344/a5/symbols'
    syms = [sym1,sym2,sym3,sym4,sym5]
    filenames = syms
    with open('symbols', 'w') as outfile:
        for fname in syms:
            with open(fname) as infile:
                outfile.write(infile.read())

def zip_file():
    p1 ='/python34/csc344/a1/assignment1'
    p2 ='/python34/csc344/a2/assignment2'
    p3 ='/python34/csc344/a3/assignment3'
    p4 ='/python34/csc344/a4/assignment4'
    p5 ='/python34/csc344/a5/assignment5'
    p = [p1,p2,p3,p4,p5]
    zf = zipfile.ZipFile("ThomasHuffaker-CSC344.zip", "w")
    
    for path in p:
        zf.write(path)
    
    zf.write('/python34/csc344/csc344.html')
    zf.write('/python34/csc344/symbols')
    zf.close()

    email = input('Enter the email to send to: ')
    user = "example@gmail.com"
    pswd = "examplepassword"
    
    msg = MIMEMultipart()
    	
    msg['From'] = user
    msg['To'] = email
    msg['Subject'] = "CSC344"

    attach = "ThomasHuffaker-CSC344.zip"
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(user, pswd)
    mailServer.sendmail(user, email, msg.as_string())
    mailServer.close()
    print("Email sent to " + email)


    
parse()
html()
con()
zip_file()

