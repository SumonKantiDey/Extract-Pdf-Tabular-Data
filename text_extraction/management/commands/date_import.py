#python manage.py populate_bank
from django.core.management.base import BaseCommand
from text_extraction.models import *
from datetime import datetime
import dateparser
import email
import dateutil
import pandas as pd
import imaplib
import os
#/home/blueschemeai/project/textextraction/apis/djangoproject/text_extract/text_extraction/management/commands/clarksons
#,,,,
from text_extraction.management.commands.clarksons import MAIN_CODE as clarksonextract
import re
def read_data():
     df = pd.read_excel('C:/Users/sumon/Downloads/year2018.xlsx')
     for row in range(len(df)):
         p = Braemartimeassesment2.objects.filter(year=df['Year'][row],week=df['Week Num'][row])
         if p:
             for val in p:
                 print(dateutil.parser.parse(str(df['From'][row])).date())
                 val.start_date = dateutil.parser.parse(str(df['From'][row])).date()
                 val.end_date = dateutil.parser.parse(str(df['To'][row])).date()
                 val.save()  
         else:
             continue     
class Command(BaseCommand):
    def handle(self, *args, **options):
        #val = bank_data_gen()
        read_data()
        print("Completed")



