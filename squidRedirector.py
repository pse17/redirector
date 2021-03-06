#!/usr/bin/env python3
import sys
import json
import logging
from logging import config

CONFIG_PATH = '/usr/local/squidRedirector/redirector.conf'

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


# Читаем конфиг на каждом запросе т.к. все изменения должны работать сразу
def read_config():
    try:
        with open(CONFIG_PATH) as config_file:
            config = json.load(config_file)
    except Exception as err:
        app_logger.error(err)
        config = None
    return config


def check_url(url):    
    result_line = 'ERR\n'
    
    config = read_config()
    # Если конфиг прочитать не удалось пропускаем все
    if config is None:
        return result_line
    
    # Обходим все ключи в словаре
    for site_from, site_to in config.items():
        if site_from in url:
            result = "OK"
            kv_pairs = " status=301 url=https://" + site_to
            new_url = " 301:https://" + site_to
            
            result_line = result + kv_pairs + new_url + "\n"
            redirect_logger.info('Redirected from %s to %s' % (site_from, site_to))
    
    return result_line


app_logger.info('Redirector started')

while True:
    try:
        line  = sys.stdin.readline()
    except EOFError:
        app_logger.debug('Redirector closed by EOF')
        break
    except Exception as err:
        app_logger.error(err)
        break

    line_parts = line.split(' ')
    result_line = check_url(line_parts[0])

    sys.stdout.write(result_line)
    sys.stdout.flush()
