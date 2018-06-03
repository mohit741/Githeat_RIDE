import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import pandas as pd
import json


def index(request):
    err = {}
    data = {}
    if request.method == 'POST':
        train_no = str(request.POST['trainno']).strip()
        url1 = 'https://www.cleartrip.com/trains/' + train_no
        url2 = 'https://erail.in/train-fare/' + train_no + '?query=' + train_no
        try:
            r1 = requests.get(url1)
            r2 = requests.get(url2)
            soup = BeautifulSoup(r1.text, 'html.parser')
            train = soup.find('h1').text.split('\n')[1].strip()
            train_meta = soup.find('h1').text.split('\n')[4].strip()
            train_name = train + ' ' + train_meta
            table = soup.find('table', class_='results')
            df = pd.read_html(str(table))
            res = df[0].to_json()
            data['train_name'] = train_name
            data['stations'] = json.loads(res)
            li = soup.find('ul', class_='list-unstyled info-summary').find_all('li')
            details = {}
            for i in range(0, 2):
                key = li[i].text.split(':')[0]
                value = li[i].text.split(':')[1]
                details[key.strip()] = value.strip()
            span = li[2].find_all('span')
            for i in range(0, len(span)):
                key = span[i].text.split(':')[0]
                value = span[i].text.split(':')[1]
                details[key.strip()] = value.strip()
            data['details'] = details
            soup = BeautifulSoup(r2.text, 'html.parser')
            table = soup.find('div', class_='panel panel-warning').find('table')
            df = pd.read_html(str(table))
            res = df[0].to_json()
            data['fare'] = json.loads(res)
            return HttpResponse(json.dumps(data), content_type='application/json')

        except Exception as e:
            return render(request, 'index.html', {'err': e.args[0]})
    else:
        return render(request, 'index.html', err)


def find_trains(request):
    pass
