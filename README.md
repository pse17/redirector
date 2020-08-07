## squidRedirector это программа-редиректор для прокси-сервера Squid.

    Для того, чтобы использовать squidRedirector необходимо чтобы предварительно был настроен, сконфигурирован и запущен сам прокси-сервер Squid. Сделать это можно по [инструкции](http://www.squid-cache.org/Versions/v3/3.5/cfgman/).

    Для логирования перенаправлений и ошибок используется rsyslog который также должен быть настроен и запущен. [Инструкция](https://www.rsyslog.com/doc/v8-stable/)
    
Файл конфигурации redirector.conf
>{
>        "откуда": "куда",
>}
например
>    {
>        "lurkmore.to": "wikipedia.org",
>    }

Для установки скачайте **squidRedirector-0.1-1.fc31.x86_64.rpm**
Наберите *sudo dnf install squidRedirector-0.1-1.fc31.x86_64.rpm*
Перезапустите прокси-сервер Squid *systemctl restart squid.service*