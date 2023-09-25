from win10toast import ToastNotifier

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


class Notification:
    def __init__(self):
        self.toast = ToastNotifier()

    def show_notification(self, messages: list) -> None:
        """
        Shows a notification with "from" and "subject" when a new email arrives
        """
        if not messages:
            return

        if len(messages) == 1:
            self.toast.show_toast(
                f'De {messages[0]["from"]}',
                f'{messages[0]["subject"]}',
                duration=20,
                threaded=True
            )

        else:
            self.toast.show_toast(
                'Suas mensagens',
                f'Você tem {len(messages)} novas mensagens',
                duration=5,
                threaded=True
            )
