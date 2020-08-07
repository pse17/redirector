Name:    squidRedirector
Version: 0.1
Release: 1%{?dist}
Summary: A simple redirector for squid.

License: GPL
Source0: squidRedirector-0.1.tar.gz
Requires: python >= 3.7, squid >= 3.5, rsyslog

%description
A simple redirector for squid.

%prep
%autosetup

%install
mkdir -p %{buildroot}/usr/local/squidRedirector
mkdir -p %{buildroot}/etc/rsyslog.d/
install -p -m 755 squidRedirector.py %{buildroot}/usr/local/squidRedirector
install -p -m 644 redirector.conf %{buildroot}/usr/local/squidRedirector
install -p -m 644 README.md %{buildroot}/usr/local/squidRedirector
install -p -m 644 rsyslog_redirector.conf %{buildroot}/etc/rsyslog.d/

%files
%defattr(-,root,root)
/usr/local/squidRedirector/squidRedirector.py
/usr/local/squidRedirector/redirector.conf
/usr/local/squidRedirector/README.md
/etc/rsyslog.d/rsyslog_redirector.conf

%post
echo "url_rewrite_program /usr/bin/python3 /usr/local/squidRedirector/squidRedirector.py" >> /etc/squid/squid.conf 

%changelog


