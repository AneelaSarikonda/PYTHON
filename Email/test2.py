import smtplib

toaddr = 'shaikallibasha8@gmail.com'
cc = ['sk.jabida506@gmail.com','shaikallibasha8@gmail.com']
#bcc = ['chairman@slayerscouncil.uk']
fromaddr = 'aneela.sarikonda@gmail.com'
message_subject = "This is an email sent from python "
message_text = "Hii This is Aneela"
message = "From: %s\r\n" % fromaddr+"To: %s\r\n" % toaddr+"CC: %s\r\n" % ",".join(cc)+"Subject: %s\r\n" % message_subject+"\r\n" +message_text
toaddrs = [toaddr] + cc 
server = smtplib.SMTP('smtp.gmail.com')
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, message)
server.ehlo()
server.starttls()
smtplib.SMTPSenderRefused(530, '5.7.0 Must issue a STARTTLS command first. w131sm6717736pfc.16 - gsmtp', 'aneela.sarikonda@gmail.com')

server.quit()
