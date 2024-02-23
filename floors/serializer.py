from rest_framework import serializers
from floors.models import person_details,Company_details,floors,Register_user



class Registerserializer(serializers.ModelSerializer):
    class Meta:
        models=Register_user
        fields = "__all__"
        # include=['']
        # exclude=['']

        def validate(self, attrs):
            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError({"password":"password miss match "})

            return attrs
        def create(self, validated_data):

           pass









