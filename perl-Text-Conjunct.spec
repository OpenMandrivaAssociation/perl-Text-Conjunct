%define upstream_name    Text-Conjunct
%define upstream_version 1.0

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Join lists of items together
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Text::Conjunct joins strings together with a conjunction, typically "and"
or "or".

* *

  If there is only one string, it is just returned.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.0.0-2mdv2011.0
+ Revision: 658429
- rebuild for updates rpm-setup

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 444070
- import perl-Text-Conjunct


* Thu Sep 17 2009 cpan2dist 1.0-1mdv
- initial mdv release, generated with cpan2dist
