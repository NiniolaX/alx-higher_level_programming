#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    hidden_names = dir(hidden_4)
    for name in hidden_names:
        if not name.startswith('__'):
            print('{}'.format(name), end='\n')
