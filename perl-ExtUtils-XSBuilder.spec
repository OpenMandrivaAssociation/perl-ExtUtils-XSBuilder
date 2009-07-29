%define upstream_name    ExtUtils-XSBuilder
%define upstream_version 0.28

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:		1

Summary:	ExtUtils::XSBuilder - Automatic XS glue code generation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/ExtUtils/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-Tie-IxHash
# not automatically detected:
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}
Requires:	perl-Parse-RecDescent perl-Tie-IxHash

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
rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
%makeinstall_std

%__os_install_post
find $RPM_BUILD_ROOT%{_prefix} -type f -print | sed "s@^$RPM_BUILD_ROOT@@g" | grep -v perllocal.pod > %{upstream_name}-%{upstream_version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/ExtUtils/*
%{_mandir}/*/*
