from flask import Flask, render_template, request
import urllib2
import json


app = Flask(__name__)

@app.route("/")
def bitstamp():
    response = urllib2.urlopen('http://www.cryptocoincharts.info/v2/api/tradingPair/BTC_USD')
    http = response.read()
    j = json.loads(http)
    bitstamp = j['price']
    return render_template('home.html', bitstamp=bitstamp)

@app.route('/submit', methods=('GET', 'POST'))
def submit():
        if request.form['convert'] == 'convert':
            response = urllib2.urlopen('http://www.cryptocoincharts.info/v2/api/tradingPair/BTC_USD')
            http = response.read()
            j = json.loads(http)
            bitstamp = j['price']
            if request.form['select'] == 'btc2usd':
                btc = request.form['BTC']
                conversion = float(btc) * float(bitstamp)
                return render_template('conversion.html', bitstamp=bitstamp, btc=btc, conversion=conversion)
            else:
                btc = request.form['BTC']
                conversion = float(btc) * (1/float(bitstamp))
                return render_template('conversion1.html', bitstamp=bitstamp, btc=btc, conversion=conversion)

@app.route('/reset', methods=('GET', 'POST'))
def reset():
    response = urllib2.urlopen('http://www.cryptocoincharts.info/v2/api/tradingPair/BTC_USD')
    http = response.read()
    j = json.loads(http)
    bitstamp = j['price']
    return render_template('home.html', bitstamp=bitstamp)

if __name__ == "__main__":
    app.run()