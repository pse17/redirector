#!/usr/bin/env python
import sys
import json

def read_config():
    with open('redirector.json', "r") as j:
        config = json.load(j)
    return config["sites"]


def check_url(url):

    status = "ERR"
    sites = read_config()
    
    for site in sites:
        if url.startswith(site.key()):
            url.replace(site.key, site.value())
            url = "http://" + url 
            status = "OK"
    
    if status == "ERR":
        url = ""
    
    return status, url


while True:
    url  = sys.stdin.readline().strip().split(' ')[0]

    status, new_url = check_url(url)

    sys.stdout.write('%s %s\n' % (status, new_url) )
    sys.stdout.flush()


