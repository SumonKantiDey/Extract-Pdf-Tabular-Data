from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension


class Clarksontimefixture(models.Model):
    assesed12month = models.TextField()
    thisweekMonthly = models.TextField()
    thisweekDaily = models.TextField()
    lastweekMonthly = models.TextField()
    lastweekDaily = models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'Clarksontimefixture'
class errorlog(models.Model):
    type=models.TextField()
    name = models.TextField()
    table=models.TextField()
    class Meta:
        db_table = 'errorlog'
class Clarksonspotass1(models.Model):
    assesed=models.TextField()
    thisweekMonthly = models.TextField()
    thisweekDaily = models.TextField()
    lastweekMonthly = models.TextField()
    lastweekDaily = models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)

    class Meta:
        db_table = 'Clarksonspotass1'
class Clarksonspotass2(models.Model):
    Weeklyfrieghtass=models.TextField()
    thisweek=models.TextField()
    lastweek=models.TextField()
    week=models.IntegerField()
    year=models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'Clarksonspotass2'
class Clarksontimeass(models.Model):
    Vessel = models.TextField()
    CBM = models.TextField()
    Cargo = models.TextField()
    Area = models.TextField()
    Period = models.TextField()
    Rate=models.TextField()
    Charterer=models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'Clarksontimeass'
# Create your models here.
class Clarksonspotfixture(models.Model):
    Vessel = models.TextField()
    CBM = models.TextField()
    Cargo = models.TextField()
    Voyage = models.TextField()
    Laycan = models.TextField()
    Rate=models.TextField()
    Charterer=models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'Clarksonspotfixture'

#-----------------Gibson------------------
class Gibsonspotass(models.Model):
    Mts = models.TextField()
    Country = models.TextField()
    Usperpmt = models.TextField()
    previousweek = models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'gibsonspotass'
class Gibsontimeass(models.Model):
    Cbm = models.TextField()
    type = models.TextField()
    USperpcm = models.TextField()
    previousweekpcm = models.TextField()
    USperday = models.TextField()
    previousweekday = models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'gibsontimeass'
class Gibsonspotfixture(models.Model):
    Vessel = models.TextField()
    CBM = models.TextField()
    Mts = models.TextField()
    Cargo = models.TextField()
    Load=models.TextField()
    Disch=models.TextField()
    Laycan = models.TextField()
    Rate=models.TextField()
    Charterer=models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'gibsonspotfixture'
class Gibsontimefixture(models.Model):
    Vessel = models.TextField()
    CBM = models.TextField()
    Period = models.TextField()
    Delivery=models.TextField()
    Redelivery=models.TextField()
    Laycan = models.TextField()
    Hire=models.TextField()
    Charterer=models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'gibsontimefixture'
#-----------------------Steem1960---------------------------------------#
class Steemspotfixture(models.Model):
    Vessel = models.TextField()
    Built = models.TextField()
    CBM = models.TextField()
    Charterer = models.TextField()
    Qty = models.TextField()
    Cargo = models.TextField()
    LoadPort = models.TextField()
    DischPort = models.TextField()
    Laycan = models.TextField()
    Freight = models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'steemspotfixture'
class Steemtimefixture(models.Model):
    Vessel = models.TextField()
    Built = models.TextField()
    CBM = models.TextField()
    Charterer = models.TextField()
    Period = models.TextField()
    Cargo = models.TextField()
    DeliveryRedel = models.TextField()
    Laycan = models.TextField()
    Hire = models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'steemtimefixture'

class Steemspotass(models.Model):
    size_mts = models.TextField()
    cargo = models.TextField()
    trade = models.TextField()
    USDperMT = models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'steemspotass'
class Steemtimeass(models.Model):
    VesselSize = models.TextField()
    HireperUSDpcm = models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'steemtimeass'
#--------------------Fearngas------------------#
class Fearngasspotfixture(models.Model):
    Vessel = models.TextField()
    Cbm = models.TextField()
    Type = models.TextField()
    LoadDisch = models.TextField()
    Laycan = models.TextField()
    Rate = models.TextField()
    Charterer = models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'fearngasspotfixture'

class Fearngastimefixture(models.Model):
    Vessel = models.TextField()
    Cbm = models.TextField()
    Period = models.TextField()
    LoadDisch = models.TextField()
    Laycan = models.TextField()
    Rate = models.TextField()
    Charterer = models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'fearngastimefixture'

class Fearngasspotassement(models.Model):
    spotmarket = models.TextField()
    Thisweek = models.TextField()
    change = models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'fearngasspotassement'
#--------------------Braemar------------------#
class Braemarspotfixture(models.Model):
    Charterer = models.TextField()
    Vessel = models.TextField()
    Cbm = models.TextField()
    YOB = models.TextField()
    Cargo = models.TextField()
    Load = models.TextField()
    Discharge = models.TextField()
    Laycan = models.TextField()
    Rate = models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'braemarspotfixture'
class Braemarspotassesment(models.Model):
    Region = models.TextField()
    price = models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'braemarspotassesment'
class Braemartimefixture(models.Model):
    Charterer = models.TextField()
    Vessel = models.TextField()
    Cbm = models.TextField()
    YOB = models.TextField()
    Period = models.TextField()
    Del = models.TextField()
    Redel = models.TextField()
    Laycan = models.TextField()
    Hire = models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'braemartimefixture'
class Braemartimeassesment1(models.Model):
    MonthTCperpcm_12 = models.TextField()
    East = models.TextField()
    West = models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'braemartimeassesment1'

class Braemartimeassesment2(models.Model):
    TC = models.TextField()
    pcm = models.TextField()
    week = models.IntegerField()
    year = models.IntegerField()
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    class Meta:
        db_table = 'braemartimeassesment2'
        
class UserEmail(models.Model):
    title = models.CharField(max_length = 256)
    email = models.CharField(max_length = 256)
    def __str__(self):
        return self.email
   
class Pdf(models.Model):
    user = models.ForeignKey(UserEmail, on_delete = models.CASCADE,verbose_name="User Name")
    pdf = models.FileField(upload_to='pdf/', blank=True,validators=[validate_file_extension])
    date = models.DateTimeField()
    class Meta:
        db_table = "pdf_file"


