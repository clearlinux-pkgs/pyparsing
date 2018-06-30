#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyparsing
Version  : 2.2.0
Release  : 45
URL      : http://pypi.debian.net/pyparsing/pyparsing-2.2.0.tar.gz
Source0  : http://pypi.debian.net/pyparsing/pyparsing-2.2.0.tar.gz
Summary  : Python parsing module
Group    : Development/Tools
License  : MIT
Requires: pyparsing-python3
Requires: pyparsing-python
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest

BuildRequires : python3-dev
BuildRequires : setuptools

%description
====================================
PyParsing -- A Python Parsing Module
====================================

%package legacypython
Summary: legacypython components for the pyparsing package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pyparsing package.


%package python
Summary: python components for the pyparsing package.
Group: Default
Requires: pyparsing-python3

%description python
python components for the pyparsing package.


%package python3
Summary: python3 components for the pyparsing package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyparsing package.


%prep
%setup -q -n pyparsing-2.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519350557
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
export SOURCE_DATE_EPOCH=1519350557
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
