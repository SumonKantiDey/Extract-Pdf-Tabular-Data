from rest_framework import serializers
from .models import Clarksontimefixture,errorlog,Clarksonspotass1,Clarksonspotass2,Clarksontimeass,Clarksonspotfixture,UserEmail,Pdf
from .models import Gibsonspotfixture,Gibsontimefixture,Gibsonspotass,Gibsontimeass
from .models import Steemspotfixture,Steemtimefixture,Steemspotass,Steemtimeass
from .models import Fearngasspotfixture,Fearngastimefixture,Fearngasspotassement
from .models import Braemarspotfixture,Braemarspotassesment,Braemartimefixture,Braemartimeassesment1,Braemartimeassesment2
class ClarksonspotfixtureViewSerializer(serializers.Serializer):
    class Meta:
        model = Clarksonspotfixture
        fields = ('__all__')
class ClarksontimefixtureViewSerializer(serializers.Serializer):
    class Meta:
        model: Clarksontimefixture
        fields = ('__all__')
class Clarksonspotassesment1ViewSerializer(serializers.Serializer):
    class Meta:
        model: Clarksonspotass1
        fields = ('__all__')

class Clarksonspotassesment2ViewSerializer(serializers.Serializer):
    class Meta:
        model: Clarksonspotass2
        fields = ('__all__')

class ClarksontimeassesmentViewSerializer(serializers.Serializer):
    class Meta:
        model:Clarksontimeass
        fields = ('__all__')
class GibsonspotfixtureViewSerializer(serializers.Serializer):
    class Meta:
        model: Gibsonspotfixture
        fields = ('__all__')
class GibsontimefixtureViewSerializer(serializers.Serializer):
    class Meta:
        model: Gibsontimefixture
        fields = ('__all__')
class GibsonspotassViewSerializer(serializers.Serializer):
    class Meta:
        model: Gibsonspotass
        fiels = ('__all__')
class GibsontimeassViewSerializer(serializers.Serializer):
    class Meta:
        model: Gibsontimeass
        fields = ('__all__')
class SteemspotfixtureViewSerializer(serializers.Serializer):
    class Meta:
        model: Steemspotfixture
        fields = ('__all__')
class SteemtimefixtureViewSerializer(serializers.Serializer):
    class Meta:
        model: Steemtimefixture
        fields = ('__all__')
class SteemspotassViewSerializer(serializers.Serializer):
    class Meta:
        model: Steemspotass
        fields = ('__all__')
class SteemtimeassViewSerializer(serializers.Serializer):
    class Meta:
        model: Steemtimeass
        fields = ('__all__')
class FearngasspotfixtureViewSerializer(serializers.Serializer):
    class Meta:
        model: Fearngasspotfixture
        fields = ('__all__')
class FearngastimefixtureViewSerializer(serializers.Serializer):
    class Meta:
        model: Fearngastimefixture
        fields = ('__all__')
class FearngasspotassementViewSerializer(serializers.Serializer):
    class Meta:
        model: Fearngasspotassement
        fields = ('__all__')
class BraemarspotfixtureViewSerializer(serializers.Serializer):
    class Meta:
        model: Braemarspotfixture
        fields = ('__all__')
class BraemarspotassesmentViewSerializer(serializers.Serializer):
    class Meta:
        model = Braemarspotassesment
        fields = ('__all__')
class BraemartimefixtureViewSerializer(serializers.Serializer):
    class Meta:
        model: Braemartimefixture
        fields = ('__all__')

class Braemartimeassesment1ViewSerializer(serializers.Serializer):
    class Meta:
        model: Braemartimeassesment1
        fields = ('__all__')
class Braemartimeassesment2ViewSerializer(serializers.Serializer):
    class Meta:
        model: Braemartimeassesment2
        fields = ('__all__')
        