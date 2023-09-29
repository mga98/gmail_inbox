import json

from typing import List


class Filter:
    def deep_filter(emails: List[str], filters: List[str]) -> List[str]:
        filtered_emails = []

        if emails:
            for email in emails:
                lower_subject = email['subject'].lower()
                lower_from = email['from'].lower()

                for filter in filters:
                    filter = filter.lower()

                    if filter in lower_subject or filter in lower_from:
                        filtered_emails.append(email)
                        break

        return filtered_emails

    def save_filters(self, filters: List[str]) -> None:
        with open('filters.json', 'w') as filters_json:
            json.dump(filters, filters_json)
