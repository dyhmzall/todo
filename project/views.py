from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from .models import Project, Todo
from .serializers import ProjectModelSerializer, ProjectModelSerializer2, TodoModelSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, renderer_classes, action


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer


class ProjectAPIView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectModelSerializer2(projects, many=True)
        return Response(serializer.data)


# для примера
# @api_view(['GET'])
# @renderer_classes([JSONRenderer])
# def project_view(request):
#     projects = Project.objects.all()
#     serializer = ProjectModelSerializer2(projects, many=True)
#     return Response(serializer.data)


class ProjectCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer2


class ProjectListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer2


class ProjectRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer2


class ProjectDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer2


class ProjectUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer2


# ViewSet

class ProjectViewSet(ViewSet):
    renderer_classes = [JSONRenderer]

    @action(detail=True, methods=['get'])
    def project_text_only(self, request, pk=None):
        project = get_object_or_404(Project, pk=pk)
        return Response({'project.text': project.text})

    def list(self, request):
        projects = Project.objects.all()
        serializer = ProjectModelSerializer2(projects, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectModelSerializer2(project)
        return Response(serializer.data)

# custom view set

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

class ProjectCustomViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer2
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


# filtering

class ProjectQuerysetFilterViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()

    def get_queryset(self):
        return Project.objects.filter(name__contains='python')


class ProjectKwargsFilterView(ListAPIView):
    serializer_class = ProjectModelSerializer2

    def get_queryset(self):
        name = self.kwargs['name']
        return Project.objects.filter(name__contains=name)


