#!/usr/bin/python
import imaplib, email

user = 'email here'
password = ' password here'
imap_url = 'imap.gmail.com'

M = imaplib.IMAP4_SSL(imap_url)
M.login(user, password)


def save_emails():
    pass
M.select("INBOX")
result, data = M.uid('search', None, 'ALL')
inbox_item_list = data[0].split()
items = bytes()
for item in inbox_item_list:
    result2, email_data = M.uid('fetch', item, '(RFC822)')
    raw_email = email_data[0][1].decode('utf-8')
    email_message = email.message_from_string(raw_email)
    email_message.get_payload()
    for part in email_message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        
        content_type = part.get_content_type()
        if 'plain' in content_type:
            email_body = part.get_payload()
    body = ' '.join(str(e) for e in email_body.split())
    emails = [email_message["From"], email_message["Subject"].strip(), body]
    print(emails)
    #print(f'{email_message["From"]} {email_message["Subject"]}, Body: {email_body.split()}')
