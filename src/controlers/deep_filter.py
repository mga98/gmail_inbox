def deep_filter(emails: list, filters: list) -> list:
    filtered_emails = []

    for email in emails:
        lower_subject = email['subject'].lower()
        lower_from = email['from'].lower()

        for filter in filters:
            if filter.lower() in lower_subject or filter.lower() in lower_from:
                filtered_emails.append(email)
                break

    return filtered_emails
