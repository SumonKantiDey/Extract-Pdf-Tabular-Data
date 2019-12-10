#python manage.py populate_text_extract
from django.core.management.base import BaseCommand
from text_extraction.models import *
from datetime import datetime
import dateparser
import email
import imaplib
import os
#/home/blueschemeai/project/textextraction/apis/djangoproject/text_extract/text_extraction/management/commands/clarksons

from text_extraction.management.commands.clarksons import MAIN_CODE as clarksonextract
import re
def read_data():
    detach_dir = './media/pdf/' #where the pdf content will save
    m = imaplib.IMAP4_SSL("outlook.office365.com")
    m.login('yourmail.com','######')
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
        if re_mail  == 'yourmail@clarksons.com' :
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
                    date=dateparser.parse(mail["Date"])
                    if not os.path.isfile(att_path) :
                        fp = open(att_path, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()
                    timefixture,timeassesment,spotass1,spotass2,spotfixture=clarksonextract(att_path)
                    try:
                        if  str(type(timefixture))=="<class 'pandas.core.frame.DataFrame'>":
                            if not timefixture.empty :
                                values=timefixture.values
                                for i in values:
                                    Clarksontimefixture(assesed12month=str(i[0]).replace("\n","").replace("\t",""), thisweekMonthly=str(i[1]).replace("\n","").replace("\t","")
                                                        , thisweekDaily=str(i[2]).replace("\n","").replace("\t",""),lastweekMonthly=str(i[3]).replace("\n","").replace("\t",""), lastweekDaily=str(i[4]).replace("\n","").replace("\t",""), week=date.isocalendar()[1], year=date.year).save()
                    except Exception as e:
                        pass
                        print(e)
                        errorlog(name=filename,type='clarkson',table='timefixture').save()
                    try:
                        if  spotfixture:
                            for i in spotfixture:
                                col=i.columns
                                col=[i.replace("\n","").replace("\t","") for i in col ]
                                if "Vessel" not in col:
                                    values=i.values.tolist()
                                    values.append(col)
                                else:
                                    values=i.values.tolist()
                                for j in values:
                                    Clarksonspotfixture(Vessel=str(j[0]).replace("\n","").replace("\t",""),CBM=str(j[1]).replace("\n","").replace("\t",""), Cargo=str(j[2]).replace("\n","").replace("\t",""), Voyage=str(j[3]).replace("\n","").replace("\t",""),
                                                        Laycan=str(j[4]).replace("\n","").replace("\t",""), Rate=str(j[5]).replace("\n","").replace("\t",""), Charterer=str(j[6]).replace("\n","").replace("\t",""), week=date.isocalendar()[1], year=date.year).save()

                    except Exception as e:
                        pass
                        print(e)
                        errorlog(name=filename, type='clarkson', table='spotfixture').save()
                    try:
                        if  str(type(spotass1))=="<class 'pandas.core.frame.DataFrame'>":
                            if not spotass1.empty :
                                values=spotass1.values.tolist()
                                values=values[1:]
                                for i in values:
                                        Clarksonspotass1(assesed=str(i[0]).replace("\n", "").replace("\t", ""),
                                        thisweekMonthly=str(i[1]).replace("\n", "").replace("\t", "")
                                        , thisweekDaily=str(i[2]).replace("\n", "").replace("\t", ""),
                                        lastweekMonthly=str(i[3]).replace("\n", "").replace("\t", ""),
                                        lastweekDaily=str(i[4]).replace("\n", "").replace("\t", ""),
                                        week=date.isocalendar()[1], year=date.year).save()
                    except Exception as e:
                        errorlog(name=filename, type='clarkson', table='spotass1').save()
                        print(e)
                        pass
                    try:
                        if  str(type(spotass2))=="<class 'pandas.core.frame.DataFrame'>":
                            if not spotass2.empty :
                                values=spotass2.values.tolist()
                                for i in values:
                                        Clarksonspotass2(Weeklyfrieghtass=str(i[0]).replace("\n", "").replace("\t", ""),
                                        thisweek=str(i[1]).replace("\n", "").replace("\t", "")
                                        , lastweek=str(i[2]).replace("\n", "").replace("\t", ""),
                                        week=date.isocalendar()[1], year=date.year).save()
                    except Exception as e:
                        print(e)
                        errorlog(name=filename, type='clarkson', table='spotass2').save()
                        pass
                    try:
                        if str(type(timeassesment)) == "<class 'pandas.core.frame.DataFrame'>":
                            if not timeassesment.empty:
                                values = timeassesment.values.tolist()
                                for j in values:
                                    Clarksontimeass(Vessel=str(j[0]).replace("\n","").replace("\t",""),CBM=str(j[1]).replace("\n","").replace("\t",""), Cargo=str(j[2]).replace("\n","").replace("\t",""), Area=str(j[3]).replace("\n","").replace("\t",""),
                                                        Period=str(j[4]).replace("\n","").replace("\t",""), Rate=str(j[5]).replace("\n","").replace("\t",""), Charterer=str(j[6]).replace("\n","").replace("\t",""), week=date.isocalendar()[1], year=date.year).save()

                    except Exception as e:
                        errorlog(name=filename, type='clarkson', table='timeassesment').save()
                        print(e)
                        pass

                else:
                    continue

class Command(BaseCommand):
    def handle(self, *args, **options):
        #val = bank_data_gen()
        read_data()
        print("Completed")



