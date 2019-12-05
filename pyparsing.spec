#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyparsing
Version  : 2.4.5
Release  : 72
URL      : https://files.pythonhosted.org/packages/00/32/8076fa13e832bb4dcff379f18f228e5a53412be0631808b9ca2610c0f566/pyparsing-2.4.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/00/32/8076fa13e832bb4dcff379f18f228e5a53412be0631808b9ca2610c0f566/pyparsing-2.4.5.tar.gz
Summary  : Python parsing module
Group    : Development/Tools
License  : MIT
Requires: pyparsing-license = %{version}-%{release}
Requires: pyparsing-python = %{version}-%{release}
Requires: pyparsing-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : nose
BuildRequires : py
BuildRequires : pytest

%description
PyParsing -- A Python Parsing Module
====================================
|Build Status|

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
%setup -q -n pyparsing-2.4.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573426454
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyparsing
cp %{_builddir}/pyparsing-2.4.5/LICENSE %{buildroot}/usr/share/package-licenses/pyparsing/df156c6a0a89ed2a3bd4a473c68cf85907509ca0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyparsing/df156c6a0a89ed2a3bd4a473c68cf85907509ca0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
