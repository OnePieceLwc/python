import smtplib
import email.utils
from email.mime.text import MIMEText
 
def send_email():
    message = MIMEText("content")
    message['To'] = email.utils.formataddr(('收件人姓名', '收件人邮箱'))
    message['From'] = email.utils.formataddr(('发送人姓名', '发件人邮箱'))
    message['Subject'] = '文件内容'
 
    server = smtplib.SMTP_SSL('smtp.qq.com', 465)
    server.login('发件人邮箱', '授权码')
 
    try:
        server.sendmail('发件人邮箱', ['收件人邮箱'], msg=message.as_string())
        server.quit()
        print("邮件发送成功")
    except Exception as e:
        print("邮件发送失败:", e)
 
# 调用函数发送邮件
send_email()
