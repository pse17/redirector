## squidRedirector программа-редиректор для прокси-сервера Squid.

Настраивается в файле конфигурации redirector.conf.
{"откуда": "куда",} например:    
{    
    "lurkmore.to": "wikipedia.org",    
}        

Для установки скачайте [**squidRedirector-0.1-1.fc31.x86_64.rpm**](https://github.com/pse17/redirector/blob/master/x86_64/squidRedirector-0.1-1.fc31.x86_64.rpm)    
Наберите:    
> *sudo dnf install squidRedirector-0.1-1.fc31.x86_64.rpm*

Перезапустите прокси-сервер Squid и rsyslog если они уже были установлены
> *systemctl restart squid*    
> *systemctl restart rsyslog*

Eсли нет просто перезагрузите систему. 