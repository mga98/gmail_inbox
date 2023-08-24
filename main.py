from __future__ import print_function

from api import start_api
from get_messages import Messages


def main():
    # Call the Gmail API
    service = start_api('credentials.json')
    messages = Messages(service)

    messages_header = messages.filter()
    messages_header = messages.get_messages(messages_header)
    print(messages_header)


if __name__ == '__main__':
    main()
