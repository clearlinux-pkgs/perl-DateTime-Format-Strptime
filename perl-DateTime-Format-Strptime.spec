#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DateTime-Format-Strptime
Version  : 1.75
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-Strptime-1.75.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-Strptime-1.75.tar.gz
Summary  : 'Parse and format strp and strf time patterns'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-DateTime-Format-Strptime-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(Class::Data::Inheritable)
BuildRequires : perl(Class::Inspector)
BuildRequires : perl(Class::Singleton)
BuildRequires : perl(DateTime)
BuildRequires : perl(DateTime::Locale)
BuildRequires : perl(DateTime::Locale::Base)
BuildRequires : perl(DateTime::Locale::FromData)
BuildRequires : perl(DateTime::TimeZone)
BuildRequires : perl(Devel::StackTrace)
BuildRequires : perl(Eval::Closure)
BuildRequires : perl(Exception::Class)
BuildRequires : perl(File::ShareDir)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::DeprecationManager)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Params::ValidationCompiler)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Specio)
BuildRequires : perl(Specio::Declare)
BuildRequires : perl(Specio::Exporter)
BuildRequires : perl(Specio::Library::Builtins)
BuildRequires : perl(Specio::Library::String)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Identify)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Sub::Name)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Warnings)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(Variable::Magic)
BuildRequires : perl(namespace::autoclean)
BuildRequires : perl(namespace::clean)

%description
# NAME
DateTime::Format::Strptime - Parse and format strp and strf time patterns

%package dev
Summary: dev components for the perl-DateTime-Format-Strptime package.
Group: Development
Provides: perl-DateTime-Format-Strptime-devel = %{version}-%{release}

%description dev
dev components for the perl-DateTime-Format-Strptime package.


%package license
Summary: license components for the perl-DateTime-Format-Strptime package.
Group: Default

%description license
license components for the perl-DateTime-Format-Strptime package.


%prep
%setup -q -n DateTime-Format-Strptime-1.75

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-Strptime
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-Strptime/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/DateTime/Format/Strptime.pm
/usr/lib/perl5/vendor_perl/5.28.1/DateTime/Format/Strptime/Types.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DateTime::Format::Strptime.3
/usr/share/man/man3/DateTime::Format::Strptime::Types.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DateTime-Format-Strptime/LICENSE
