import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class email_ops:
	def __init__(self, smtp_server, imap_server):
		self.smtp_server = smtp_server
		self.imap_server = imap_server
		self.header = None
		self.message = ''

	
	def send_message(self,param) :
		
		msg = MIMEMultipart()
		msg['From'] = param.get('login')
		rec = param.get('recipients')
		msg['To'] = ', '.join(rec)
		msg['Subject'] = param.get('subject')
		msg.attach(MIMEText(param.get('message')))
		
		smtp_msg = smtplib.SMTP(self.smtp_server, 587)
		# identify ourselves to smtp gmail client
		smtp_msg.ehlo()
		# secure our email with tls encryption
		smtp_msg.starttls()
		smtp_msg.login(param.get('login'), param.get('password'))
		smtp_msg.sendmail(param.get('login'), msg['To'], msg.as_string())
		smtp_msg.quit()


	def recieve_message(self,user_login, user_password):
		mail = imaplib.IMAP4_SSL(self.imap_server, 993)
		mail.login(user_login, user_password)

		mail.select()
		criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'

		result, data = mail.search(None, criterion)

		assert data[0], 'There are no letters with current header'
		
		latest_email_uid = data[0].split()[-1]
		result, data = mail.fetch(latest_email_uid, '(RFC822)')
		
		raw_email = data[0][1]
		
		self.message = email.message_from_bytes(raw_email)
		mail.close()
		mail.logout()
		
		return self.message
		
if __name__ == '__main__':

#	e_mail = email_ops("smtp.gmail.com","imap.gmail.com")
	e_mail = email_ops("mail.nic.ru","mail.nic.ru")

	param = dict()
	param['login'] = 'pantipov@mpkit.ru'
	param['password'] = 'some password'
	param['subject'] = 'Subject automated'
	param['recipients'] = ['pantipov@mpkit.ru'] #['vasya@email.com', 'petya@email.com']
	param['message'] = 'Сообщение просто так'

	
	e_mail.send_message(param)
	print(e_mail.recieve_message(param.get('login'), param.get('password')))
	
