import json


mockData = ''
with open('mockData.json') as f:
    data = json.load(f)
    mockData = data
    print(mockData)


class WeatherFetcher:
    pass