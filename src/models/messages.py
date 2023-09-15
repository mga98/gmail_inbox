class Messages:
    def __init__(self, service):
        self.service = service

    def filter(
        self,
        filter='',
        userId='me',
        includeSpamTrash=False,
        labelIds='INBOX',
    ) -> object:
        '''
        Filter the email that will be displayed
        '''
        return self.service.users().messages().list(
            userId=userId,
            includeSpamTrash=includeSpamTrash,
            labelIds=labelIds,
            q=f'category:primary subject:{filter} is:unread',
        ).execute()

    def get_messages(self, results) -> list | str:
        '''
        Return a list of emails subjects and senders
        '''
        messages = results.get('messages')

        if not messages:
            return False

        messages_header = list()

        for msg in messages:
            txt = self.service.users().messages().get(
                userId='me', id=msg['id']
            ).execute()

            try:
                payload = txt['payload']
                headers = payload['headers']

                for d in headers:
                    if d['name'] == 'Subject':
                        subject = d['value']

                    if d['name'] == 'From':
                        sender = d['value']

                messages_header.append({
                    'subject': subject,
                    'from': sender
                })

            except Exception:
                pass

        return messages_header