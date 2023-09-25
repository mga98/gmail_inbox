class Messages:
    def __init__(self, service):
        self.service = service

    def filter(
        self,
        sender=None,
        subject=None,
        userId='me',
        includeSpamTrash=False,
        labelIds='INBOX',
    ) -> object:
        '''
        Filter the email by sender or subject or both
        '''
        if sender and subject:
            return self.service.users().messages().list(
                userId=userId,
                includeSpamTrash=includeSpamTrash,
                labelIds=labelIds,
                q=f'category:primary from:{sender} subject:{subject} is:unread',  # noqa
            ).execute()

        elif sender:
            return self.service.users().messages().list(
                userId=userId,
                includeSpamTrash=includeSpamTrash,
                labelIds=labelIds,
                q=f'category:primary from:{sender} is:unread',
            ).execute()

        elif subject:
            return self.service.users().messages().list(
                userId=userId,
                includeSpamTrash=includeSpamTrash,
                labelIds=labelIds,
                q=f'category:primary subject:{subject} is:unread',
            ).execute()

        else:
            return self.service.users().messages().list(
                userId=userId,
                includeSpamTrash=includeSpamTrash,
                labelIds=labelIds,
                q='category:primary is:unread',
            ).execute()

    def get_messages(self, results) -> list | str:
        '''
        Returns a list of email senders and subjects
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
