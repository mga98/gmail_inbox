from __future__ import print_function

import sys
import time
import schedule
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controlers.notifications import Notification  # noqa
from controlers.deep_filter import deep_filter  # noqa
from controlers.api import start_api  # noqa
from models.messages import Messages  # noqa


def main(filters: list = None):
    # Call the Gmail API
    service = start_api('credentials.json')

    messages = Messages(service)
    notifications = Notification()

    messages_header = messages.filter()
    messages_header = messages.get_messages(messages_header)

    if filters:
        filtered_emails = deep_filter(messages_header, filters)
        notifications.show_notification(filtered_emails)

    else:
        notifications.show_notification(messages_header)


if __name__ == '__main__':
    filters = ['vagas', 'vaga', 'retorno', 'patense', 'entrevista']

    main(filters)
    schedule.every(1).minute.do(main, filters)

    while True:
        schedule.run_pending()
        time.sleep(1)
