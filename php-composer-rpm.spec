# Disable automatic dependency processing
# (prevents endless loop if php-composer is already installed on buildsys)
AutoReqProv: no

Name: php-composer
Version: 1.0.0
Release: %{BUILD_NUMBER}
Summary: Dependency Manager for PHP
Group: Development/Libraries
License: MIT
URL: http://getcomposer.org/
BuildArch: noarch
Prefix: /usr/bin
%define  _rpmfilename  %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm

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



%build
# % {__mkdir} -p "${RPM_BUILD_ROOT}"



%install
echo
echo "Install.."
# delete existing rpm's
%{__rm} -fv "%{_rpmdir}/%{name}"*.noarch.rpm
# create directories
%{__install} -d -m 755 \
	"${RPM_BUILD_ROOT}%{prefix}" \
		|| exit 1

# download from getcomposer.org
wget -O "${RPM_BUILD_ROOT}%{prefix}/composer" "https://getcomposer.org/composer.phar" \
	|| exit 1

# copy composer.phar
%{__chmod} 555 "${RPM_BUILD_ROOT}%{prefix}/composer" \
	|| exit 1



%clean
if [ ! -z "%{_topdir}" ]; then
	%{__rm} -rf --preserve-root "%{_topdir}" \
		|| echo "Failed to delete build root (probably fine..)"
fi



### Files ###
%files
%defattr(-,root,root,-)
%{prefix}/composer

