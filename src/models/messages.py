from typing import List


class Messages:
    def __init__(self, service):
        self.service = service

    def filter(
        self,
        userId='me',
        includeSpamTrash=True,
        labelIds='INBOX',
    ) -> object:
        '''
        Get all the unread emails from the current user and inbox
        '''
        return self.service.users().messages().list(
            userId=userId,
            includeSpamTrash=includeSpamTrash,
            labelIds=labelIds,
            q='category:primary is:unread',
        ).execute()

    def get_messages(self, results) -> List[dict] | str:
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
