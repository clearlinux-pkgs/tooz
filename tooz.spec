#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEB6CCA1483FA74EC (infra-root@openstack.org)
#
Name     : tooz
Version  : 1.56.0
Release  : 47
URL      : https://tarballs.openstack.org/tooz/tooz-1.56.0.tar.gz
Source0  : https://tarballs.openstack.org/tooz/tooz-1.56.0.tar.gz
Source99 : https://tarballs.openstack.org/tooz/tooz-1.56.0.tar.gz.asc
Summary  : Coordination library for distributed systems.
Group    : Development/Tools
License  : Apache-2.0
Requires: tooz-python
Requires: PyMySQL
Requires: Sphinx
Requires: coverage
Requires: enum34
Requires: fasteners
Requires: fixtures
Requires: futures
Requires: futurist
Requires: kazoo
Requires: msgpack-python
Requires: os-testr
Requires: oslo.serialization
Requires: oslo.utils
Requires: oslosphinx
Requires: pbr
Requires: psycopg2
Requires: pymemcache
Requires: python-mock
Requires: python-subunit
Requires: redis
Requires: reno
Requires: requests
Requires: six
Requires: stevedore
Requires: testrepository
Requires: testtools
Requires: voluptuous
Requires: zake
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Tooz
====
.. image:: https://img.shields.io/pypi/v/tooz.svg
:target: https://pypi.python.org/pypi/tooz/
:alt: Latest Version

%package python
Summary: python components for the tooz package.
Group: Default

%description python
python components for the tooz package.


%prep
%setup -q -n tooz-1.56.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493680255
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1493680255
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
