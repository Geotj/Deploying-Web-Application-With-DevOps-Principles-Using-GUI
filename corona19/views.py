from django.shortcuts import render
from rest_framework.decorators import action, api_view
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

@api_view(['GET'])
def webscrapper(request):
    try:
        import requests
        import pandas as pd
        import bs4
        url = "https://www.worldometers.info/coronavirus/"
        result = requests.get(url)

        soup = bs4.BeautifulSoup(result.text, 'lxml')
        cases = soup.find_all('div', class_='maincounter-number')
        data = []

        for i in cases:
            span = i.find('span')
            data.append(span.string)


        df = pd.DataFrame({'CoronaData': data})
        df.index = ["TotalCases", "TotalDeaths", "TotalRecovered"]

        # To delete all existing rows from the table
        corona19_model.objects.all().delete()
        tc = df.iloc[0]
        td = df.iloc[1]
        tr = df.iloc[2]
        # to create a new object
        corona19_model.objects.create(totalcases=tc, totaldeaths=td, totalrecovered=tr)
        response = corona19_model.objects.all().values()
        return Response(response)
    except Exception as err:
        raise Exception(str(err))
