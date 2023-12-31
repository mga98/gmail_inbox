from __future__ import print_function

import sys
import time
import schedule
from typing import List
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controlers.notifications import Notification  # noqa
from controlers.deep_filter import Filter  # noqa
from controlers.api import start_api  # noqa
from models.messages import Messages  # noqa


def main(filters: List | None = None) -> None:
    # Call the Gmail API
    service = start_api('credentials.json')

    messages = Messages(service)
    notifications = Notification()

    messages_header = messages.filter()
    messages_header = messages.get_messages(messages_header)

    if filters:
        filtered_emails = Filter.deep_filter(messages_header, filters)
        notifications.show_notification(filtered_emails)

    else:
        notifications.show_notification(messages_header)


if __name__ == '__main__':
    filters = []

    while True:
        filter = str(input('Adicione um filtro ou aperte 0 para sair: '))

        if filter == '0':
            break

        filters.append(filter)

    if len(filters) > 0:
        print(f'Filtros aplicados: {filters}')
    else:
        print('Nenhum filtro aplicado')

    main(filters)
    schedule.every(1).minute.do(main, filters)

    while True:
        schedule.run_pending()
        time.sleep(1)
