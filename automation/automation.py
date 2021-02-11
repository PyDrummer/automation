import shutil
import re

email = ["davismichele@wright.info", "danielletaylor@hotmail.com", "codymorrow@hotmail.com"]
phone = ["946.856.8523x7729", "437-807-8509x41110", "(461)731-3087x6570"]

# read = shutil.copy('content.text', 'new_assets')
emailRe = re.compile(r"\w+.\w+@\w+.\w+.(com|net|org|info|biz)")
phoneRe = re.compile(r'(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'
)


all_lines = []
emailFound = []
phoneFound = []
new_phone = []
# for i in email:
#     find = emailRe.search(i)
#     found.append(find.group())

# for i in phone:
#     find = phoneRe.search(i)
#     phoneFound.append(find.group())

with open("assets/potential-contacts.txt", 'r') as read:
    # print(read)
    for lines in read:
        split_read = lines.split(" ")
        # print(split_read)
        all_lines.append(lines)
        # print(all_lines)
        

    # split_read = read_line.split(' ')
    # print(split_read)
    for i in all_lines:
        if phoneRe.search(i):
            find_phone = phoneRe.search(i)
            found = find_phone.group()
            if len(found) < 10:
                found = '206-' + found[:3] + "-" + found[4:]
            if len(found) == 10:
                found = found[:3] + "-" + found[3:6] + "-" + found[6:]
            if len(found.split('x')[0]) < 10:
                # print(found.split('x')[0])
                found = '206-' + found
                # print(found)
            if '.' in found:
                found = found.replace('.', '-')
                # print(found)
            if '+1' in found or '(' in found:
                found = found.strip('+1-')
                found = found.strip('(')
                found = found.replace(')', '-')
            if '1-' in found[:2]:
                found = found.strip('1-')

            phoneFound.append(found)

                # print(found)

        if emailRe.search(i):
            find_email = emailRe.search(i)
            found = find_email.group()
            emailFound.append(found)
    
    # Checking for dupes:
    for num in phoneFound:
        # print('old phone found', phoneFound.count(num))
        while phoneFound.count(num) > 1:
            phoneFound.remove(num)
        
    # Checking for dupes:
    for num in emailFound:
        # print('old email found', emailFound.count(num))
        while emailFound.count(num) > 1:
            emailFound.remove(num)

phoneFound.sort()
# print(phoneFound)
emailFound.sort()
# print(emailFound)

# for writing to a file now
with open('assets/phone_numbers.txt', 'w+') as f:
    for nums in phoneFound:
        f.write(f'{nums}\n')

with open('assets/emails.txt', 'w+') as f:
    for email in emailFound:
        f.write(f'{email}\n')
