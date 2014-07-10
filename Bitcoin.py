import urllib2
import json
import wxPython

# HTTP Request and JSON encoding

response = urllib2.urlopen('http://api.bitcoincharts.com/v1/markets.json')
http = response.read()
j = json.loads(http)

# Parsing data

# bitstamp
for x in j:
    symbol = x['symbol']
    if symbol == 'bitstampUSD':
        bitstamp = x['ask']
# btc-e
for e in j:
    symbol = e['symbol']
    if symbol == 'btceUSD':
        btce = e['ask']


print bitstamp, btce