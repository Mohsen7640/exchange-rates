from src.config import rules
from kavenegar import *
from src.config import KAVENEGAR_API_KEY
from src.local_config import receiver


def check_notify_rules(rates: dict) -> str:
    preferred_rates = rules['notification']['preferred']
    msg = ''

    for rate in preferred_rates.keys():
        if rates[rate] <= preferred_rates[rate]['min']:
            msg += f'{rate} reached min : {rates[rate]}'
        if rates[rate] >= preferred_rates[rate]['max']:
            msg += f'{rate} reached max : {rates[rate]}'

    return msg


def send_sms(msg: str) -> None:
    try:
        api = KavenegarAPI(KAVENEGAR_API_KEY)
        params = {
            'sender': '10004346',
            'receptor': receiver['phone'],
            'message': msg
        }
        response = api.sms_send(params)
        print(str(response))

    except APIException as e:
        print(str(e))
    except HTTPException as e:
        print(str(e))
