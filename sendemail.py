
import smtplib
from email.mime.text import MIMEText

def send_email(nick_name, text):
	_user = "xxx"
	_pwd  = "xxx"
	_to   = "xxx"
	
	msg = MIMEText(text)
	msg["Subject"] = "软件更新提醒"
	msg["From"]    = nick_name+'<'+_user+'>'
	msg["To"]      = 'REA'+'<'+_to+'>'
	
	s = smtplib.SMTP_SSL("smtp.qq.com", 465)
	s.login(_user, _pwd)
	s.sendmail(_user, _to, msg.as_string())
	s.quit()

if __name__ == '__main__':
	send_email("这是一封测试邮件")
	pass
