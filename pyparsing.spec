#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyparsing
Version  : 3.0.4
Release  : 92
URL      : https://files.pythonhosted.org/packages/bf/6f/509e501ff67a335186c8adcdc3ee62195919731b22796b0690658a76bb6f/pyparsing-3.0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/bf/6f/509e501ff67a335186c8adcdc3ee62195919731b22796b0690658a76bb6f/pyparsing-3.0.4.tar.gz
Summary  : Python parsing module
Group    : Development/Tools
License  : MIT
Requires: pyparsing-license = %{version}-%{release}
Requires: pyparsing-python = %{version}-%{release}
Requires: pyparsing-python3 = %{version}-%{release}
Requires: Jinja2
BuildRequires : Jinja2
BuildRequires : buildreq-distutils3
BuildRequires : nose
BuildRequires : py
BuildRequires : pytest

%description
====================================
        
        |Build Status| |Coverage|
        
        Introduction
        ============
        
        The pyparsing module is an alternative approach to creating and
        executing simple grammars, vs. the traditional lex/yacc approach, or the
        use of regular expressions. The pyparsing module provides a library of
        classes that client code uses to construct the grammar directly in
        Python code.
        
        *[Since first writing this description of pyparsing in late 2003, this
        technique for developing parsers has become more widespread, under the
        name Parsing Expression Grammars - PEGs. See more information on PEGs*

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
Provides: pypi(pyparsing)

%description python3
python3 components for the pyparsing package.


%prep
%setup -q -n pyparsing-3.0.4
cd %{_builddir}/pyparsing-3.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635641584
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyparsing
cp %{_builddir}/pyparsing-3.0.4/LICENSE %{buildroot}/usr/share/package-licenses/pyparsing/df156c6a0a89ed2a3bd4a473c68cf85907509ca0
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
