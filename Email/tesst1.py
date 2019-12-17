import smtplib
content="Hii This is Aneela"
cc=''
mail=smtplib.SMTP('smtp.gmail.com',525)
mail.ehlo()
mail.starttls()
mail.login('aneela.sarikonda@gmail.com','9963609943')
mail.sendmail('aneela.sarikonda@gmail.com','sk.jabida506@gmail.com',content)
mail.close()
