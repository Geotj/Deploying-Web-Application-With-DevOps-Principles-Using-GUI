from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import viewsets

from corona19.models import corona19_model
from corona19.serializers import Corona19Serializer


class Corona19ViewSet(viewsets.ModelViewSet):
    serializer_class = Corona19Serializer
    queryset = corona19_model.objects.all()

    @action(detail=False)
    def delete_all_data(self, request):
        corona19_model.objects.all().delete()
        return Response("All Data Deleted")


def coronadata_table_template(request):
    queryset = corona19_model.objects.all()
    return render(request, 'coronaDataTemplate.html', {'results': queryset})