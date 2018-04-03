#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header


#发送邮箱服务器
smtpserver = 'smtp.126.com'

#发送邮箱用户/密码
user = 'mkesky@126.com'
password = 'mkesky1012'

#发送邮箱
sender = 'mkesky@126.com'

#接收邮箱
receiver = '694064792@qq.com'

#发送邮件主题
subject = 'Python e-mail test'

#编写HTML类型的邮件正文
msg = MIMEText('<html><h1>你好啊，啦啦啦；</h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')


#连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()







