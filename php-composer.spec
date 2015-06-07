# Disable automatic dependency processing
# (prevents endless loop if php-composer is already installed on buildsys)
AutoReqProv: no

Name: php-composer
Version: 1.0.0.%{BUILD_NUMBER}
Release: 2
Summary: Dependency Manager and build tools for PHP
Group: Development/Libraries
License: MIT
URL: http://getcomposer.org/
BuildArch: noarch
Prefix: /usr/bin
%define  _rpmfilename  %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm

#Requires: php-cli
#Requires: php-curl
#Requires: php-date
#Requires: php-hash
#Requires: php-iconv
#Requires: php-json
#Requires: php-libxml
#Requires: php-mbstring
#Requires: php-openssl
#Requires: php-pcre
#Requires: php-reflection
#Requires: php-simplexml
#Requires: php-spl
#Requires: php-tokenizer
#Requires: php-xsl
#Requires: php-zip

%description
Composer is a tool for dependency management in PHP. It allows you to declare
the dependent libraries your project needs and it will install them in your
project for you.



%prep



%build



%install
echo
echo "Install.."
# delete existing rpm's
%{__rm} -fv "%{_rpmdir}/%{name}"*.noarch.rpm
# create directories
%{__install} -d -m 755 \
	"${RPM_BUILD_ROOT}%{prefix}" \
		|| exit 1
# download composer and box
echo "Downloading.."
pushd "${RPM_BUILD_ROOT}%{prefix}"
	echo;echo
	curl -Ss  https://getcomposer.org/installer | php
	mv composer.phar composer || exit 1
	echo;echo
	curl -SsL https://box-project.github.io/box2/installer.php | php
	mv box.phar      box      || exit 1
	echo;echo
popd
%{__chmod} 555 "${RPM_BUILD_ROOT}%{prefix}/composer" || exit 1
%{__chmod} 555 "${RPM_BUILD_ROOT}%{prefix}/box"      || exit 1

# TEMPORARY FIX FOR: https://github.com/composer/getcomposer.org/issues/82
if [ -f "${RPM_BUILD_ROOT}%{prefix}/error_log" ]; then
	rm -fv "${RPM_BUILD_ROOT}%{prefix}/error_log"
fi



%clean
if [ ! -z "%{_topdir}" ]; then
	%{__rm} -rf --preserve-root "%{_topdir}" \
		|| echo "Failed to delete build root (probably fine..)"
fi



### Files ###
%files
%defattr(-,root,root,-)
%{prefix}/composer
%{prefix}/box
