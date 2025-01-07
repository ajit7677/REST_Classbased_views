from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    roll_no = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    mobile = serializers.IntegerField()
    country = serializers.CharField(max_length=15)
    email = serializers.EmailField()

    # When ever we goes to inset the data in DB or create new records then this method is play important role.
    # For GET method this create method is not required.
    def create(self, validate_data):
        return Student.objects.create(**validate_data)
    def update(self, instance, validated_data):
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)
        instance.name = validated_data.get('name', instance.name)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.country = validated_data.get('country', instance.country)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance