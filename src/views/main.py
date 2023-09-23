from __future__ import print_function

import sys
import time
import schedule
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controlers.notifications import Notification  # noqa
from controlers.api import start_api  # noqa
from models.messages import Messages  # noqa


def main(sender=None, subject=None):
    # Call the Gmail API
    service = start_api('credentials.json')

    messages = Messages(service)
    notifications = Notification()

    messages_header = messages.filter(sender, subject)
    messages_header = messages.get_messages(messages_header)
    notifications.show_notification(messages_header)


if __name__ == '__main__':
    allow_filter = str(input('\nDeseja aplicar filtros? S/N: ')).upper()

    sender = None
    subject = None

    if allow_filter == 'S':
        print('\nEscolha o tipo de filtro:')
        print('1 - Filtrar por remetente')
        print('2 - Filtrar por assunto')
        print('3 - Filtrar por remetente e assunto')

        filter_type = int(input('\nNúmero de filtro: '))

        if filter_type == 1:
            sender = str(input('Remetente: '))
        elif filter_type == 2:
            subject = str(input('Assunto: '))
        else:
            sender = str(input('Remetente: '))
            subject = str(input('Assunto: '))

    main(sender, subject)
    schedule.every(30).seconds.do(main, sender, subject)

    while True:
        schedule.run_pending()
        time.sleep(1)
