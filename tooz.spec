#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tooz
Version  : 1.62.0
Release  : 49
URL      : https://files.pythonhosted.org/packages/64/e8/60a155f699205e19888d8faf1ba7c0a972578983fafc1758e68e0d52d50e/tooz-1.62.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/64/e8/60a155f699205e19888d8faf1ba7c0a972578983fafc1758e68e0d52d50e/tooz-1.62.0.tar.gz
Summary  : Coordination library for distributed systems.
Group    : Development/Tools
License  : Apache-2.0
Requires: tooz-python3
Requires: tooz-license
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
Requires: openstackdocstheme
Requires: os-testr
Requires: oslo.serialization
Requires: oslo.utils
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
Requires: tenacity
Requires: testrepository
Requires: testtools
Requires: voluptuous
Requires: zake
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
====

%package license
Summary: license components for the tooz package.
Group: Default

%description license
license components for the tooz package.


%package python
Summary: python components for the tooz package.
Group: Default
Requires: tooz-python3

%description python
python components for the tooz package.


%package python3
Summary: python3 components for the tooz package.
Group: Default
Requires: python3-core

%description python3
python3 components for the tooz package.


%prep
%setup -q -n tooz-1.62.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532376535
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/tooz
cp LICENSE %{buildroot}/usr/share/doc/tooz/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/tooz/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
