from __future__ import print_function

import sys
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
    filtro = ''

    messages_header = messages.filter(filtro)
    messages_header = messages.get_messages(messages_header)
    notifications.show_notification(messages_header)


if __name__ == '__main__':
    main()
