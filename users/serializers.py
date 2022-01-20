from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Users


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'firstname', 'lastname', 'email']
