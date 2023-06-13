from rest_framework import serializers
import core.models as mdls
from rest_framework.serializers import ValidationError


class Login(serializers.RelatedField):
    def to_representation(self, value):
        return f"{value.login}"
    def to_internal_value(self, data):
        # index=data.get("index")
        
        try:
            login=mdls.Unique_Login.objects.get(login=data)
            return login
        except:
            raise ValidationError("this login does not exist")
        
class Unique_Login_Serializer(serializers.ModelSerializer):
    class Meta:
        model=mdls.Unique_Login
        fields=["id","login"]

class IQ_Serializer(serializers.ModelSerializer):
    login_f=Login(many=False, queryset=mdls.Unique_Login.objects.all())
    class Meta:
        model=mdls.IQ_Test
        fields=["id","score","login_f","date_passed"]

class EQ_Serializer(serializers.ModelSerializer):
    login_f=Login(many=False, queryset=mdls.Unique_Login.objects.all())
    class Meta:
        model=mdls.EQ_Test
        fields=["id","result","login_f","date_passed"]