#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyparsing
Version  : 2.3.1
Release  : 59
URL      : https://files.pythonhosted.org/packages/b9/b8/6b32b3e84014148dcd60dd05795e35c2e7f4b72f918616c61fdce83d27fc/pyparsing-2.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b9/b8/6b32b3e84014148dcd60dd05795e35c2e7f4b72f918616c61fdce83d27fc/pyparsing-2.3.1.tar.gz
Summary  : Python parsing module
Group    : Development/Tools
License  : MIT
Requires: pyparsing-license = %{version}-%{release}
Requires: pyparsing-python = %{version}-%{release}
Requires: pyparsing-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : nose
BuildRequires : py
BuildRequires : pytest

%description
PyParsing â A Python Parsing Module
===================================
|Build Status|

%package legacypython
Summary: legacypython components for the pyparsing package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pyparsing package.


%package license
Summary: license components for the pyparsing package.
Group: Default

%description license
license components for the pyparsing package.


%package python
Summary: python components for the pyparsing package.
Group: Default
Requires: pyparsing-python3 = %{version}-%{release}

%description python
python components for the pyparsing package.


%package python3
Summary: python3 components for the pyparsing package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyparsing package.


%prep
%setup -q -n pyparsing-2.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547436553
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
export SOURCE_DATE_EPOCH=1547436553
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyparsing
cp LICENSE %{buildroot}/usr/share/package-licenses/pyparsing/LICENSE
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyparsing/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
