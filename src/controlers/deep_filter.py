def deep_filter(emails: list, filters: list) -> list:
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
