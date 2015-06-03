# Set the version number to the date of the snapshot release
%define _version %(cat %{_sourcedir}/version.txt)

# Disable automatic dependency processing
# (prevents endless loop if php-composer is already installed on buildsys)
AutoReqProv: no

Name: php-composer
Version: %{_version}
Release: 1
Summary: Dependency Manager for PHP
Group: Development/Libraries
License: MIT
URL: http://getcomposer.org/
Source0: composer.phar
Source1: version.txt
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

Requires: php-cli
Requires: php-curl
Requires: php-date
Requires: php-hash
Requires: php-iconv
Requires: php-json
Requires: php-libxml
Requires: php-mbstring
Requires: php-openssl
Requires: php-pcre
Requires: php-reflection
Requires: php-simplexml
Requires: php-spl
Requires: php-tokenizer
Requires: php-xsl
Requires: php-zip

%description
Composer is a tool for dependency management in PHP. It allows you to declare
the dependent libraries your project needs and it will install them in your
project for you.

%prep
cp %{SOURCE0} .

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin/
cp -r composer.phar %{buildroot}/usr/bin/composer

%clean
rm -rf %{buildroot}

%files
%defattr(755,root,root)
/usr/bin/composer
