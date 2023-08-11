#!/usr/bin/python3
import hidden_4
hidden_names = dir(hidden_4)
for name in hidden_names:
    if not name.startswith('__'):
        print('{}'.format(name), end='\n')
