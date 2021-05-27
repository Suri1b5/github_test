import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("avvarusurendrab5@gmail.com","Surendra7@")
server.sendmail("avvarusurendrab5@gmail.com",
                "surismart4@gmail.com",
                "sending message through python scripting")
server.quit()
