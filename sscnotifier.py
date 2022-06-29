from bs4 import BeautifulSoup
import requests
import smtplib
  
# from tkinter import *

def sendmail(mail_address,msg):
	s = smtplib.SMTP('smtp.gmail.com',587)
  
# start TLS for security
	s.starttls()
  
# Authentication
	s.login("aditipant991@gmail.com", "nyqdevcbbfavzstg")
  
# message to be sent
	message =  str(msg)
  
# sending the mail
	s.sendmail("aditipant991@gmail.com", mail_address, message)
  
# terminating the session
# s.quit()

url="https://ssc.nic.in/"
r=requests.get(url)
html_content=r.content
soup=BeautifulSoup(html_content,'html.parser')

container=soup.findAll("div",{"class":"eachNotification"})
i=0
msg=" "
for x in container:
    date=x.span.text
    news=x.a.text.strip()
    link=x.a.get('href')
    # print(date)
    # print(news)
    # print(link)
    # print("\n")
    msg=msg+date+'\n'+news+'\n'+link+'\n'+'\n'
    i+=1
    if i==10:
        break

# print('msg',msg)
sendmail('satishrjk07@gmail.com',msg)