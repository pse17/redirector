#!/usr/bin/python
import sys

pattern = 'yandex.ru'
repl = 'google.com'
result = 'ERR\n'

while True:
    line  = sys.stdin.readline().strip()
    s = line.split(' ')

    if s[0].find(pattern) != -1:
        result = 'OK status=302 url="https://google.com"\n'

    sys.stdout.write(result)
    sys.stdout.flush()


