#!/usr/bin/env python
import sys
import json
import logging
from logging import config

CONFIG_PATH = '/etc/squid/redirector.json'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(module)s P%(process)d T%(thread)d %(message)s'
            },
        },
    'handlers': {
        'sys-logger5': {
            'class': 'logging.handlers.SysLogHandler',
            'address': '/dev/log',
            'facility': "local5",
            'formatter': 'verbose',
            },
        'sys-logger6': {
            'class': 'logging.handlers.SysLogHandler',
            'address': '/dev/log',
            'facility': "local6",
            'formatter': 'verbose',
            },
        },
    'loggers': {
        'redirect_logger': {
            'handlers': ['sys-logger5'],
            'level': logging.INFO ,
            'propagate': True,
            },
        'app_logger': {
            'handlers': ['sys-logger6'],
            'level': logging.DEBUG,
            'propagate': True,
            },
        }
    }
config.dictConfig(LOGGING)
redirect_logger = logging.getLogger("redirect_logger")
app_logger = logging.getLogger("app_logger")


# Читаем конфиг на каждой итерации т.к. все изменения должны работать сразу
def read_config():
    try:
        with open(CONFIG_PATH) as config_file:
            config = json.load(config_file)
    except Exception as err:
        app_logger.error(err)
        config = None
    return config


def check_url(url):    
    result, url = "ERR", ''
    
    config = read_config()
    # Если конфиг прочитать не удалось пропускаем все
    if config is None:
        return result, url

    for site_from, site_to in config.items():
        if url.startswith(site_from):
            url = url.replace(site_from, site_to)
            url = "302:http://" + url 
            result = "OK"
    
    return result, url


app_logger.info('Redirector started')
while True:
    try:
        line  = sys.stdin.readline()
        app_logger.debug(line) # Для отладки
    except EOFError:
        app_logger.debug('Redirector closed by EOF')
        break
    except Exception as err:
        app_logger.debug(err)
        break

    result, new_url = check_url(line.split(' ')[0])
    if result == "OK":
        redirect_logger.info(new_url)

    sys.stdout.write('%s %s\n' % (result, new_url) )
    sys.stdout.flush()


