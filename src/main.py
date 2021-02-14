import requests
import json
from src.config import url
from src.config import rules
from src.mail import send_smtp_mail
from src.notification import check_notify_rules, send_sms


def get_rates() -> dict or None:
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def archive(filename: str, rates: dict) -> None:
    with open(file=f'archive/{filename}.json', mode='w') as f:
        f.write(json.dumps(rates))


def get_preferred_rates(rates: dict) -> dict or None:
    if rules['email']['preferred']:
        preferred_rates = dict()
        for rate in rules['email']['preferred']:
            preferred_rates[rate] = rates[rate]
        rates = preferred_rates
    return rates


def send_mail(timestamp: str, rates: dict) -> None:
    subject = f'{timestamp}'
    rates = get_preferred_rates(rates)

    body = json.dumps(rates)

    send_smtp_mail(
        subject,
        body
    )


def send_notification(msg: str) -> None:
    send_sms(msg)


if __name__ == '__main__':
    get_response = get_rates()

    if rules['archive']['enable']:
        archive(
            filename=get_response['timestamp'],
            rates=get_response['rates']
        )

    if rules['email']['enable']:
        send_mail(
            timestamp=get_response['timestamp'],
            rates=get_response['rates']
        )

    if rules['notification']['enable']:
        notification_msg = check_notify_rules(
            rates=get_response['rates']
        )

        if notification_msg:
            send_notification(
                msg=notification_msg
            )
