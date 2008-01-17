%define module	ExtUtils-XSBuilder

Summary:	ExtUtils::XSBuilder - Automatic XS glue code generation
Name:		perl-%{module}
Version:	0.28
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/ExtUtils/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-Tie-IxHash
# not automatically detected:
Requires:	perl-Parse-RecDescent perl-Tie-IxHash
BuildArch:	noarch
Epoch:		1
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ExtUtils::XSBuilder is a set modules to parse C header files and create XS
glue code and documentation out of it. Idealy this allows to "write" an
interface to a C library without coding a line. Since no C-API is ideal,
some adjuments are necessary most of the time. So to use this module you
must still be familiar with C and XS programming, but it removes a lot of
stupid work and copy&paste from you. Also when the C API changes, most
of the time you only have to rerun XSBuilder to get your new Perl API.
 
%prep

%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
%makeinstall_std

%__os_install_post
find $RPM_BUILD_ROOT%{_prefix} -type f -print | sed "s@^$RPM_BUILD_ROOT@@g" | grep -v perllocal.pod > %{module}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/ExtUtils/*
%{_mandir}/*/*
