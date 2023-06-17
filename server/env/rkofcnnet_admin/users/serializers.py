from rest_framework import serializers
from users.models import Users

class UsersSerializers(serializers.ModelSerializer) :
    class Meta:
        model = Users
        #read_only_fields = ['id']
        fields = "__all__"