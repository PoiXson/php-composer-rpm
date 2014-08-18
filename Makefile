mock: clean prepare
	mbt

rpmbuild: clean prepare
	mbt --buildstyle=rpmbuild

clean:
	rm -rf BUILD BUILDROOT SRPMS RPMS SOURCES/composer.phar

prepare:
	mkdir -p BUILD RPMS/noarch SRPMS SOURCES
	curl -s -z SOURCES/composer.phar -o SOURCES/composer.phar https://getcomposer.org/composer.phar
