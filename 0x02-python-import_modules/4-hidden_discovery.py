#!/usr/bin/python3
from urllib.request import urlopen

# Download the remote pyc file
url = 'https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc'
with urlopen(url) as response:
    with open('hidden_4.pyc', 'wb') as f:
        f.write(response.read())

# Save names obtained from dir() in a list
names = [name for name in dir(f) if not name.startswith('__')]

# Print out names in list
for name in names:
        print('{}'.format(name), end='\n')
