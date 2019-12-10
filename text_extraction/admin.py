from django.contrib import admin
from .models import Pdf,UserEmail,Clarksontimefixture,errorlog,Clarksonspotass1,Clarksonspotass2,Clarksontimeass,Clarksonspotfixture
from .models import Gibsonspotass,Gibsontimeass,Gibsonspotfixture,Gibsontimefixture 
from .models import Steemspotfixture,Steemtimefixture,Steemspotass,Steemtimeass
from .models import Fearngasspotfixture,Fearngastimefixture,Fearngasspotassement
from .models import Braemarspotfixture,Braemarspotassesment,Braemartimefixture,Braemartimeassesment1,Braemartimeassesment2
# Register your models here.
admin.site.register(Pdf)
class UserEmailAdmin(admin.ModelAdmin):
    list_display = ('title', 'email')
admin.site.register(UserEmail,UserEmailAdmin),
admin.site.register(Clarksontimefixture),
admin.site.register(errorlog),
admin.site.register(Clarksonspotass1),
admin.site.register(Clarksonspotass2),
admin.site.register(Clarksontimeass),
admin.site.register(Clarksonspotfixture),
admin.site.register(Gibsonspotass),
admin.site.register(Gibsontimeass),
admin.site.register(Gibsonspotfixture),
admin.site.register(Gibsontimefixture),
admin.site.register(Steemspotfixture),
admin.site.register(Steemtimefixture),
admin.site.register(Steemspotass),
admin.site.register(Steemtimeass),
admin.site.register(Fearngasspotfixture),
admin.site.register(Fearngastimefixture),
admin.site.register(Fearngasspotassement),
admin.site.register(Braemarspotfixture),
admin.site.register(Braemarspotassesment),
admin.site.register(Braemartimefixture),
admin.site.register(Braemartimeassesment1),
admin.site.register(Braemartimeassesment2)

