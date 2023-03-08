from rest_framework import serializers
from api.models import company

# create serializers here
class companyserial(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=company
        fields="__all__"
