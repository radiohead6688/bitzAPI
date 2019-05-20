import json
import requests

import bitz
from email_method import send_email

bitz = bitz.Bitz()

"""
Testing the quotation methods
"""
# data = bitz.get_price_data_multiple_symbols('btc_usdt','ltc_usdt','eth_usdt')
# data = bitz.get_Kline_data('btc_usdt', '1min', size = 2, to = 1557673440000)
# data = bitz.get_fiat_money_exchange_rate('cny_usdt','usdt_cny')
# data = bitz.get__fiat_cryptocurrency_exchange_rate('usdt','btc')
# data = bitz.get_cryptocurrency_exchange_rate('usdt','btc')
# data = bitz.get_server_timestamp()
# data = bitz.get_cryptocurrency_trading_fee('btc_usdt','eth_btc')

# if data is not None:
    # print(json.dumps(data, indent=4))

    # with open('log.txt', 'w') as fout:
        # json.dump(data, fout)
# else:
    # print('[!] Request Failed!')

"""
Testing signature
"""
# data = bitz.get_cryptocurrency_deposit_address('usdt')
# data = bitz.get_cryptocurrency_withdrawal_addresses('btc')
data = bitz.add_limit_price_order('sell', 9000, 0.01, 'btc_usdt')

if data is not None:
    print(json.dumps(data, indent=4))

    with open('log.txt', 'w') as fout:
        json.dump(data, fout)
else:
    print('[!] Request Failed!')

"""
Testing the trade methods
"""


"""
Testing email sending
"""
# send email
# with open('email_credentials', 'r') as handle:
    # parsed = json.load(handle)

# with open('email_content', 'r') as fp:
    # message = fp.read()

# send_email(message,parsed['sender_address'],parsed['password'],'zzynuaa@sina.com','smtp.sina.com')

# if __name__=="__main__":
    # market = get_market('btc_usdt')
