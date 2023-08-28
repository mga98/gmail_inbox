from __future__ import print_function

from api import start_api
from get_messages import Messages
from notifications import Notification


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
