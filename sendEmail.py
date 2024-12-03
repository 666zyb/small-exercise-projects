import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender =input("请输入发件人邮箱账号:")  # 发件人邮箱账号
my_pass = input("请输入发件人邮箱SMTP授权密码:")  # 发件人邮箱SMTP授权密码
my_user = input("请输入收件人邮箱账号:")  # 收件人邮箱账号
send_name=input("请输入发件人邮箱昵称:")
accept_name=input("请输入收件人邮箱昵称:")

def mail():
    ret = True
    try:
        msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr([send_name, my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([accept_name, my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = input("邮箱主题(标题):")  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")