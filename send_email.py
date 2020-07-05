from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


server_name = 'smtp.gmail.com:587'
user_name = '*********'
pass_word = "*********"
receiver_EMAIL_ADDRESS = ['mail_id_1','mail_id_2','mail_id_3']
subject = "folder size data"
data_list = [('folder_1', 252),('folder_2', 156),('folder_3', 369)]


class SendMail:
	def __init__(self,server_name,user_name,pass_word,receiver_EMAIL_ADDRESS,subject,data_list):
		self.server_name = server_name
		self.user_name = user_name
		self.pass_word = pass_word
		self.receiver_EMAIL_ADDRESS = receiver_EMAIL_ADDRESS
		self.subject = subject
		self.data_list = data_list


	def send_email(self):
		try:
			server = smtplib.SMTP(self.server_name)
			server.ehlo()
			server.starttls()
			server.login(self.user_name, self.pass_word)
			the_msg = MIMEMultipart("alternative")
			the_msg["Subject"] = self.subject
			the_msg["From"] = self.user_name
			the_msg["To"] = ','.join(self.receiver_EMAIL_ADDRESS)
			plain_txt = "Folder Name with size"
			html_txt = ""
			html_txt += """<html><table border="1">
			<tr><th>Folder Name</th><th>Size</th></tr>"""
			html_txt += "<html>"
			for i in self.data_list:
				html_txt += "<tr>"
				html_txt += f"<td>{i[0]}</td>"
				html_txt += f"<td>{i[1]}</td>"
				html_txt += "</tr>"
			html_txt += "</table></html>"

			part_1 = MIMEText(plain_txt, "plain")
			part_2 = MIMEText(html_txt, "html")

			the_msg.attach(part_1)
			the_msg.attach(part_2)
			server.sendmail(self.user_name, self.receiver_EMAIL_ADDRESS, the_msg.as_string())
			server.quit()

		except:
			print("exception")

mail_obj = SendMail(server_name,user_name,pass_word,receiver_EMAIL_ADDRESS,subject)

mail_obj.send_email()
