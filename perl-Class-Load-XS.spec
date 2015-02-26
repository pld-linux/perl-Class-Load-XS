#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Class
%define		pnam	Load-XS
%include	/usr/lib/rpm/macros.perl
Summary:	Class::Load::XS - XS implementation of parts of Class::Load
Summary(pl.UTF-8):	Class::Load::XS - implementacja XS części modułu Class::Load
Name:		perl-Class-Load-XS
Version:	0.06
Release:	4
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a3e73647f84eb8bd26847c3dda78f0d3
URL:		http://search.cpan.org/dist/Class-Load-XS/
BuildRequires:	perl-Module-Build >= 0.3601
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Load >= 0.20
BuildRequires:	perl-Module-Implementation >= 0.04
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an XS implementation for portions of Class::Load.
See Class::Load for API details.

%description -l pl.UTF-8
Ten moduł dostarcza implementację XS niektórych części Class::Load.
Więcej szczegółów na temat API w Class::Load.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/Class/Load
%{perl_vendorarch}/Class/Load/XS.pm
%dir %{perl_vendorarch}/auto/Class/Load
%dir %{perl_vendorarch}/auto/Class/Load/XS
%attr(755,root,root) %{perl_vendorarch}/auto/Class/Load/XS/XS.so
%{_mandir}/man3/Class::Load::XS.3pm*
