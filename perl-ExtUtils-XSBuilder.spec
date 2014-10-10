%define upstream_name    ExtUtils-XSBuilder
%define upstream_version 0.28

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Epoch:		1

Summary:	ExtUtils::XSBuilder - Automatic XS glue code generation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/ExtUtils/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Parse::RecDescent)
BuildRequires:	perl(Tie::IxHash)

BuildArch:	noarch

# not automatically detected:
Requires:	perl(Parse::RecDescent)
Requires:	perl(Tie::IxHash)

%description
ExtUtils::XSBuilder is a set modules to parse C header files and create XS
glue code and documentation out of it. Idealy this allows to "write" an
interface to a C library without coding a line. Since no C-API is ideal,
some adjuments are necessary most of the time. So to use this module you
must still be familiar with C and XS programming, but it removes a lot of
stupid work and copy&paste from you. Also when the C API changes, most
of the time you only have to rerun XSBuilder to get your new Perl API.
 
%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/ExtUtils/*
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.280.0-1mdv2010.0
+ Revision: 403166
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1:0.28-6mdv2009.0
+ Revision: 256863
- rebuild

* Thu Jan 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1:0.28-4mdv2008.1
+ Revision: 154205
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1:0.28-3mdv2008.0
+ Revision: 67816
- rebuild


* Sun Mar 11 2007 Oden Eriksson <oeriksson@mandriva.com> 0.28-2mdv2007.1
+ Revision: 141320
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-ExtUtils-XSBuilder

* Tue Apr 11 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.28-1mdk
- 0.28
- Fix URL 
- Fix SOURCE( rpmbuildupdate friendly)
- use mkrel

* Fri May 20 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.27-2mdk
- fix missing dependancies

* Fri Jan 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.27-1mdk
- 0.27
- add tests

* Tue Aug 03 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.23-1mdk
- roll back to 0.23 as embperl won't build until we have 0.26

* Mon Aug 02 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.25-2mdk
- rebuild for new perl

* Sat Apr 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.25-1mdk
- 0.25

