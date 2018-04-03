# #coding=utf-8
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# #发送邮箱服务器
# smtpserver = 'smtp.qq.com'
#
# #发送邮箱用户、密码
# user = '694064792@qq.com'
# password = 'maco.1012'
#
# #发送邮箱
# sender = '694064792@qq.com'
#
# #接收邮箱
# receiver = 'ma.keke@njswtz.com'
#
# #发送邮件主题
# subject = 'Python E-mail Test'
#
# #编写HTML类型的邮件正文
# msg = MIMEText('<html><h1>你好!</h1></html>','html','utf-8')
# msg['Subject'] = Header(subject,'utf-8')
#
# #连接发送邮件
# smtp = smtplib.SMTP()
# smtp.connect(smtpserver)
# smtp.login(user,password)
# smtp.sendmail(sender,receiver,msg.as_string())
# smtp.quit()


'''
其实，这段代码也并不复杂，只要你理解使用过邮箱发送邮件，那么以下问题是你必须要考虑的：
你登录的邮箱帐号/密码
对方的邮箱帐号
邮件内容（标题，正文，附件）
邮箱服务器（SMTP.xxx.com/pop3.xxx.com）

'''



#yagmail 实现发邮件，   yagmail 可以更简单的来实现自动发邮件功能。
#github项目地址: https://github.com/kootenpv/yagmail

#安装  pip install yagmail

#简单例子
import yagmail

#链接邮箱服务器
yag = yagmail.SMTP(user='mkesky@126.com',password='maco.1012',host='smtp.126.com')

#邮箱正文
contents = ['This is the body,and here is just text http://somedomain/image.png',
            'you can find a audio file attached','/local/path/song.mp3']

#发送邮件
# yag.send['694064792@qq.com','subject',contents]

#给多个用户发送邮件
#发送邮件
# yag.send(['aa@126.com','bb@qq.com','cc@gmail.com'],'subject',contents)
#只需要将接收邮箱变成一个list即可；

#发送带附件的邮件
#发送邮件
yag.send('694064792@qq.com','发送邮件',contents,['F:\\123.txt','G:\\NBA.jpg'])
#只需要添加要发送的附件列表即可。



























