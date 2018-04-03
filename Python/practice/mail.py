#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮箱服务器
smtpserver = 'smtp.126.com'

#发送邮箱用户、密码
user = 'mkesky@126.com'
password = 'maco.1012'

#发送邮箱
sender = 'mkesky@126.com'

#接收邮箱
receiver = '694064792@qq.com'

#发送邮件主题
subject = 'Python E-mail Test'

#编写HTML类型的邮件正文
msg = MIMEText('<html><h1>你好!</h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')

#连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()


'''
其实，这段代码也并不复杂，只要你理解使用过邮箱发送邮件，那么以下问题是你必须要考虑的：
你登录的邮箱帐号/密码
对方的邮箱帐号
邮件内容（标题，正文，附件）
邮箱服务器（SMTP.xxx.com/pop3.xxx.com）

'''