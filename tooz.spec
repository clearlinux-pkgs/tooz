#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tooz
Version  : 1.34.0
Release  : 29
URL      : http://tarballs.openstack.org/tooz/tooz-1.34.0.tar.gz
Source0  : http://tarballs.openstack.org/tooz/tooz-1.34.0.tar.gz
Summary  : Coordination library for distributed systems.
Group    : Development/Tools
License  : Apache-2.0
Requires: tooz-python
BuildRequires : Babel-python
BuildRequires : PyMySQL-python
BuildRequires : Sphinx-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : flake8
BuildRequires : flake8-python
BuildRequires : futures-python
BuildRequires : iso8601-python
BuildRequires : kazoo-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr-python
BuildRequires : netifaces-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : psycopg2-python
BuildRequires : pymemcache-python
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python-subunit-python
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : redis-python
BuildRequires : retrying-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore-python
BuildRequires : sysv_ipc-python
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testscenarios-python
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : zake-python

%description
Tooz
====
.. image:: https://img.shields.io/pypi/v/tooz.svg
:target: https://pypi.python.org/pypi/tooz/
:alt: Latest Version

%package python
Summary: python components for the tooz package.
Group: Default
Requires: Babel-python
Requires: futures-python
Requires: iso8601-python
Requires: msgpack-python-python
Requires: oslo.utils-python
Requires: retrying-python
Requires: six-python
Requires: zake-python

%description python
python components for the tooz package.


%prep
%setup -q -n tooz-1.34.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
