from django.core.management.base import BaseCommand
from text_extraction.models import *
from datetime import datetime
import dateparser
import email
import imaplib
import os
import re
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import traceback
def read_data():
    email = EmailMessage(
        subject='This is the mail subject',
        body='This is the body of the message',
        from_email=settings.EMAIL_HOST_USER,
        to=['yourmail@gmail.com'],
        cc=['yourmail@gmail.com'],
        #reply_to=['cheng@blah.com'],  # when the reply or reply all button is clicked, this is the reply to address, normally you don't have to set this if you want the receivers to reply to the from_email address
    )
    email.send(fail_silently=False)
    #email.content_subtype = 'html' # if the email body contains html tags, set this. Otherwise, omit it
    # try:
    #     email.send(fail_silently=False)
    #     return HttpResponseRedirect('/')
    # except Exception:
    #     print(traceback.format_exc()) 
    detach_dir = './media/pdf/' #where the pdf content will save
    m = imaplib.IMAP4_SSL("outlook.office365.com")
    m.login('yourmail','######')
    m.select("inbox")

    resp, items = m.search(None, 'UNSEEN') #ALL
    items = items[0].split()

    for emailid in items:
        resp, data = m.fetch(emailid, "(RFC822)") 
        email_body = data[0][1] 
        mail = email.message_from_bytes(email_body) 
        #temp = m.store(emailid,'+FLAGS', '\\Seen')
        m.expunge()

        if mail.get_content_maintype() != 'multipart':
            continue
        #extract the exect mail
        re_mail = re.search("<.*>",mail["From"])
        re_mail = re_mail.group(0)[1:-1]
        if re_mail == 'yourmail.com':
            broker_add = UserEmail.objects.get_or_create(title = mail["Subject"], email = re_mail)[0]
            broker_add.save()
            print("Brokers Email Address : ",re_mail)
            print("Brokers Email subject : ",mail["Subject"])
            print("Brokers Email Date : ", mail["Date"])
            print(dateparser.parse(mail["Date"]))
            for part in mail.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue

                filename = part.get_filename()
                filetype = re.search(".pdf", filename)
                print(filetype)
                if filetype:
                    att_path = os.path.join(detach_dir, filename)
                    print(att_path)
                    save_pdf = Pdf.objects.get_or_create(user = broker_add,pdf = att_path,date = dateparser.parse(mail["Date"]))[0]
                    save_pdf.save()
                    if not os.path.isfile(att_path) :
                        fp = open(att_path, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()
                else:
                    continue
