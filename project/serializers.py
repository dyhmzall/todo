from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Project, Todo
from users.serializers import UserModelSerializer


class ProjectModelSerializer(HyperlinkedModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectModelSerializer2(ModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(HyperlinkedModelSerializer):
    user = UserModelSerializer()
    project = ProjectModelSerializer()

    class Meta:
        model = Todo
        fields = '__all__'
