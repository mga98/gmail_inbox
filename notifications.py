from win10toast import ToastNotifier


class Notification:
    def __init__(self):
        self.toast = ToastNotifier()

    def show_notification(self, messages: list) -> None:
        if not messages:
            return

        if len(messages) == 1:
            self.toast.show_toast(
                f'De {messages[0]["from"]}',
                f'{messages[0]["subject"]}',
                duration=5,
                threaded=True
            )

        else:
            self.toast.show_toast(
                'Suas mensagens',
                f'Você tem {len(messages)} novas mensagens',
                duration=5,
                threaded=True
            )
