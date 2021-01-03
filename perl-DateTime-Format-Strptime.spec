#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DateTime-Format-Strptime
Version  : 1.78
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-Strptime-1.78.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-Strptime-1.78.tar.gz
Summary  : 'Parse and format strp and strf time patterns'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-DateTime-Format-Strptime-license = %{version}-%{release}
Requires: perl-DateTime-Format-Strptime-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(DateTime)
BuildRequires : perl(DateTime::Locale)
BuildRequires : perl(DateTime::Locale::Base)
BuildRequires : perl(DateTime::Locale::FromData)
BuildRequires : perl(DateTime::TimeZone)
BuildRequires : perl(Params::ValidationCompiler)
BuildRequires : perl(Specio)
BuildRequires : perl(Specio::Declare)
BuildRequires : perl(Specio::Exporter)
BuildRequires : perl(Specio::Library::Builtins)
BuildRequires : perl(Specio::Library::String)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Warnings)
BuildRequires : perl(Try::Tiny)

%description
# NAME
DateTime::Format::Strptime - Parse and format strp and strf time patterns

%package dev
Summary: dev components for the perl-DateTime-Format-Strptime package.
Group: Development
Provides: perl-DateTime-Format-Strptime-devel = %{version}-%{release}
Requires: perl-DateTime-Format-Strptime = %{version}-%{release}

%description dev
dev components for the perl-DateTime-Format-Strptime package.


%package license
Summary: license components for the perl-DateTime-Format-Strptime package.
Group: Default

%description license
license components for the perl-DateTime-Format-Strptime package.


%package perl
Summary: perl components for the perl-DateTime-Format-Strptime package.
Group: Default
Requires: perl-DateTime-Format-Strptime = %{version}-%{release}

%description perl
perl components for the perl-DateTime-Format-Strptime package.


%prep
%setup -q -n DateTime-Format-Strptime-1.78
cd %{_builddir}/DateTime-Format-Strptime-1.78

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-Strptime
cp %{_builddir}/DateTime-Format-Strptime-1.78/LICENSE %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-Strptime/029783b2524e7b319c1e4ada55a886b307e72128
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DateTime::Format::Strptime.3
/usr/share/man/man3/DateTime::Format::Strptime::Types.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DateTime-Format-Strptime/029783b2524e7b319c1e4ada55a886b307e72128

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/DateTime/Format/Strptime.pm
/usr/lib/perl5/vendor_perl/5.30.3/DateTime/Format/Strptime/Types.pm
