import ast
import time
import datetime
import json
import pandas as pd
import re
import sys
import numpy as np
from django.shortcuts import render
from django_pandas.io import read_frame
from django.http import HttpResponse
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
    )

from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import traceback
from django.contrib.auth import authenticate
from django.http import HttpResponse,HttpResponseRedirect
from .serializers import ClarksonspotfixtureViewSerializer,ClarksontimefixtureViewSerializer,Clarksonspotassesment1ViewSerializer,Clarksonspotassesment2ViewSerializer,ClarksontimeassesmentViewSerializer
from .serializers import GibsonspotfixtureViewSerializer,GibsontimefixtureViewSerializer,GibsonspotassViewSerializer,GibsontimeassViewSerializer
from .serializers import FearngasspotfixtureViewSerializer,FearngastimefixtureViewSerializer,FearngasspotassementViewSerializer
from .serializers import BraemarspotfixtureViewSerializer,BraemarspotassesmentViewSerializer,BraemartimefixtureViewSerializer,Braemartimeassesment1ViewSerializer,Braemartimeassesment2ViewSerializer
from .serializers import SteemspotfixtureViewSerializer,SteemtimefixtureViewSerializer,SteemspotassViewSerializer,SteemtimeassViewSerializer
from .models import Clarksontimefixture,errorlog,Clarksonspotass1,Clarksonspotass2,Clarksontimeass,Clarksonspotfixture,UserEmail,Pdf
from .models import Gibsontimefixture,Gibsonspotfixture,Gibsonspotass,Gibsontimeass
from .models import Steemspotfixture,Steemtimefixture,Steemspotass,Steemtimeass
from .models import Fearngasspotfixture,Fearngastimefixture,Fearngasspotassement
from .models import Braemarspotfixture, Braemarspotassesment, Braemartimefixture, Braemartimeassesment1, Braemartimeassesment2
from .permissions import IsAnalyticsView,IsBrokerView
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework_jwt.settings import api_settings
from rest_framework import status, generics
def index(request):
    #logging.getLogger("error_logger").error("Hi I am here")
    logging.getLogger("error_logger").error("Hello")
    return HttpResponse("Hello World. First Django Project. ThePythonDjango.Com")


class Brokerlist(APIView):
    permission_classes = [IsAnalyticsView,]  # [IsAdminUser, ]
    def get(self, request, *args, **kwargs):
        json =[
            {
                'label': 'Clarksons',
                'value': 'Clarksons',
                'tables': [
                    {

                        'label': 'Spot Fixtures',
                        'value': 'Spot Fixtures',
                        'field': [
                            {'label': 'Vessel', 'value': 'vessel'}, {'label': 'Built', 'value': 'Built'}, {
                                'label': 'CBM', 'value': 'CBM'}, {'label': 'Charterer', 'value': 'Charterer'},
                            {'label': 'MTS', 'value': 'MTS'}, {'label': 'Load', 'value': 'Load'}, {'label': 'Disch', 'value': 'Disch'}, {
                                'label': 'Laycan', 'value': 'Laycan'}, {'label': 'Rate', 'value': 'Rate'},
                            {'label': 'Week', 'value': 'Week'}, {
                                'label': 'Year', 'value': 'Year'}


                        ]
                    },
                    {
                        'label': 'TC Fixtures',
                        'value': 'TC Fixtures',
                  						'field': [{"label": "Vessel", "value": "Vessel"}, {"label": "CBM", "value": "CBM"}, {"label": "Charterer", "value": "Charterer"}, {"label": "MTS", "value": "MTS"}, {"label": "Area", "value": "Area"}, {"label": "Period", "value": "Period"},
                                                                    {"label": "Rate", "value": "Rate"}, {"label": "Week", "value": "Week"}, {"label": "Year", "value": "Year"}]
                    },
                    {
                        'label': 'VLGC Spot TCE Rates',
                        'value': 'VLGC Spot TCE Rates',
                        'field': [{"label": "Assessed", "value": "assesed"}, {"label": "This Week Monthly", "value": "thisweekMonthly"}, {"label": "This Week Daily", "value": "thisweekDaily"}, {"label": "Last Week Monthly", "value": "lastweekMonthly"}, {"label": "Last Week Daily", "value": "lastweekDaily"}, {"label": "Week", "value": "Week"},
                                  {"label": "Year", "value": "Year"}
                                  ]
                    },
                    {
                        'label': 'Weekly Spot Freight Assessments',
                        'value': 'Weekly Spot Freight Assessments',
                        'field': [{"label": "Weekly Freight Assessment", "value": "Weeklyfrieghtass"}, {"label": "This Week", "value": "thisweek"}, {"label": "Last Week", "value": "lastweek"}, {"label": "Week", "value": "Week"}, {"label": "Year", "value": "Year"}
                                  ]
                    },
                    {
                        'label': '12M TC Assessments',
                        'value': '12M TC Assessments',
                        'field': [{"label": "Assessed 12 Month", "value": "assesed12month"}, {"label": "This Week Monthly", "value": "thisweekMonthly"}, {"label": "This Week Daily", "value": "thisweekDaily"}, {"label": "Last Week Monthly", "value": "lastweekMonthly"}, {"label": "Last Week Daily", "value": "lastweekDaily"}, {"label": "Week", "value": "Week"}, {"label": "Year", "value": "Year"}]
                    }

                ]
            },
            {
                'label': 'Gibson',
                'value': 'Gibson',
                'tables': [
                    {
                        'label': 'Spot Fixtures',
                        'value': 'Spot Fixtures',
                        'field': [
                            {'label': 'Vessel', 'value': 'vessel'}, {'label': 'Built', 'value': 'Built'},
                            {'label': 'CBM', 'value': 'CBM'}, {'label': 'Charterer', 'value': 'Charterer'},
                            {'label': 'MTS', 'value': 'MTS'}, {'label': 'Load', 'value': 'Load'},
                            {'label': 'Disch', 'value': 'Disch'}, {'label': 'Laycan', 'value': 'Laycan'},
                            {'label': 'Rate', 'value': 'Rate'},
                            {'label': 'Week', 'value': 'Week'}, {'label': 'Year', 'value': 'Year'}

                        ]
					},
					{
                        'label': 'TC Fixtures',
                        'value': 'TC Fixtures',
                        'field': [{"label":"Vessel","value":"Vessel"},{"label":"CBM","value":"CBM"},{"label":"Charterer","value":"Charterer"},{"label":"Period","value":"Period"},{"label":"Delivery","value":"Delivery"},{"label":"Redelivery","value":"Redelivery"},
                  {"label":"Laycan","value":"Laycan"},{"label":"Rate","value":"Rate"},{"label":"Week","value":"Week"},{"label":"Year","value":"Year"}]
				    },
					{
                        'label': 'Spot Assessments',
                        'value': 'Spot Assessments',
                        'field': [{"label":"MTS","value":"MTS"},{"label":"Cargo","value":"Cargo"},{"label":"Load","value":"Load"},{"label":"Disch","value":"Disch"},{"label":"Rate","value":"Rate"},{"label":"Rate Previous Week","value":"previousweek"},{"label":"Week","value":"Week"},{"label":"Year","value":"Year"}]
					},
					{
                        'label': '12M TC Assessments',
                        'value': '12M TC Assessments',
                        'field': [{"label":"CBM","value":"CBM"},{"label":"Type","value":"Type"},{"label":"Region","value":"Region"},{"label":"Rate Monthly","value":"RateMonthly"},{"label":"Rate Previous Weekpcm","value":"RatePreviousWeekpcm"},
							{"label":"Rate Daily","value":"RateDaily"},{"label":"Rate Daily Previous Week","value":"RateDailyPreviousWeek"},{"label":"Week","value":"Week"},{"label":"Year","value":"Year"}]

                    },

                ]
            },
             {
                'label': 'Steem1960',
                'value': 'Steem1960',
                'tables': [
                    {
                        'label': 'Spot Fixtures',
                        'value': 'Spot Fixtures',
                        'field': [
                            {'label': 'Vessel', 'value': 'vessel'}, {'label': 'Built', 'value': 'Built'},
                            {'label': 'CBM', 'value': 'CBM'}, {'label': 'Charterer', 'value': 'Charterer'},
                            {'label': 'MTS', 'value': 'MTS'}, {'label': 'Load', 'value': 'Load'},
                            {'label': 'Disch', 'value': 'Disch'}, {'label': 'Laycan', 'value': 'Laycan'},
                            {'label': 'Rate', 'value': 'Rate'},
                            {'label': 'Week', 'value': 'Week'}, {'label': 'Year', 'value': 'Year'}

                        ]
					},
					{
						'label': 'TC Fixtures',
						'value': 'TC Fixtures',
						'field': [
                            {"label":"Vessel","value":"Vessel"},{"label":"Built","value":"Built"},{"label":"CBM","value":"CBM"},{"label":"Charterer","value":"Charterer"},
							{"label":"Period","value":"Period"},{"label":"Cargo","value":"Cargo"},{"label":"Delivery","value":"Delivery"},{"label":"Redelivery","value":"Redelivery"},
							{"label": "Laycan", "value": "Laycan"}, {"label": "Rate", "value": "Rate"}, {"label": "Week", "value": "Week"}, {"label": "Year", "value": "Year"}
                            ]
					},
					{
						'label': 'Spot Assessments',
                        'value': 'Spot Assessments',
						'field': [
                            {"label": "MTS", "value": "MTS"}, {"label": "Cargo", "value": "Cargo"}, {"label": "Load", "value": "Load"}, {"label": "Disch", "value": "Disch"},
						    {"label": "Rate", "value": "Rate"}, {"label": "Week", "value": "Week"}, {"label": "Year", "value": "Year"}]
                    },
                    {
                        'label': '12M TC Assessments',
                        'value': '12M TC Assessments',
                        'field': [
                            {"label":"CBM","value":"CBM"},{"label":"Rate Per Month","value":"RatePerMonth"},{"label":"Type","value":"Type"},
						    {"label":"Week","value":"Week"},{"label":"Year","value":"Year"}]

					}
				]
            },
            {
                'label': 'Fearngas',
                'value': 'Fearngas',
                'tables': [
                    {
                        'label': 'Spot Fixtures',
                        'value': 'Spot Fixtures',
                        'field': [
                            {'label': 'Vessel', 'value': 'vessel'}, {'label': 'Built', 'value': 'Built'},
                            {'label': 'CBM', 'value': 'CBM'}, {'label': 'Charterer', 'value': 'Charterer'},
                            {'label': 'MTS', 'value': 'MTS'}, {'label': 'Load', 'value': 'Load'},
                            {'label': 'Disch', 'value': 'Disch'}, {'label': 'Laycan', 'value': 'Laycan'},
                            {'label': 'Rate', 'value': 'Rate'},
                            {'label': 'Week', 'value': 'Week'}, {'label': 'Year', 'value': 'Year'}
                        ]
					},
					{
                        'label': 'TC Fixtures',
                        'value': 'TC Fixtures',
                        'field': [{"label":"Vessel","value":"Vessel"},{"label":"CBM","value":"CBM"},{"label":"Charterer","value":"Charterer"},{"label":"Period","value":"Period"},
						 {"label":"Delivery","value":"Delivery"},{"label":"Redelivery","value":"Redelivery"},{"label":"Laycan","value":"Laycan"},{"label":"Rate","value":"Rate"},
						 {"label":"Week","value":"Week"},{"label":"Year","value":"Year"}]
					},
					{
                        'label': 'Spot Assessments',
                  						'value': 'Spot Assessments',
                        'field': [{"label": "Type", "value": "Type"}, {"label": "CBM", "value": "CBM"}, {"label": "This Week", "value": "ThisWeek"},
								{"label":"change","value":"change"},{"label":"Week","value":"Week"},{"label":"Year","value":"Year"}]


                    }

                ]
            },
            {
                'label': 'Braemar',
                'value': 'Braemar',
                'tables': [
                    {
                        'label': 'Spot Fixtures',
                        'value': 'Spot Fixtures',
                        'field': [
                            {'label': 'Vessel', 'value': 'vessel'}, {
                                'label': 'Built', 'value': 'Built'},
                            {'label': 'CBM', 'value': 'CBM'}, {
                                'label': 'Charterer', 'value': 'Charterer'},
                            {'label': 'MTS', 'value': 'MTS'}, {
                                'label': 'Load', 'value': 'Load'},
                            {'label': 'Disch', 'value': 'Disch'}, {
                                'label': 'Laycan', 'value': 'Laycan'},
                            {'label': 'Rate', 'value': 'Rate'},
                            {'label': 'Week', 'value': 'Week'}, {
                                'label': 'Year', 'value': 'Year'}

                        ]
                    },
               		{
                        'label': 'TC Fixtures',
                        'value': 'TC Fixtures',
                        'field': [
                                    {"label": "Vessel", "value": "Vessel"}, {"label": "Cbm", "value": "Cbm"}, {"label": "Charterer", "value": "Charterer"},
                                    {"label": "Built", "value": "Built"}, {"label": "Period", "value": "Period"}, {
                                      "label": "Delivery", "value": "Delivery"}, {"label": "Redelivery", "value": "Redelivery"},
                                    {"label": "Laycan", "value": "Laycan"}, {"label": "Hire", "value": "Hire"}, {"label": "Week", "value": "Week"}, {"label": "Year", "value": "Year"}
                                ]
                    },
               		{
                        'label': '12Mth TC',
                        'value': '12Mth TC',
                        'field': [
                                    {"label": "CBM", "value": "CBM"}, {"label": "Type", "value": "Type"}, {"label": "Region", "value": "Region"}, {"label": "Rate", "value": "Rate"},
                                    {"label": "Week", "value": "Week"}, {"label": "Year", "value": "Year"}
                                ]
                    },
               		{
                        'label': '1 - 3 Mth TC',
                        'value': '1 - 3 Mth TC',
                        'field': [
                                    {"label": "CBM", "value": "CBM"}, {"label": "Pcm", "value": "Pcm"}, {"label": "Type", "value": "Type"},
                                    {"label": "Week", "value": "Week"}, {"label": "Year", "value": "Year"}
                                ]
                    },
               		{
                        'label': 'Spot Assesment',
                        'value': 'Spot Assesment',
                        'field': [
                                    {"label": "Load", "value": "Load"}, {"label": "Disch", "value": "Disch"}, {"label": "MTS", "value": "MTS"}, {"label": "Type", "value": "Type"}, {"label": "Rate", "value": "Rate"},
                                    {"label": "Week", "value": "Week"}, {"label": "Year", "value": "Year"}
                                  ]
                    }

                ]
            }
        ]
    
        return Response(json)
class BrokerYearWeekDate(APIView):
    def get(self, request, *args, **kwargs):
        # def str_to_class(str):
        #     return getattr(sys.modules[__name__], str)
        broker_name = ['clarkson','gibson','steem1960','fearngas','braemar']
        def str_to_obj(s):
            clarkson = [Clarksontimefixture,Clarksonspotass1,Clarksonspotass2,Clarksontimeass,Clarksonspotfixture]
            gibson = [Gibsontimefixture,Gibsonspotfixture,Gibsonspotass,Gibsontimeass]
            fearngas = [Fearngasspotfixture,Fearngastimefixture,Fearngasspotassement]
            steem1960 = [Steemspotfixture,Steemtimefixture,Steemspotass,Steemtimeass]
            braemar = [Braemarspotfixture,Braemarspotassesment,Braemartimefixture,Braemartimeassesment1,Braemartimeassesment2]
            if s == 'clarkson':
                return clarkson
            elif s == 'gibson':
                return gibson
            elif s == 'steem1960':
                return steem1960
            elif s == 'fearngas':
                return fearngas
            elif s == 'braemar':
                return braemar
        for name in broker_name:
            if kwargs['name'] == name:
                #broker_name = str_to_class(kwargs['name'])
                store = []
                print(str_to_obj(name))
                for broker in str_to_obj(name):
                    queryset = broker.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
                    for item in queryset:
                        sec_dic = {
                            'start_date': item['start_date'],
                            'end_date' : item['end_date']
                        }
                        store.append(sec_dic)
                week_date = list({(v['start_date'], v['start_date']):v for v in store}.values())
                print(week_date)
        return Response(week_date[0])
#Clarkson Year Week
class Clarksonyearweek(APIView):

    def get(self, request, *args, **kwargs):
        lst = [Clarksontimefixture,Clarksonspotass1,Clarksonspotass2,Clarksontimeass,Clarksonspotfixture]
        year_val = set(x.year for l in lst for x in l.objects.all())
        data = []
        for val in year_val:
            queryset = set(x.week for l in lst for x in l.objects.filter(year=val))
            tmp = []
            for item in queryset:
                tmp.append(item)
            sec_dic = {
                'year':str(val),
                'weeks':tmp
            }
            
            data.append(sec_dic)
            #data.append(arr)
        return Response({'results': data})

#spot fixture
class ClarksonspotfixtureView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClarksonspotfixtureViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Clarksonspotfixture.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                    "Vessel":item['Vessel'],"CBM":item['CBM'],
                    "Cargo":item['Cargo'],"Voyage":item['Voyage'],"Laycan":item['Laycan'],
                   "Rate":item['Rate'],"Charterer":item['Charterer'],"week":item['week'],
                   "year":item['year']
                   }
            data.append(dic)
        columns=[{"label":"Vessel","value":"Vessel"},{"label":"CBM","value":"CBM"},{"label":"Cargo","value":"Cargo"},{"label":"Voyage","value":"Voyage"},{"label":"Laycan","value":"Laycan"},{"label":"Rate","value":"Rate"},{"label":"Charterer","value":"Charterer"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} }) 

#Time fixture       
class ClarksontimefixtureView(APIView):
    serializer_class = ClarksontimefixtureViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Clarksontimefixture.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                    "assesed12month":item['assesed12month'],"thisweekMonthly":item['thisweekMonthly'],
                    "thisweekDaily":item['thisweekDaily'],"lastweekMonthly":item['lastweekMonthly'],"lastweekDaily":item['lastweekDaily'],
                    "week":item['week'],"year":item['year']
                   }
            data.append(dic)
        columns=[{"label":"assesed12month","value":"assesed12month"},{"label":"thisweekMonthly","value":"thisweekMonthly"},{"label":"thisweekDaily","value":"thisweekDaily"},{"label":"lastweekMonthly","value":"lastweekMonthly"},{"label":"lastweekDaily","value":"lastweekDaily"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} }) 
        
#Clark spot Ass1
class Clarksonspotassesment1View(APIView):
    serializer_class = Clarksonspotassesment1ViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Clarksonspotass1.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "assesed":item['assesed'],"thisweekMonthly":item['thisweekMonthly'],
                "thisweekDaily":item['thisweekDaily'],"lastweekMonthly":item['lastweekMonthly'],"lastweekDaily":item['lastweekDaily'],
                "week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"assesed","value":"assesed"},{"label":"thisweekMonthly","value":"thisweekMonthly"},{"label":"thisweekDaily","value":"thisweekDaily"},{"label":"lastweekMonthly","value":"lastweekMonthly"},{"label":"lastweekDaily","value":"lastweekDaily"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} }) 

#Clark spot Ass2
class Clarksonspotassesment2View(APIView):
    serializer_class = Clarksonspotassesment2ViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Clarksonspotass2.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "Weeklyfrieghtass":item['Weeklyfrieghtass'],"thisweek":item['thisweek'],
                "lastweek":item['lastweek'],"week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"Weeklyfrieghtass","value":"Weeklyfrieghtass"},{"label":"thisweek","value":"thisweek"},{"label":"lastweek","value":"lastweek"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} }) 

#Clarkson TimeAss
class ClarksontimeassesmentView(APIView):
    serializer_class = ClarksontimeassesmentViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Clarksontimeass.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "Vessel":item['Vessel'],"CBM":item['CBM'],
                "Cargo":item['Cargo'],"Area":item['Area'],"Period":item['Period'],"Rate":item['Rate'],"Charterer":item['Charterer'],
                "week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"Vessel","value":"Vessel"},{"label":"CBM","value":"CBM"},{"label":"Cargo","value":"Cargo"},{"label":"Area","value":"Area"},{"label":"Period","value":"Period"},{"label":"Rate","value":"Rate"},{"label":"Charterer","value":"Charterer"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} }) 

#For gibson
class Gibsonyearweek(APIView):

    def get(self, request, *args, **kwargs):
        lst = [Gibsontimefixture,Gibsonspotfixture,Gibsonspotass,Gibsontimeass]
        year_val = set(x.year for l in lst for x in l.objects.all())
        data = []
        for val in year_val:
            queryset = list(set(x.week for l in lst for x in l.objects.filter(year=val)))[::-1]
            
            tmp = []
            for item in queryset:
                tmp.append(item)
            sec_dic = {
                'year':str(val),
                'weeks':tmp
            }
            
            data.append(sec_dic)
            #data.append(arr)
        return Response({'results': data})
       
class GibsonspotfixtureView(APIView):
    serializer_class = GibsonspotfixtureViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Gibsonspotfixture.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "Vessel":item['Vessel'],"CBM":item['CBM'],"Mts":item['Mts'],"Cargo":item['Cargo'],"Load":item['Load'],
                "Disch":item['Disch'],"Laycan":item['Laycan'],"Rate":item['Rate'],"Charterer":item['Charterer'],"week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"Vessel","value":"Vessel"},{"label":"CBM","value":"CBM"},{"label":"Mts","value":"Mts"},{"label":"Cargo","value":"Cargo"},{"label":"Load","value":"Load"},{"label":"Disch","value":"Disch"},{"label":"Laycan","value":"Laycan"},{"label":"Rate","value":"Rate"},{"label":"Charterer","value":"Charterer"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} })

class GibsontimefixtureView(APIView):
    serializer_class = GibsontimefixtureViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Gibsontimefixture.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "Vessel":item['Vessel'],"CBM":item['CBM'],"Period":item['Period'],"Delivery":item['Delivery'],"Redelivery":item['Redelivery'],
                "Laycan":item['Laycan'],"Hire":item['Hire'],"Charterer":item['Charterer'],"week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"Vessel","value":"Vessel"},{"label":"CBM","value":"CBM"},{"label":"Period","value":"Period"},{"label":"Delivery","value":"Delivery"},{"label":"Redelivery","value":"Redelivery"},{"label":"Laycan","value":"Laycan"},{"label":"Hire","value":"Hire"},{"label":"Charterer","value":"Charterer"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} })

class GibsonspotassView(APIView):
    serializer_class = GibsonspotassViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Gibsonspotass.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "Mts":item['Mts'],"Country":item['Country'],"Usperpmt":item['Usperpmt'],"Previousweek":item['previousweek'],"week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"Mts","value":"Mts"},{"label":"Country","value":"Country"},{"label":"Usperpmt","value":"Usperpmt"},{"label":"Previousweek","value":"Previousweek"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} })

class GibsontimeassView(APIView):
    serializer_class = GibsontimeassViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Gibsontimeass.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "Cbm":item['Cbm'],"Type":item['type'],"USperpcm":item['USperpcm'],"Previousweekpcm":item['previousweekpcm'],
                "USperday":item['USperday'],"Previousweekday":item['previousweekday'],"week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"Cbm","value":"Cbm"},{"label":"Type","value":"Type"},{"label":"USperpcm","value":"USperpcm"},{"label":"Previousweekpcm","value":"Previousweekpcm"},
                  {"label":"USperday","value":"USperday"},{"label":"Previousweekday","value":"Previousweekday"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} })

#For Steem1960
class Steemyearweek(APIView):
    def get(self, request, *args, **kwargs):
        lst = [Steemspotfixture, Steemtimefixture, Steemspotass, Steemtimeass]
        year_val = set(x.year for l in lst for x in l.objects.all())
      
        #year_val = set([e.year for e in Steemspotfixture.objects.all()])
        data = []
        for val in year_val:
            #queryset = set([e.week for e in Steemspotfixture.objects.filter(year=val)])
            queryset = set(x.week for l in lst for x in l.objects.filter(year=val))
            
            tmp = []
            for item in queryset:
                tmp.append(item)
            sec_dic = {
                'year':str(val),
                'weeks':tmp
            }
            data.append(sec_dic)
            #data.append(arr)
        return Response({'results': data})
class SteemspotfixtureView(APIView):
    serializer_class = SteemspotfixtureViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Steemspotfixture.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        print(queryset)
        data = []
        for item in queryset:
            dic = {
                "Vessel":item['Vessel'],"Built":item['Built'],"CBM":item['CBM'],"Charterer":item['Charterer'],"Qty":item['Qty'],
                "Cargo":item['Cargo'],"LoadPort":item['LoadPort'],"DischPort":item['DischPort'],"Laycan":item['Laycan'],"Freight":item['Freight'],"week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"Vessel","value":"Vessel"},{"label":"Built","value":"Built"},{"label":"CBM","value":"CBM"},{"label":"Charterer","value":"Charterer"},
                 {"label":"Qty","value":"Qty"},{"label":"Cargo","value":"Cargo"},{"label":"LoadPort","value":"LoadPort"},{"label":"DischPort","value":"DischPort"},
                 {"label":"Laycan","value":"Laycan"},{"label":"Freight","value":"Freight"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} })

class SteemtimefixtureView(APIView):
    serializer_class = SteemtimefixtureViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Steemtimefixture.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "Vessel":item['Vessel'],"Built":item['Built'],"CBM":item['CBM'],"Charterer":item['Charterer'],"Period":item['Period'],
                "Cargo":item['Cargo'],"DeliveryRedel":item['DeliveryRedel'],"Laycan":item['Laycan'],"Hire":item['Hire'],"week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"Vessel","value":"Vessel"},{"label":"Built","value":"Built"},{"label":"CBM","value":"CBM"},{"label":"Charterer","value":"Charterer"},
            {"label":"Period","value":"Period"},{"label":"Cargo","value":"Cargo"},{"label":"DeliveryRedel","value":"DeliveryRedel"},
            {"label":"Laycan","value":"Laycan"},{"label":"Hire","value":"Hire"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} })

class SteemspotassView(APIView):
    serializer_class = SteemspotassViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Steemspotass.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "size_mts":item['size_mts'],"cargo":item['cargo'],"trade":item['trade'],
                "USDperMT":item['USDperMT'],"week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"size_mts","value":"size_mts"},{"label":"cargo","value":"cargo"},{"label":"trade","value":"trade"},
                 {"label":"USDperMT","value":"USDperMT"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} })

class SteemtimeassView(APIView):
    serializer_class = SteemtimeassViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Steemtimeass.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "VesselSize":item['VesselSize'],"HireperUSDpcm":item['HireperUSDpcm'],
                "week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"VesselSize","value":"VesselSize"},{"label":"HireperUSDpcm","value":"HireperUSDpcm"},
                 {"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} })


#For Fearngas
class Fearngasyearweek(APIView):
    def get(self, request, *args, **kwargs):
        year_val = set([e.year for e in Fearngasspotfixture.objects.all()])
        data = []
        for val in year_val:
            queryset = set([e.week for e in Fearngasspotfixture.objects.filter(year=val)])
            tmp = []
            for item in queryset:
                tmp.append(item)
            sec_dic = {
                'year':str(val),
                'weeks':tmp
            }
            data.append(sec_dic)
            #data.append(arr)
        return Response({'results': data})

class FearngasspotfixtureView(APIView):
    serializer_class = FearngasspotfixtureViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Fearngasspotfixture.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "Vessel":item['Vessel'],"Cbm":item['Cbm'],"Type":item['Type'],"LoadDisch":item['LoadDisch'],"Laycan":item['Laycan'],
                "Rate":item['Rate'],"Charterer":item['Charterer'],"week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"Vessel","value":"Vessel"},{"label":"Cbm","value":"Cbm"},{"label":"Type","value":"Type"},
                 {"label":"LoadDisch","value":"LoadDisch"},{"label":"Laycan","value":"Laycan"},{"label":"Rate","value":"Rate"},
                 {"label":"Charterer","value":"Charterer"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} })

class FearngastimefixtureView(APIView):
    serializer_class = FearngastimefixtureViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Fearngastimefixture.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "Vessel":item['Vessel'],"Cbm":item['Cbm'],"Period":item['Period'],"LoadDisch":item['LoadDisch'],"Laycan":item['Laycan'],
                "Rate":item['Rate'],"Charterer":item['Charterer'],"week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"Vessel","value":"Vessel"},{"label":"Cbm","value":"Cbm"},{"label":"Period","value":"Period"},
                 {"label":"LoadDisch","value":"LoadDisch"},{"label":"Laycan","value":"Laycan"},{"label":"Rate","value":"Rate"},
                 {"label":"Charterer","value":"Charterer"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} })

class FearngasspotassementView(APIView):
    serializer_class = FearngasspotassementViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Fearngasspotassement.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "spotmarket":item['spotmarket'],"Thisweek":item['Thisweek'],"change":item['change'],
                "week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"spotmarket","value":"spotmarket"},{"label":"Thisweek","value":"Thisweek"},
                 {"label":"change","value":"change"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} })
#For Breamar
class Braemaryearweek(APIView):
    def get(self, request, *args, **kwargs):
        lst = [Braemarspotfixture,Braemarspotassesment,Braemartimefixture,Braemartimeassesment1,Braemartimeassesment2]
        year_val = set(x.year for l in lst for x in l.objects.all())
    
        data = []
        for val in year_val:
            queryset = set(x.week for l in lst for x in l.objects.filter(year=val))
            
            tmp = []
            for item in queryset:
                tmp.append(item)
            sec_dic = {
                'year':str(val),
                'weeks':tmp
            }
            data.append(sec_dic)
        return Response({'results': data})

class BraemarspotfixtureView(APIView):
    serializer_class = BraemarspotfixtureViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Braemarspotfixture.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "Charterer":item['Charterer'],"Vessel":item['Vessel'],"Cbm":item['Cbm'],"YOB":item['YOB'],"Cargo":item['Cargo'],
                "Load":item['Load'],"Discharge":item['Discharge'],"Laycan":item['Laycan'],"Rate":item['Rate'],
                "week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"Charterer","value":"Charterer"},{"label":"Vessel","value":"Vessel"},{"label":"Cbm","value":"Cbm"},
                 {"label":"YOB","value":"YOB"},{"label":"Cargo","value":"Cargo"},{"label":"Load","value":"Load"},{"label":"Discharge","value":"Discharge"},
                 {"label":"Laycan","value":"Laycan"},{"label":"Rate","value":"Rate"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} })

class BraemarspotassesmentView(APIView):
    serializer_class = BraemarspotassesmentViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Braemarspotassesment.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "Region":item['Region'],"Price":item['price'],"week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"Region","value":"Region"},{"label":"Price","value":"price"},
                 {"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} })

class BraemartimefixtureView(APIView):
    serializer_class = BraemartimefixtureViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Braemartimefixture.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "Charterer":item['Charterer'],"Vessel":item['Vessel'],"Cbm":item['Cbm'],"YOB":item['YOB'],"Period":item['Period'],
                "Del":item['Del'],"Redel":item['Redel'],"Laycan":item['Laycan'],"Hire":item['Hire'],
                "week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"Charterer","value":"Charterer"},{"label":"Vessel","value":"Vessel"},{"label":"Cbm","value":"Cbm"},
                 {"label":"YOB","value":"YOB"},{"label":"Period","value":"Period"},{"label":"Del","value":"Del"},{"label":"Redel","value":"Redel"},
                 {"label":"Laycan","value":"Laycan"},{"label":"Hire","value":"Hire"},{"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} })

class Braemartimeassesment1View(APIView):
    serializer_class = Braemartimeassesment1ViewSerializer
    def get(self, request, *args, **kwargs):
        queryset = Braemartimeassesment1.objects.filter(year=kwargs['year'],week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "MonthTCperpcm_12":item['MonthTCperpcm_12'],"East":item['East'],"West":item['West'],"week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"MonthTCperpcm_12","value":"MonthTCperpcm_12"},{"label":"East","value":"East"},{"label":"West","value":"West"},
                 {"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} })


class Braemartimeassesment2View(APIView):
    serializer_class = Braemartimeassesment2ViewSerializer

    def get(self, request, *args, **kwargs):
        queryset = Braemartimeassesment2.objects.filter(
            year=kwargs['year'],
            week=kwargs['week']).values()
        data = []
        for item in queryset:
            dic = {
                "TC":item['TC'],"Pcm":item['pcm'],"week":item['week'],"year":item['year']
            }
            data.append(dic)
        columns=[{"label":"TC","value":"TC"},{"label":"Pcm","value":"pcm"},
                 {"label":"Week","value":"week"},{"label":"Year","value":"year"}]
        return Response({'results':{"column":columns, "rows":data} })
   
def send_email(request):
    email = EmailMessage(
        subject='This is the mail subject',
        body='This is the body of the message',
        from_email=settings.EMAIL_HOST_USER,
        to=['sumonkantidey23@gmail.com'],
        cc=['sumonkantidey23@gmail.com'],
        #reply_to=['cheng@blah.com'],  # when the reply or reply all button is clicked, this is the reply to address, normally you don't have to set this if you want the receivers to reply to the from_email address
    )
    #email.content_subtype = 'html' # if the email body contains html tags, set this. Otherwise, omit it
    try:
        email.send(fail_silently=False)
        return HttpResponseRedirect('/')
    except Exception:
        print(traceback.format_exc())  # you probably want to add a log here instead of console pri


@csrf_exempt
def login(request,**kwargs):
    username = request.POST['username']
    password = request.POST['password']
    print(username)
    print(password)
    user = authenticate(username=username, password=password)
    print(user)
    dic = {}
    group_dic = {
        'Broker' : False,
        'Analytics': False,
        'Broker_and_Analytics' : False
    }
    group_lst = ['Broker', 'Analytics', 'Broker_and_Analytics']
    if user:
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        get_queryset = User.objects.filter(username=username).values('id', 'email')
        dic['token'] = token
        dic['username'] = username
        for item in get_queryset:
            dic['id'] = item['id']
            dic['email'] = item['email']
            
        for group_name in group_lst:
            if user.groups.filter(name=group_name).exists():
                group_dic[group_name] = True
                break

        dic['permission'] = group_dic
	dic['isAdmin'] = user.is_superuser
        return JsonResponse(dic, status=status.HTTP_200_OK)
    return JsonResponse({'error': 'User not found'}, status=status.HTTP_403_FORBIDDEN)

