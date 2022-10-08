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

def webscrapper():
    import requests
    url = "https://www.worldometers.info/coronavirus/"
    result = requests.get(url)
    import bs4
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    cases = soup.find_all('div', class_='maincounter-number')
    data = []

    for i in cases:
        span = i.find('span')
        data.append(span.string)

    import pandas as pd
    df = pd.DataFrame({'CoronaData': data})
    df.index = ["TotalCases", "TotalDeaths", "TotalRecovered"]

    requests.get('http://localhost:8000/corona_data/delete_all_data/')

    import webbrowser
    url = 'http://localhost:8000/corona_data/'
    tc = df.iloc[0]
    td = df.iloc[1]
    tr = df.iloc[2]

    df.iloc[0]
    df.iloc[1]
    df.iloc[2]

    myobj = {
        "totalcases": tc,
        "totaldeaths": td,
        "totalrecovered": tr
    }

    x = requests.post(url, data=myobj)

    webbrowser.open(url)

