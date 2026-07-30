%define upstream_name    ExtUtils-XSBuilder
%define upstream_version 0.28
Name:		perl-%{upstream_name}
Version:	0.28
Release:	1
Epoch:		1

Summary:	ExtUtils::XSBuilder - Automatic XS glue code generation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/ExtUtils-XSBuilder
Source0:	https://cpan.metacpan.org/authors/id/G/GR/GRICHTER/ExtUtils-XSBuilder-0.28.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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


