from typing import Match
from django.shortcuts import render
import requests
from requests.exceptions import ConnectionError

def index(request):
   
    CovidData = []   
    try:
        reqdata = requests.get('https://static.easysunday.com/covid-19/getTodayCases.json').json()
    except ConnectionError as e:    
        print( type(e) )
        reqdata = {"Error": "Found something when wrong"}
    
    InteresetData = [
        'country',
        'cases',
        'todayCases',
        'deaths',
        'todayDeaths',
        'recovered',
        'todayRecovered',
        'active',
        'critical',
        'tests',
        'population',
        'UpdateDate',
        'Error'
    ]

    InteresetDataStr = [
    'Country',
    'Cases',
    'Today Cases',
    'Deaths',
    'Today Deaths',
    'Recovered',
    'Today Recovered',
    'Active',
    'Critical',
    'Tests',
    'Population',    
    'Updated Date',
    'Error'
    ]

    # print(InteresetData.index('Confirmed'))
    for key, value in reqdata.items():        
        if key in InteresetData:            
            CovidData.append(
            {   'Key': InteresetDataStr[InteresetData.index(key)],
                'Value': value
            })
    
    return render(request, 'index.html', {
        'CovidData': CovidData})
