#! /usr/bin/env python3

import re, pyperclip

# ToDo: Create a regex for phone numbers
phoneRegex = re.compile(r'''
#415-555-0000, 555-5555, (123) 123-4444, 555-5555 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?       #area code (optional)
(\s|-)                           #first separator
\d\d\d                           #first 3 digits
-                                #separator
\d\d\d\d                         #last 4 digits
((ext(\.)?\s |x)                 #extension word part (optional)
(\d{2,5}))?                      #extension number part (optional)
)
''', re.VERBOSE)


# ToDo: Create a regex for Emails
emailRegex = re.compile(r'''
#something.+_thing@something.com

[a-zA-Z0-9_.+]+       # name part
@                     # @ symbol
[a-zA-Z0-9_.+]+       # domain name part

''',re.VERBOSE)

# ToDo: Get Text off clipboard
text = pyperclip.paste()

# ToDo: Extract email/phone from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)
print(extractedEmail)
# ToDo: Copy extracted phone/email to clipboard
