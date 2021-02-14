BASE_URL = 'http://data.fixer.io/api/latest?access_key='
API_KEY = 'YOUR API KEY'
url = BASE_URL + API_KEY

KAVENEGAR_API_KEY = 'YOUR API KEY'


rules = {
    'archive': {
        'enable': True
    },
    'email': {
        'enable': True,
        'preferred': ['BTC', 'IRR', 'USD']
    },
    'notification': {
        'enable': True,
        'preferred': {
            'USD': {'min': 1.10, 'max': 1.30},
            'IRR': {'min': 41100, 'max': 61100}
        }
    }
}
