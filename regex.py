import re

chat1 = 'I am missing my order 532255. My number is 3526221732 and address is...'
pattern = 'order[^\d]*(\d{6})'

matches = re.findall(pattern, chat1)
print(matches)