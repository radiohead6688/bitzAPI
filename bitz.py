import json
import requests
import time
from enum import Enum

from signature import api_signature

class Bitz:

    def __init__(self):
        with open('user_info', 'r') as handle:
            parsed = json.load(handle)
        self.__apiKey = parsed['apiKey']
        self.__apiSecret = parsed['apiSecret']
        self.__tradePwd = parsed['tradePwd']


    # api_base_rul = 'https://apiv2.bitz.com/'
    api_base_rul = 'https://api.bitzapi.com/'

    headers = {'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/ \
            537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
    exceptions = {
        # '200': 'Success'
        '-102': 'Invalid parameter',
        '-103': 'Verification failed',
        '-104': 'Network Error-1',
        '-105': 'Invalid api signature',
        '-106': 'Network Error-2',
        '-109': 'Invalid scretKey',
        '-110': 'The number of access requests exceeded',
        '-111': 'Current IP is not in the range of trusted IP',
        '-112': 'Service is under maintenance',
        '-100015': 'Trade password error',
        '-100044': 'Fail to request data',
        '-100101': 'Invalid symbol',
        '-100201': 'Invalid symbol',
        '-100301': 'Invalid symbol',
        '-100401': 'Invalid symbol',
        '-100302': 'Type of K-line error',
        '-100303': 'Size of K-line error',
        '-200003': 'Please set trade password',
        '-200005': 'This account can not trade',
        '-200025': 'Temporary trading halt',
        '-200027': 'Price Error',
        '-200028': 'Amount must be greater than 0',
        '-200029': 'Number must be between %s and %d',
        '-200030': 'Over price range',
        '-200031': 'Insufficient assets',
        '-200032': 'System error. Please contact customer service',
        '-200033': 'Fail to trade',
        '-200034': 'The order does not exist',
        '-200035': 'Cancellation error, order filled',
        '-200037': 'Trade direction error',
        '-200038': 'Trading Market Error',
        '-200055': 'Order record does not exist',
        '-300069': 'api_key is illegal',
        '-300101': 'Transaction type error',
        '-300102': 'Price or number cannot be less than 0',
        '-300103': 'Trade password error',
        '-301001': 'Network Error-3',
    }


    """
    Quotation methods
    """
    def get_price_data(self, name):
        api_url = '{0}Market/ticker?symbol={1}'.format(self.api_base_rul, name)
        response = requests.get(api_url, headers = self.headers)
        #
        #   {
        #       "status": 200,
        #       "msg": "",
        #       "data": {
        #           "symbol": "777_btc",
        #           "quoteVolume": "2.5926",     //Total
        #           "volume": "2120645.6004",    //Volume
        #           "priceChange24h": "-4.83",   //24h Change
        #           "askPrice": "0.00000124",    //ask1 price
        #           "askQty": "509.1400",        //volume of ask1 price
        #           "bidPrice": "0.00000123",    //bid1 price
        #           "bidQty": "76.4401",         //volume of bid1 price
        #           "open": "0.00000118",        //open
        #           "high": "0.00000130",        //high
        #           "low": "0.00000109",         //low
        #           "now": "0.00000124",         //price
        #           "firstId": "105551102",      //first order
        #           "lastId": "105853063",       //last order
        #           "dealCount": "2650",         //order number
        #           "numberPrecision": "4",      //decimal point of number
        #           "pricePrecision": "8",       //decimal point of price
        #           "cny": "0.06912764",
        #           "usd": "0.01014551",
        #           "krw": "71696.37"
        #       },
        #       "time": 1532760578,
        #       "microtime": "0.11632100 1532760578",
        #       "source": "api"
        #   }
        #
        status = str(response.status_code)
        if status == '200':
            return json.loads(response.content.decode('utf-8'))
        elif status in self.exceptions:
            print('[!] {0} Error: {1}'.format(status, self.exceptions[status]))
            return None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(status, response.content))
            return None

    def get_depth_data(self, name):
        api_url = '{0}Market/depth?symbol={1}'.format(self.api_base_rul, name)
        response = requests.get(api_url, headers = self.headers)
        #
        #   {
        #       "status": 200,
        #       "msg": "",
        #       "data": {
        #           "asks": [   //sell
        #              [
        #                "57.70000000",         //price
        #                "1.6783",              //number
        #                "96.837910000000"      //Total price
        #              ],
        #           ],
        #           "bids": [  //buy
        #              [
        #                "0.00121238",
        #                "1398.9960",
        #                 "1.696114770480"
        #              ],
        #           ],
        #           "coinPair": "ltc_btc"
        #       },
        #       "time": 1532671014,
        #       "microtime": "0.49301600 1532671014",
        #       "source": "api"
        #   }
        #

        status = str(response.status_code)
        if status == '200':
            return json.loads(response.content.decode('utf-8'))
        elif status in self.exceptions:
            print('[!] {0} Error: {1}'.format(status, self.exceptions[status]))
            return None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(status, response.content))
            return None

    def get_order_data(self, name):
        api_url = '{0}Market/order?symbol={1}'.format(self.api_base_rul, name)
        response = requests.get(api_url, headers = self.headers)

        #
        #   {
        #       "status": 200,
        #       "msg": "",
        #       "data": [
        #           {
        #               "id": "105526523",
        #               "t": "12:58:48",    //time
        #               "T": 1535796654,
        #               "p": "0.01053000",  //price
        #               "n": "11.9096",     //number
        #               "s": "buy"          //type
        #           },
        #           {
        #               "id": "103157630",
        #               "t": "17:09:57",
        #               "T": 1535796654,
        #               "p": "0.01231200",
        #               "n": "2.6548",
        #               "s": "buy"
        #           }
        #       ],
        #       "time": 1532670836,
        #       "microtime": "0.91846700 1532670836",
        #       "source": "api"
        #   }
        #

        status = str(response.status_code)
        if status == '200':
            return json.loads(response.content.decode('utf-8'))
        elif status in self.exceptions:
            print('[!] {0} Error: {1}'.format(status, self.exceptions[status]))
            return None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(status, response.content))
            return None

    def get_price_data_all_symbols(self):
        api_url = '{0}Market/tickerall'.format(self.api_base_rul)
        response = requests.get(api_url, headers = self.headers)


        status = str(response.status_code)
        if status == '200':
            return json.loads(response.content.decode('utf-8'))
        elif status in self.exceptions:
            print('[!] {0} Error: {1}'.format(status, self.exceptions[status]))
            return None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(status, response.content))
            return None

    def get_price_data_multiple_symbols(self, *names):
        api_url = '{}Market/tickerall?symbols='.format(self.api_base_rul)
        for name in names:
            api_url += name + ','
        api_url = api_url[:-1]

        response = requests.get(api_url, headers = self.headers)

        #
        #   {
        #       "status": 200,
        #       "msg": "",
        #       "data": {
        #           "btc_usdt": {
        #               "symbol": "btc_usdt",
        #               "quoteVolume": "544214830.41",
        #               "volume": "75828.85",
        #               "priceChange": "4.17",
        #               "priceChange24h": "5.92",
        #               "askPrice": "7199.23",
        #               "askQty": "0.1854",
        #               "bidPrice": "7192.07",
        #               "bidQty": "0.3716",
        #               "open": "6792.93",
        #               "high": "7514.43",
        #               "low": "6664.44",
        #               "now": "7195.41",
        #               "firstId": 834805150,
        #               "lastId": 845307765,
        #               "dealCount": 202400,
        #               "numberPrecision": 4,
        #               "pricePrecision": 2,
        #               "cny": "49118.77",
        #               "usd": "7195.41",
        #               "krw": "8445316.90",
        #               "jpy": "790704.39"
        #           },
        #           "ltc_usdt": {
        #               "symbol": "ltc_usdt",
        #               "quoteVolume": "331563338.81",
        #               "volume": "3697516.40",
        #               "priceChange": "-2.08",
        #               "priceChange24h": "1.21",
        #               "askPrice": "87.9343",
        #               "askQty": "0.3710",
        #               "bidPrice": "87.3144",
        #               "bidQty": "0.5600",
        #               "open": "86.6097",
        #               "high": "95.3600",
        #               "low": "83.7633",
        #               "now": "87.6641",
        #               "firstId": 834805187,
        #               "lastId": 845307685,
        #               "dealCount": 1623957,
        #               "numberPrecision": 4,
        #               "pricePrecision": 4,
        #               "cny": "598.43",
        #               "usd": "87.66",
        #               "krw": "102892.13",
        #               "jpy": "9633.41"
        #           },
        #           "": null
        #       },
        #       "time": 1557668110,
        #       "microtime": "0.75807800 1557668110",
        #       "source": "api"
        #   }
        #

        status = str(response.status_code)
        if status == '200':
            return json.loads(response.content.decode('utf-8'))
        elif status in self.exceptions:
            print('[!] {0} Error: {1}'.format(status, self.exceptions[status]))
            return None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(status, response.content))
            return None

    def get_Kline_data(self, name, resolution, size = None, to = None):
        api_url = '{0}Market/kline?symbol={1}&resolution={2}'.format(self.api_base_rul, name, resolution)

        if size is not None:
            api_url += '&size={}'.format(size)

        if to is not None:
            api_url += '&to={}'.format(to)

        response = requests.get(api_url, headers = self.headers)

        #
        #   {
        #       "status": 200,
        #       "msg": "",
        #       "data": {
        #           "bars": [
        #               {
        #                   "time": "1557673440000",
        #                   "open": "6977.68",
        #                   "high": "6980.56",
        #                   "low": "6953.76",
        #                   "close": "6955.13",
        #                   "volume": "115.4158",
        #                   "datetime": "2019-05-12 23:04:00"
        #               },
        #               {
        #                   "time": "1557673380000",
        #                   "open": "6939.91",
        #                   "high": "6986.20",
        #                   "low": "6939.64",
        #                   "close": "6974.04",
        #                   "volume": "173.3622",
        #                   "datetime": "2019-05-12 23:03:00"
        #               }
        #           ],
        #           "resolution": "1min",
        #           "symbol": "btc_usdt",
        #           "from": "1557673440000",
        #           "to": "1557673380000",
        #           "size": 2
        #       },
        #       "time": 1557673754,
        #       "microtime": "0.43972700 1557673754",
        #       "source": "api"
        #   }
        #

        status = str(response.status_code)
        if status == '200':
            return json.loads(response.content.decode('utf-8'))
        elif status in self.exceptions:
            print('[!] {0} Error: {1}'.format(status, self.exceptions[status]))
            return None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(status, response.content))
            return None


    def get_fiat_money_exchange_rate(self, *names):
        api_url = '{0}Market/currencyRate?symbols='.format(self.api_base_rul)
        for name in names:
            api_url += name + ','
        api_url = api_url[:-1]

        response = requests.get(api_url, headers = self.headers)

        #
        #   {
        #       "status": 200,
        #       "msg": "",
        #       "data": {
        #           "cny_usdt": {
        #               "coin": "cny",
        #               "currencyCoin": "usdt",
        #               "rate": "0.145400",
        #               "rateTime": "2019-05-16 11:59:09",
        #               "ratenm": "cny/usdt",
        #               "flatform": "api.k780.com",
        #               "created": 1557979202,
        #               "timezone": "PRC"
        #           },
        #           "usdt_cny": {
        #               "coin": "usdt",
        #               "currencyCoin": "cny",
        #               "rate": "6.877600",
        #               "rateTime": "2019-05-16 11:59:09",
        #               "ratenm": "usdt/cny",
        #               "flatform": "api.k780.com",
        #               "created": 1557979202,
        #               "timezone": "PRC"
        #           },
        #           "": null
        #       },
        #       "time": 1557979508,
        #       "microtime": "0.02866600 1557979508",
        #       "source": "api"
        #   }
        #

        status = str(response.status_code)
        if status == '200':
            return json.loads(response.content.decode('utf-8'))
        elif status in self.exceptions:
            print('[!] {0} Error: {1}'.format(status, self.exceptions[status]))
            return None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(status, response.content))
            return None

    def get_fiat_cryptocurrency_exchange_rate(self, *names):
        api_url = '{0}Market/currencyCoinRate?coins='.format(self.api_base_rul)
        for name in names:
            api_url += name + ','
        api_url = api_url[:-1]

        response = requests.get(api_url, headers = self.headers)

        #
        #   {
        #       "status": 200,
        #       "msg": "",
        #       "data": {
        #           "usdt": {
        #               "btc": "0.0001247620",
        #               "eth": "0.0038309772",
        #               "bz": "9.6880449525",
        #               "usdt": "1",
        #               "cny": "6.8787145058",
        #               "jpy": "109.4690749863",
        #               "dkkt": "6.6616038477",
        #               "krw": "1190.4761904761",
        #               "eur": "0.8917997231",
        #               "sgd": "1.3688991586",
        #               "usd": "1",
        #               "dkk": "6.6616038477"
        #           },
        #           "btc": {
        #               "btc": 1,
        #               "usdt": "8015.2600000000",
        #               "eth": "30.7113328196",
        #               "bz": "79681.2749003984",
        #               "cny": "55134.6852300242",
        #               "jpy": "877423.0979748221",
        #               "dkkt": "53394.4868566556",
        #               "krw": "9541976.1904761904",
        #               "eur": "7148.0066492587",
        #               "sgd": "10972.0826705579",
        #               "usd": "8015.2600000000",
        #               "dkk": "53394.4868566556"
        #           },
        #           "": null
        #       },
        #       "time": 1557986338,
        #       "microtime": "0.14414300 1557986338",
        #       "source": "api"
        #   }
        #

        status = str(response.status_code)
        if status == '200':
            return json.loads(response.content.decode('utf-8'))
        elif status in self.exceptions:
            print('[!] {0} Error: {1}'.format(status, self.exceptions[status]))
            return None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(status, response.content))
            return None

    def get_cryptocurrency_exchange_rate(self, *names):
        api_url = '{0}Market/coinRate?coins='.format(self.api_base_rul)
        for name in names:
            api_url += name + ','
        api_url = api_url[:-1]


        response = requests.get(api_url, headers = self.headers)

        #
        #   {
        #       "status": 200,
        #       "msg": "",
        #       "data": {
        #           "usdt": {
        #               "btc": "0.0001247620",
        #               "eth": "0.0038309772",
        #               "bz": "9.6880449525",
        #               "usdt": "1",
        #               "cny": "6.8787145058",
        #               "jpy": "109.4690749863",
        #               "dkkt": "6.6616038477",
        #               "krw": "1190.4761904761",
        #               "eur": "0.8917997231",
        #               "sgd": "1.3688991586",
        #               "usd": "1",
        #               "dkk": "6.6616038477"
        #           },
        #           "btc": {
        #               "btc": 1,
        #               "usdt": "8015.2600000000",
        #               "eth": "30.7113328196",
        #               "bz": "79681.2749003984",
        #               "cny": "55134.6852300242",
        #               "jpy": "877423.0979748221",
        #               "dkkt": "53394.4868566556",
        #               "krw": "9541976.1904761904",
        #               "eur": "7148.0066492587",
        #               "sgd": "10972.0826705579",
        #               "usd": "8015.2600000000",
        #               "dkk": "53394.4868566556"
        #           },
        #           "": null
        #       },
        #       "time": 1557986338,
        #       "microtime": "0.14414300 1557986338",
        #       "source": "api"
        #   }
        #

        status = str(response.status_code)
        if status == '200':
            return json.loads(response.content.decode('utf-8'))
        elif status in self.exceptions:
            print('[!] {0} Error: {1}'.format(status, self.exceptions[status]))
            return None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(status, response.content))
            return None

    def get_server_timestamp(self):
        api_url = '{0}Market/getServerTime'.format(self.api_base_rul)
        response = requests.get(api_url, headers = self.headers)

        #
        #   {
        #       "status": 200,
        #       "msg": "",
        #       "data": [],
        #       "time": 1557987712,
        #       "microtime": "0.38221500 1557987712",
        #       "source": "api"
        #   }
        #

        status = str(response.status_code)
        if status == '200':
            return json.loads(response.content.decode('utf-8'))
        elif status in self.exceptions:
            print('[!] {0} Error: {1}'.format(status, self.exceptions[status]))
            return None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(status, response.content))
            return None

    def get_cryptocurrency_trading_fee(self, *names):
        api_url = '{0}Market/symbolListRate?symbols='.format(self.api_base_rul)
        for name in names:
            api_url += name + ','
        api_url = api_url[:-1]

        response = requests.get(api_url, headers = self.headers)

        #
        #   {
        #       "status": 200,
        #       "msg": "",
        #       "data": [],
        #       "time": 1557987712,
        #       "microtime": "0.38221500 1557987712",
        #       "source": "api"
        #   }
        #

        status = str(response.status_code)
        if status == '200':
            return json.loads(response.content.decode('utf-8'))
        elif status in self.exceptions:
            print('[!] {0} Error: {1}'.format(status, self.exceptions[status]))
            return None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(status, response.content))
            return None


    """
    Trading methods
    """
    def add_limit_price_order(self,side,price,number,symbol):
        api_url = '{0}Trade/addEntrustSheet'.format(self.api_base_rul)

        orderType = '1' if (side == 'buy') else '2'
        sig_params = {'apiKey':self.__apiKey, 'apiSecret':self.__apiSecret, 'type':orderType,
                'price':price,'number':number, 'symbol':symbol, 'tradePwd':self.__tradePwd}
        data = api_signature(sig_params)

        response = requests.post(api_url, data)
        #
        #   {
        #       "status": 200,
        #       "msg": "",
        #       "data": [],
        #       "time": 1557987712,
        #       "microtime": "0.38221500 1557987712",
        #       "source": "api"
        #   }
        #

        status = str(response.status_code)
        if status == '200':
            return json.loads(response.content.decode('utf-8'))
        elif status in self.exceptions:
            print('[!] {0} Error: {1}'.format(status, self.exceptions[status]))
            return None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(status, response.content))
            return None

    def get_cryptocurrency_deposit_address(self,name):
        api_url = '{0}Trade/getCoinAddress'.format(self.api_base_rul)

        sig_params = {'apiKey':self.__apiKey, 'apiSecret':self.__apiSecret, 'coin':name}
        data = api_signature(sig_params)

        response = requests.post(api_url, data)
        #
        #   {
        #       "status": 200,
        #       "msg": "",
        #       "data": [],
        #       "time": 1557987712,
        #       "microtime": "0.38221500 1557987712",
        #       "source": "api"
        #   }
        #

        status = str(response.status_code)
        if status == '200':
            return json.loads(response.content.decode('utf-8'))
        elif status in self.exceptions:
            print('[!] {0} Error: {1}'.format(status, self.exceptions[status]))
            return None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(status, response.content))
            return None

    def get_cryptocurrency_withdrawal_addresses(self,name):
        api_url = '{0}Trade/getCoinAddressList'.format(self.api_base_rul)

        sig_params = {'apiKey':self.__apiKey, 'apiSecret':self.__apiSecret, 'coin':name}
        data = api_signature(sig_params)

        response = requests.post(api_url, data)
        #
        #   {
        #       "status": 200,
        #       "msg": "",
        #       "data": [],
        #       "time": 1557987712,
        #       "microtime": "0.38221500 1557987712",
        #       "source": "api"
        #   }
        #

        status = str(response.status_code)
        if status == '200':
            return json.loads(response.content.decode('utf-8'))
        elif status in self.exceptions:
            print('[!] {0} Error: {1}'.format(status, self.exceptions[status]))
            return None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(status, response.content))
            return None

    def get_user_assets(self):
        api_url = '{0}Assets/getUserAssets'.format(self.api_base_rul)

        sig_params = {'apiKey':self.__apiKey, 'apiSecret':self.__apiSecret}
        data = api_signature(sig_params)

        response = requests.post(api_url, data)

        #
        #   {
        #       "status": 200,
        #       "msg": "",
        #       "data": [],
        #       "time": 1557987712,
        #       "microtime": "0.38221500 1557987712",
        #       "source": "api"
        #   }
        #

        status = str(response.status_code)
        if status == '200':
            return json.loads(response.content.decode('utf-8'))
        elif status in self.exceptions:
            print('[!] {0} Error: {1}'.format(status, self.exceptions[status]))
            return None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(status, response.content))
            return None
