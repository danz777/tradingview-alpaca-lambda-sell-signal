import requests, json
from chalice import Chalice

app = Chalice(app_name='sell')

API_KEY = 'add api key'
SECRET_KEY = 'add secret key'
BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

@app.route('/sell', methods=['POST'])
def create_order(symbol, qty, side, type, time_in_force):
    request = app.current_request
    webhook_message = request.json_body

    data = {
        "symbol": webhook_message['ticker'],
        "qty": '10',
        "side": 'sell',
        "type": 'market',
        "time_in_force": 'gtc'
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    response = json.loads(r.content)
        
    return {
        'webhook_message': webhook_message,
        'id': response['id'],
        'client_order_id': response['client_order_id']
    }
