import re

with open("names.txt") as text: #names.txt should be in your project folder for your homework
    data = text.readlines()

name_pattern = re.compile('([\w]+@[\w]+.[\w]+)')

for item in data:
    print(item)
    print(name_pattern.findall(item)[0])

# emails = ['blue1@gmail.org', 'gr2een@gmail.com', '3red@gamil.com', 'tim@killerrabbit.com']

# email_pattern = re.compile('([\w]+)@([a-z]+)(.com|.org)')
# found_emails = email_pattern.findall(emails[0])
# print(found_emails)

# for i in range(4):
#     found_emails = email_pattern.findall(emails[i])
#     print(found_emails)


# find_names = name_pattern.findall("names.txt")
# for name in find_names:
#     print("names.txt")

