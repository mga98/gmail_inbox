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


def main():
    # Call the Gmail API
    service = start_api('credentials.json')

    messages = Messages(service)
    notifications = Notification()
    sender = 'Estácio'
    subject = 'Miguel'

    messages_header = messages.filter(sender, subject)
    messages_header = messages.get_messages(messages_header)
    notifications.show_notification(messages_header)


schedule.every(30).seconds.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
