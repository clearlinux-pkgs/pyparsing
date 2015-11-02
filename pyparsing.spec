#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyparsing
Version  : 2.0.5
Release  : 14
URL      : https://pypi.python.org/packages/source/p/pyparsing/pyparsing-2.0.5.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pyparsing/pyparsing-2.0.5.tar.gz
Summary  : Python parsing module
Group    : Development/Tools
License  : MIT
Requires: pyparsing-python
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
====================================
PyParsing -- A Python Parsing Module
====================================

%package python
Summary: python components for the pyparsing package.
Group: Default

%description python
python components for the pyparsing package.


%prep
%setup -q -n pyparsing-2.0.5

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
